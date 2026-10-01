#!/usr/bin/env python3

def dec_to_bin(decimal_integer):
    binary_digits = []
    binary_integer = 0
    while decimal_integer != 0:
        binary_integer = decimal_integer % 2
        binary_digits.append(str(binary_integer)) 
        decimal_integer = decimal_integer // 2
    binary_string = "".join(reversed(binary_digits))
    print(binary_string)

def main():
    user_input = int(input("Enter a decimal (base 10) number: "))
    dec_to_bin(user_input)

if __name__ == "__main__":
    main()