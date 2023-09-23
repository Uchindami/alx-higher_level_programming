#!/usr/bin/python3

def fizzbuzz():
    for num in range(1, 101):
        output = ""
        output += "Fizz" if num % 3 == 0 else ""
        output += "Buzz" if num % 5 == 0 else ""
        print(output or num, end=' ')

