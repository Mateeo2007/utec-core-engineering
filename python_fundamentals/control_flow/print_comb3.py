#!/usr/bin/env python3
pares = ["{}{}".format(left, right) for left in range(10) for right in range(left + 1, 10)]
print(", ".join(pares), end="")
