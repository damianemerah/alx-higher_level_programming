#!/usr/bin/python3
def common_elements(set_1, set_2):
    new_list = []
    for i, j in zip(set_1, set_2):
        if i in set_2 and j in set_1:
            new_list.append(i)
    return new_list
