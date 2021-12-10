import sys
from cx_Freeze import setup, Executable

# build_exe_options = {"packages": ["SoundCard"]}

# base="Win32GUI" should be used only for Windows GUI app
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name = "audio_reactive_led_strip",
    version = "0.1",
    description = "My GUI application!",
    # options = {"build_exe": build_exe_options},
    executables = [Executable("cli.py", base=base)]
)