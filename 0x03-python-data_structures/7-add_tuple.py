#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    tuple_c=()
    c = []

    a = list(tuple_a)
    b = list(tuple_b)

    if len(tuple_a) < 2 or len(tuple_b) < 2:
        for i in range(2):
            if not a[i]:
                a.insert(i, 0)
            if not b[i]:
                b.insert(i, 0)

    for i in range(2):
        c.append(a[i] + b[i])
    tuple_c = tuple(c)
    return tuple_c

