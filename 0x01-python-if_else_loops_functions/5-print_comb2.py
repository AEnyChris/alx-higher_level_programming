#!/usr/bin/python3
for n in range(0, 100):
    if n < 99:
        print("{:02}".format(n), end=", ")
    else:
        print(n)
