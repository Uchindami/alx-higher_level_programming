#!/usr/bin/python3
import sys


def main():
    number_counter = len(sys.argv) - 1

    print(f"{number_counter} argument{'s' if number_counter != 1 else ''}:")

    for i in range(number_counter):
        print(f"{i + 1}: {sys.argv[i + 1]}")


if __name__ == "__main__":
    main()
