#!/usr/bin/env python3
value = input("Enter tour value: ")

def factorielle(n):
    if n == 0 or n == 1:
        return 1
    else:
        print("opération ",n)
        return n * factorielle(n - 1)

factorielle(int(value))