#!/usr/bin/python3
def remove_char_at(str, n):
    new = ""
    i = 0
    for c in str:
        if i != n:
            new += c
        i += 1
    return new
