#!/usr/bin/env python3
import random
nombre = input("Dame un nombre")
nombres = []
while nombre != "":
    nombre = input("Dime un nombre de nuevo")
    nombres.append(nombre)
print(f"{random.choice([nombres])}")
