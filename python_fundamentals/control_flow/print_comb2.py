#!/usr/bin/env python3
for value in range (0, 99):
        ending = ", " if value < 5 else "\n"
        print(f"{value:02d}".format(str), end=", ")
