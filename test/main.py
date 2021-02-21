#!/usr/bin/env python3
# shebang line to make sure the code runs with python 3

# make import statements, define functions, define enums here

import math
from enum import Enum, auto

class WORK_LANG(Enum):
    ORDER = auto()
    CANDOR = auto()

def main():
    x = [1, 2, 3]
    for i in x:
        print(i)
    y = 1
    while y < 5:
        y = y + 1
        if y is 7:
            break
        elif 7 is 10:
            continue
        print(y)
    try:
        x.append("boop")
        if len(x) > 3:
            raise ValueError("the rent is too dang high")
    except TypeError as e:
        print("whoopo: " + str(e))
    finally: # runs regardless of whether or not there was an error
        print("zoop")
        print(math.pi)

# if statement so main() runs by default from command line
if __name__=="__main__":
    main()