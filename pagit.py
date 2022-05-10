import sys

from commands import *

""" Code for later
for i in os.listdir(".git/objects"):
    if i not in ("pack", "info"):
        for j in os.listdir(f".git/objects/{i}"):
            print(zlib.decompress(open(f".git/objects/{i}/{j}", "rb").read()))"""

if len(sys.argv) < 2:
    print("python <path_to_pagit>/pagit.py <command> <subcommand> [arguments]")
else:
    match sys.argv[1]:
        case "log":
            log(int(sys.argv[2]) if len(sys.argv) > 2 else 2)
        case "rm-all":
            rm_all()
        case "object":
            print_obj(sys.argv[2:])