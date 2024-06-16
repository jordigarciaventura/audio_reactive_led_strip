import sys
from cx_Freeze import setup, Executable

# build_exe_options = {"packages": ["SoundCard"]}

# base="Win32GUI" should be used only for Windows GUI app
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name="audio_reactive_led_strip",
    version="0.1.0",
    description="Get audio from your computer and transform it in RGB colors that you can send to a led strip.",
    executables=[Executable("cli.py", base=base, target_name="ARLEDS")],
    author="Jordi García Ventura",
    author_email="jordigarciaventura@gmail.com",
    license="MIT",
    python_requires=">=3.6.0",
    optimize=2,
)
