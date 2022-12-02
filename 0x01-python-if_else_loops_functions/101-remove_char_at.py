#!/usr/bin/python3
def remove_char_at(str, n):
    length = len(str)
    return (str[:n] + str[n + 1 : length])
