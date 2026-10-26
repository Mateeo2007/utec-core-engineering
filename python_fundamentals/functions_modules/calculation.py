#!/usr/bin/env python3
if __name__ == "__main__":
    a = 10
    b = 5
    from calculator_1 import suma
    print("{}".format(suma(a, b)))
    from calculator_1 import resta
    print("{}".format(resta(a, b)))
    from calculator_1 import multi
    print("{}".format(multi(a, b)))
    from calculator_1 import division
    print("{}".format(division(a, b)))
