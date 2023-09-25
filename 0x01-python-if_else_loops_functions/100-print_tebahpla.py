#!/usr/bin/python3

counter = 0
for character in range(ord('z'), ord('a') - 1, -1):
    print("{}".format(chr(character - counter)), end="")
    counter = 32 if counter == 0 else 0
