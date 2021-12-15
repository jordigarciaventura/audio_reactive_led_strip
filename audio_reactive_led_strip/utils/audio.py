import numpy as np
from scipy.ndimage.filters import gaussian_filter1d

from ..common import config
from .melbank import compute_melmat


# def db(data):
#     db = np.max(np.abs(data))
#     if db > 1: return 1
#     return db

# def rgb(db):
#     r, g, b = hsv_to_rgb(db, 1, 1)
#     return r, g, b

# def hsv_to_rgb(h, s, v):
#     if s == 0.0: return (v, v, v)
#     i = int(h*6.) # XXX assume int() truncates!
#     f = (h*6.)-i; p,q,t = v*(1.-s), v*(1.-s*f), v*(1.-s*(1.-f)); i%=6
#     if i == 0: return (v, t, p)
#     if i == 1: return (q, v, p)
#     if i == 2: return (p, v, t)
#     if i == 3: return (p, q, v)
#     if i == 4: return (t, p, v)
#     if i == 5: return (v, p, q)

# def scroll(arr, value):
#     data = np.roll(arr, 1)
#     data[0] = value
#     return data

# def symetry(arr):
#     return np.concatenate([arr[::-1], arr])

# def rms(data):
#     """Given audio fragment, return the root mean square."""
#     return np.sqrt(np.sum(data**2)/len(data))

# def db_from_pressure(pressure):
#     return 20 * np.log10(pressure)

class DBMeter:
    def __init__(self, decrement):
        self.db = 0
        self.decrement = decrement

    def update(self, data):
        
        self._decrease()

        db = max(abs(data))

        if db >= 1:
            self.db = 1
            return 1
        if db > self.db:
            self.db = db
        return self.db

    def _decrease(self):
        self.db -= self.decrement
        if self.db < 0:
            self.db = 0

class ExpFilter:
    """Simple exponential smoothing filter"""
    def __init__(self, val=0.0, alpha_decay=0.5, alpha_rise=0.5):
        """Small rise / decay factors = more smoothing"""
        assert 0.0 < alpha_decay < 1.0, 'Invalid decay smoothing factor'
        assert 0.0 < alpha_rise < 1.0, 'Invalid rise smoothing factor'
        self.alpha_decay = alpha_decay
        self.alpha_rise = alpha_rise
        self.value = val

    def update(self, value):
        if isinstance(self.value, (list, np.ndarray, tuple)):
            alpha = value - self.value
            alpha[alpha > 0.0] = self.alpha_rise
            alpha[alpha <= 0.0] = self.alpha_decay
        else:
            alpha = self.alpha_rise if value > self.value else self.alpha_decay
        self.value = alpha * value + (1.0 - alpha) * self.value
        return self.value

