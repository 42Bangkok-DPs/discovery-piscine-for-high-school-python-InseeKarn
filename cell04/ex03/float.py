#!/usr/bin/env python3

def check_number(number):
    if number.is_integer():
        print("This number is an interger")
    else:
        print("This number is a decimal.")

num = (input("Give me a number: "))


try:
    number = float(num)
    check_number(number)
except ValueError:
    print('Error')
