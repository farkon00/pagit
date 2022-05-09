import zlib
import os
import datetime

def last_obj():
    with open(".git/logs/refs/heads/main", "r") as f:
        log = f.read()[:-1]

    last_log = log[log.rfind("\n")+1:]
    info = last_log.split()
    print(
f"""
Hash: {info[1]}
Author: {info[2]} {info[3]}
Date: {datetime.datetime.fromtimestamp(int(info[4]))} {info[5]}
{" ".join(info[6:])}
"""
    )

def log_actions(num: int):
    with open(".git/logs/refs/heads/main", "r") as f:
        log = f.read()[:-1].split("\n")

    for i in log[len(log)-num:]:
        info = i.split()
        print(
f"""
Hash: {info[1]}
Author: {info[2]} {info[3]}
Date: {datetime.datetime.fromtimestamp(int(info[4]))} {info[5]}
{" ".join(info[6:])}
"""
        )