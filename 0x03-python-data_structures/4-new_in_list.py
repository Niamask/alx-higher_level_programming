#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    copie_list = []
    for i in range(len(my_list)):
        copie_list.append(my_list[i])

    if idx >= 0 and idx < len(copie_list):
        copie_list[idx] = element
        return copie_list
