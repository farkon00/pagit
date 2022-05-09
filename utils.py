import datetime

def prettify_log(info: list[str]) -> str:
    return \
f"""
Hash: {info[1]}
Author: {info[2]} {info[3]}
Date: {datetime.datetime.fromtimestamp(int(info[4]))} {info[5]}
{" ".join(info[6:])}
"""