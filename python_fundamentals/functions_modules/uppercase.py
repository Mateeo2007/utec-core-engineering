#!/usr/bin/env python3
def uppercase(str):
    for letra in str:
        codigo = ord(letra)
        if 97 <= codigo <= 122:
            mayuscula = chr(codigo - 32)
        else:
            mayuscula = letra
        print("{}".format(mayuscula), end="")
    print()
