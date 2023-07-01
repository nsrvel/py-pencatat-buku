import shutil

def get_terminal_size():
    return shutil.get_terminal_size().columns
