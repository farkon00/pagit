import zlib
import os
import utils

def log(num: int):
    with open(".git/logs/HEAD", "r") as f:
        log = f.read()[:-1].split("\n")

    for i in log[-num:]:
        info = i.split()
        print(utils.prettify_log(info))

def rm_all():
    inp = input("Are you sure you want to remove all files from repo? (y/N) ")
    if inp.lower() == "y":
        os.remove(".git/index")
    else:
        print("Aborted")

def print_obj(args: list[str]):
    if len(args) != 1:
        print("Usage: test-obj <folder> <hash>")
        return

    print(utils.decode_object(f".git/objects/{args[0][:2]}/{args[0][2:]}"))