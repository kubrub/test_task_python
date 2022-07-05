import os


def task1_create_full_path_of_directories(path):
    try:
        os.makedirs(path, exist_ok=True)
        return True
    except OSError as error:
        return False
