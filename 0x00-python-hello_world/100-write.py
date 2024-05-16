#!/usr/bin/python3

import sys

def hello_write():
    a = "and that piece of art is useful - Dora Korpar, 2015-10-19\n"
    sys.stderr.write(a)
    return 1

if __name__ == "__main__":
    sys.exit(hello_write())
