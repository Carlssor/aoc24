import inspect
import os


def read_puzzle_input(example: bool = False):
    input_file_name_modifier = "_example" if example else ""
    input_file_name = f"input{input_file_name_modifier}_{_get_puzzle_number()}.txt"
    if not os.path.exists(input_file_name):
        input_file_name = f"input{input_file_name_modifier}.txt"
    with open(os.path.join(_get_input_path(), input_file_name)) as f:
        return f.readlines()


def _get_input_path():
    return os.path.dirname(_get_caller_file())


def _get_puzzle_number():
    return int(_get_caller_file().split("puzzle")[1].split(".")[0])


def _get_caller_file():
    frame = inspect.currentframe()
    while not "puzzle" in frame.f_code.co_filename:
        frame = frame.f_back
    module = inspect.getmodule(frame)
    return module.__file__
