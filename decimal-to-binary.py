#!/usr/bin/env python3

def dec_to_bin(decimal_integer):
    binary_digits = []
    binary_integer = 0
    while decimal_integer != 0:
        binary_integer = decimal_integer % 2
        binary_digits.append(binary_integer) 
        decimal_integer = decimal_integer // 2
    print(binary_digits)
    
dec_to_bin(97)
