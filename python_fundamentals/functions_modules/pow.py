#!/usr/bin/env python3
def pow(a, b):
    #devolver el valor de a elevado a la potencia de b
    if 0 > b:
        pot = 1
        for _ in range (-b):
            pot /= a
        return pot
    pot = 1
    for _ in range(b):
        pot *= a
    return pot
