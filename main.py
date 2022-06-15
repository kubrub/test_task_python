import os
from pathlib import Path

def task1_create_full_path_of_directories(path):
    ssh = Path(path)
    try:
        ssh.mkdir(parents=True)
    except OSError:
        print(False)
    else:
        print(True)


path = os.getcwd()
print("The current working directory is %s" % path)

ssh_path = input("Input path to create - ")


#ssh_path = "/Users/mac/Desktop/tmp/year/month/week/day"
task1_create_full_path_of_directories(ssh_path)
