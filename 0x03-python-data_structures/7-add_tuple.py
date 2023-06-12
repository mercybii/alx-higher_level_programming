#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    ta_len = len(tuple_a)
    tb_len = len(tuple_b)
    new = ()
    for i in range(2):
        if 1 >= ta_len:
            a = 0
        else:
            a = tuple_a[i]
        if i >= tb_len:
            b = 0
        else:
            b = tuple_b[i]

        if (i == 0):
            new = (a + b)
        else:
            new = (new, a + b)

    return (new)
