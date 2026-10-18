#!/usr/bin/env python3


def pow(a, b):
    resultado = 1
    for i in range(abs(b)):
        resultado *= a
    if b < 0:
        return 1 / resultado
    return resultado
