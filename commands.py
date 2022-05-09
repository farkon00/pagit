import zlib
import os
import utils

def log_actions(num: int):
    with open(".git/logs/refs/heads/main", "r") as f:
        log = f.read()[:-1].split("\n")

    for i in log[len(log)-num:]:
        info = i.split()
        print(utils.prettify_log(info))

def rm_all():
    inp = input("Are you sure you want to remove all files from repo? (y/N) ")
    if inp.lower() == "y":
        os.remove(".git/index")
    else:
        print("Aborted")