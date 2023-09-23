#!/usr/bin/python3
def islower(c):
    return 97 <= ord(c) <= 122

def uppercase(input_str):
    for char in input_str:
        if islower(char):
            uppercase_char = chr(ord(char) - ord('a') + ord('A'))
            print(uppercase_char, end='')
        else:
            print(char, end='')
    
    print()
