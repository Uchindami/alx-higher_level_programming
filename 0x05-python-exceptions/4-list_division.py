#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    quotient = []

    try:
        for i in range(list_length):
            try:
                first_value = my_list_1[i] if i < len(my_list_1) else 0
                second_value = my_list_2[i] if i < len(my_list_2) else 0

                if not isinstance(first_value, (int, float)) or not isinstance(second_value, (int, float)):
                    raise ValueError("wrong type")

                if second_value == 0:
                    raise ZeroDivisionError("division by 0")

                division_quotient = first_value / second_value
                quotient.append(division_quotient)
            except ValueError as ve:
                print(ve)
                quotient.append(0)
            except ZeroDivisionError as zde:
                print(zde)
                quotient.append(0)
            except IndexError:
                print("out of range")
                quotient.append(0)

    except Exception as e:
        print(e)

    return quotient
