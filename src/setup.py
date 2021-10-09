import sys
from cx_Freeze import setup, Executable

setup(
    name = "play_sudoku_gui",
    version = "1",
    description = "Play to the Sudoku with a GUI",
    executables = [Executable("play_sudoku_gui.py")]
)