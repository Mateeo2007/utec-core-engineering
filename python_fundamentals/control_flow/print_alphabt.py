#!/usr/bin/env python3
for letter in range(ord("a"), ord("z") + 1):
    if chr(letter) in "qe":
        continue
    print(chr(letter), end="")
