#!/usr/bin/env python3
for value in range (0, 100):
        if value <= 98:
            print(f"{value:02d}".format(str), end=", ")
        if value == 99:
            print(f"{value:02d}".format(str), end="\n")
