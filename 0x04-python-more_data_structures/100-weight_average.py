#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) and my_list:
        denom = 0
        num = 0
        for x in my_list:
            num += (x[0] + x[1])
            denom += x[1]
        return (num/denom)
    return 0
