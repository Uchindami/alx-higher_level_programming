#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0

    weighted_sum = sum(tup[0] * tup[1] for tup in my_list)
    total_weight = sum(tup[1] for tup in my_list)

    return weighted_sum / total_weight
