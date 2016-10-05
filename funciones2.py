# -*- coding: UTF-8 -*-

def numero_mayor(*args):
    print max(args)
    return max(args)
    
def numero_menor(*args):
    print min(args)
    return min(args)

def distancia_desde_cero(arg):
    print abs(arg)
    return abs(arg)


numero_mayor(-10, -5, 5, 10)
numero_menor(-10, -5, 5, 10)
distancia_desde_cero(-10)
