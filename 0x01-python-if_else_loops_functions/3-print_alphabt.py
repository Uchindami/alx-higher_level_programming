#!/usr/bin/python3
for char_code in range(97, 123):
    if chr(char_code) not in ('q', 'e'):
        print("{}".format(chr(char_code)), end="")