class AudioVisualizer():

    def __init__(self,  n_fft_bins=24, n_samples=735, n_rolling_history=2, n_pixels=60, min_volume_threshold=1e-6,
                        min_frequency = 200, max_frequency=12000):
        self.n_fft_bins = n_fft_bins
        self.n_samples = n_samples
        self.n_rolling_history = n_rolling_history
        self.n_pixels = n_pixels
        self.min_volume_threshold = min_volume_threshold
        self.min_frequency = min_frequency
        self.max_frequency = max_frequency

        # frequency
        self.fft_plot_filter = ExpFilter(np.tile(0.1, self.n_fft_bins),
                         alpha_decay=0.5, alpha_rise=0.99)
        self.mel_gain = ExpFilter(np.tile(0.1, self.n_fft_bins),
                         alpha_decay=0.01, alpha_rise=0.99)
        self.mel_smoothing = ExpFilter(np.tile(0.1, self.n_fft_bins),
                         alpha_decay=0.5, alpha_rise=0.99)
        self.fft_window = np.hamming(self.n_samples * self.n_rolling_history)
        self.y_roll = np.random.rand(self.n_rolling_history, self.n_samples) / 1e16

        # spectrum
        self._prev_spectrum = np.tile(0.01, n_pixels // 2)

        self.r_filt = ExpFilter(np.tile(0.01, self.n_pixels // 2),
                       alpha_decay=0.2, alpha_rise=0.99)
        self.b_filt = ExpFilter(np.tile(0.01, self.n_pixels // 2),
                       alpha_decay=0.1, alpha_rise=0.5)
        self.common_mode = ExpFilter(np.tile(0.01, self.n_pixels // 2),
                       alpha_decay=0.99, alpha_rise=0.01)

        self._melUpdated = False

        self.r = np.zeros(self.n_pixels)
        self.g = np.zeros(self.n_pixels)
        self.b = np.zeros(self.n_pixels)

        # energy
        self.p_filt = ExpFilter(np.tile(1, (3, self.n_pixels // 2)),
                       alpha_decay=0.1, alpha_rise=0.99)
        self.p = np.tile(1.0, (3, self.n_pixels // 2))
        self.gain = ExpFilter(np.tile(0.01, self.n_fft_bins),
                            alpha_decay=0.001, alpha_rise=0.99)

        self.effects = {
            "Energy": self.energyEffect,
            "Scroll": self.scrollEffect,
            "Spectrum": self.spectrumEffect,
        }
        self.effect = self.effects["Energy"]

        self.intensity = 1

    effectNames = ["Energy", "Scroll", "Spectrum"]

    def setData(self, data):
        self.data = data
        self.effect()

    def setEffect(self, effectName):
        self.effect = self.effects[effectName]

    def getRGB(self):
        return self.r * self.intensity, self.g * self.intensity, self.b * self.intensity

    def frequency(self):
        
        y = self.data

        # Construct a rolling window of audio samples
        self.y_roll[:-1] = self.y_roll[1:]
        self.y_roll[-1] = np.copy(y)
        ydata = np.concatenate(self.y_roll, axis=0).astype(np.float32)

        vol = np.max(np.abs(ydata))
        if vol < self.min_volume_threshold:
            self._mel = np.zeros(self.n_fft_bins)
            x = np.linspace(self.min_frequency, self.max_frequency, self.n_fft_bins)
            y = np.zeros(self.n_fft_bins)
            return x, y
        else:
            # Transform audio input into the frequency domain
            N = len(ydata)
            ydata *= self.fft_window
            # Pad with zeros until the next power of two
            N_zeros = 2**int(np.ceil(np.log2(N))) - N
            y_padded = np.pad(ydata, (0, N_zeros))
            YS = np.abs(np.fft.rfft(y_padded)[:N // 2])
            # Construct a Mel filterbank from the FFT data
            self._mel = np.atleast_2d(YS).T * mel_y.T
            self._mel = np.sum(self._mel, axis=0)
            # Scale data to values more suitable for visualization
            self._mel = self._mel**2.0
            # Gain normalization
            self.mel_gain.update(np.max(gaussian_filter1d(self._mel, sigma=1.0)))
            self._mel /= self.mel_gain.value
            self._mel = self.mel_smoothing.update(self._mel)

            self._melUpdated = True

            x = np.linspace(self.min_frequency, self.max_frequency, len(self._mel))
            return x, self.fft_plot_filter.update(self._mel)

    def spectrumEffect(self):
        if not self._melUpdated:
            self.frequency()
        self._melUpdated = False

        y = self._mel

        """Effect that maps the Mel filterbank frequencies onto the LED strip"""
        y = np.copy(interpolate(y, self.n_pixels // 2))
        self.common_mode.update(y)
        diff = y - self._prev_spectrum
        self._prev_spectrum = np.copy(y)
        # Color channel mappings
        self.r = self.r_filt.update(y - self.common_mode.value)
        self.g = np.abs(diff)
        self.b = self.b_filt.update(np.copy(y))
        # Mirror the color channels for symmetric output
        self.r = np.concatenate((self.r[::-1], self.r)) * 255
        self.g = np.concatenate((self.g[::-1], self.g)) * 255
        self.b = np.concatenate((self.b[::-1], self.b)) * 255
        return self.r, self.g, self.b

    def scrollEffect(self):
        if not self._melUpdated:
            self.frequency()
        self._melUpdated = False

        y = self._mel
        
        """Effect that originates in the center and scrolls outwards"""
        y = y**2.0
        self.gain.update(y)
        y /= self.gain.value
        y *= 255.0
        r = int(np.max(y[:len(y) // 3]))
        g = int(np.max(y[len(y) // 3: 2 * len(y) // 3]))
        b = int(np.max(y[2 * len(y) // 3:]))
        # Scrolling effect window
        self.p[:, 1:] = self.p[:, :-1]
        self.p *= 0.98
        self.p = gaussian_filter1d(self.p, sigma=0.2)
        # Create new color originating at the center
        self.p[0, 0] = r
        self.p[1, 0] = g
        self.p[2, 0] = b

        self.r, self.g, self.b = np.concatenate((self.p[:, ::-1], self.p), axis=1)
        return self.r, self.g, self.b

    def energyEffect(self):
        if not self._melUpdated:
            self.frequency()
        self._melUpdated = False

        y = self._mel

        """Effect that expands from the center with increasing sound energy"""
        y = np.copy(y)
        self.gain.update(y)
        y /= self.gain.value
        # Scale by the width of the LED strip
        y *= float((self.n_pixels // 2) - 1)
        # Map color channels according to energy in the different freq bands
        scale = 0.9
        r = int(np.mean(y[:len(y) // 3]**scale))
        g = int(np.mean(y[len(y) // 3: 2 * len(y) // 3]**scale))
        b = int(np.mean(y[2 * len(y) // 3:]**scale))
        # Assign color to different frequency regions
        self.p[0, :r] = 255.0
        self.p[0, r:] = 0.0
        self.p[1, :g] = 255.0
        self.p[1, g:] = 0.0
        self.p[2, :b] = 255.0
        self.p[2, b:] = 0.0
        self.p_filt.update(self.p)
        self.p = np.round(self.p_filt.value)
        # Apply substantial blur to smooth the edges
        self.p[0, :] = gaussian_filter1d(self.p[0, :], sigma=4.0)
        self.p[1, :] = gaussian_filter1d(self.p[1, :], sigma=4.0)
        self.p[2, :] = gaussian_filter1d(self.p[2, :], sigma=4.0)

        # Set the new pixel value
        self.r, self.g, self.b = np.concatenate((self.p[:, ::-1], self.p), axis=1)
        return self.r, self.g, self.b

def rfft(data):
    y = np.abs(np.fft.rfft(data))
    x = np.fft.rfftfreq(len(data), 1./44100)
    return x, y

def create_mel_bank():
    global samples, mel_y, mel_x
    samples = int(config.MIC_RATE * config.N_ROLLING_HISTORY / (2.0 * config.FPS))
    mel_y, (_, mel_x) = compute_melmat(num_mel_bands=config.N_FFT_BINS,
                                               freq_min=config.MIN_FREQUENCY,
                                               freq_max=config.MAX_FREQUENCY,
                                               num_fft_bands=samples,
                                               sample_rate=config.MIC_RATE)

samples = None
mel_y = None
mel_x = None
create_mel_bank()

def memoize(function):
    """Provides a decorator for memoizing functions"""
    from functools import wraps
    memo = {}

    @wraps(function)
    def wrapper(*args):
        if args in memo:
            return memo[args]
        else:
            rv = function(*args)
            memo[args] = rv
            return rv
    return wrapper


# @memoize
def _normalized_linspace(size):
    return np.linspace(0, 1, size)


def interpolate(y, new_length):
    """Intelligently resizes the array by linearly interpolating the values

    Parameters
    ----------
    y : np.array
        Array that should be resized

    new_length : int
        The length of the new interpolated array

    Returns
    -------
    z : np.array
        New array with length of new_length that contains the interpolated
        values of y.
    """
    if len(y) == new_length:
        return y
    x_old = _normalized_linspace(len(y))
    x_new = _normalized_linspace(new_length)
    z = np.interp(x_new, x_old, y)
    return z