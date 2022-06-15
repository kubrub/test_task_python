from pathlib import Path


def task1_create_full_path_of_directories(path):
    ssh = Path(path)
    try:
        ssh.mkdir(parents=True)
    except OSError:
        print(False)
    else:
        print(True)