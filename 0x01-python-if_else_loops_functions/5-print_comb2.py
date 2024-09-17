#!/usr/bin/python3
for n in range(0, 100):
    if n < 10:
        print(f"0{n}", end=", ")
    elif n < 99:
        print(n, end=", ")
    else:
        print(n)
