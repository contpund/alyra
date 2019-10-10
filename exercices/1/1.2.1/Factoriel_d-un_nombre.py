#!/usr/bin/env python3
value = input("Enter tour value: ")

def facto(n):
    init = n
    res = n
    i = -1
    while n > 1:
        i=i+1
        res = res * (n - 1)
        n = n-1 
    return print( "Nombre d'opérations effectué ",i,"\nLe factorielle de ",init," est :", res)


facto(int(value))