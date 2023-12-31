#!/usr/bin/python3
def roman_to_int(roman_string):
    roman_values = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }

    if not isinstance(roman_string, str):
        return 0

    result, prev_value = 0, 0
    for symbol in roman_string[::-1]:
        value = roman_values.get(symbol, 0)
        if value < prev_value:
            result -= value
        else:
            result += value
        prev_value = value

    return result
