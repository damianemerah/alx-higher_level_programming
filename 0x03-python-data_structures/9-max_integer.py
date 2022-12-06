#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list == '':
        return "None"
    length = len(my_list) - 1
    i = 0
    while i < length:
        if my_list[i] > my_list[i + 1]:
            temp = my_list[i]
            my_list[i] = my_list[i + 1]
            my_list[i + 1] = temp
        i += 1
    return (my_list[len(my_list) - 1])
