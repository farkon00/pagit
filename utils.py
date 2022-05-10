import datetime
import zlib

def prettify_log(info: list[str]) -> str:
    return \
f"""
Hash: {info[1]}
Author: {info[2]} {info[3]}
Date: {datetime.datetime.fromtimestamp(int(info[4]))} {info[5]}
{" ".join(info[6:])}
"""

def decode_object(file: str) -> str:
    with open(file, "rb") as f:
        return zlib.decompress(f.read()).decode()