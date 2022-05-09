import zlib
import os
import utils

def log_actions(num: int):
    with open(".git/logs/refs/heads/main", "r") as f:
        log = f.read()[:-1].split("\n")

    for i in log[len(log)-num:]:
        info = i.split()
        print(utils.prettify_log(info))