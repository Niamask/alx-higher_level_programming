#!/usr/bin/python3

def no_c(my_string):
    return("".join([i if i not in "cC" else '' for i in my_string]))
