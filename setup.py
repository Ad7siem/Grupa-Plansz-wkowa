import sys
import os
from cx_Freeze import setup, Executable

target = Executable(
    script='main_v2.py',
    base='Win32GUI'
)

setup(
    name = "GryPlanszowe",
    version = "0.1",
    description = "Modern GUI for Python applications",
    author = "Adam Golews",
    # options = {'build_exe' : {'include_files' : files}},
    executables = [target]
)

# import sys
# from cx_Freeze import setup, Executable

# # Dependencies are automatically detected, but it might need fine tuning.
# # "packages": ["os"] is used as example only
# build_exe_options = {"packages": ["os"], "excludes": ["tkinter"]}

# # base="Win32GUI" should be used only for Windows GUI app
# base = None
# if sys.platform == "win32":
#     base = "Win32GUI"

# setup(
#     name = "guifoo",
#     version = "0.1",
#     description = "My GUI application!",
#     options = {"build_exe": build_exe_options},
#     executables = [Executable("main_v2.py", base=base)]
# )