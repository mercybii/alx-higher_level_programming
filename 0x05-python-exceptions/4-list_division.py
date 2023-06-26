#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for i in range(0, list_length):
        try:
            c = my_list1[i] / my_list2[i]
        expect TypeError:
            print("Wrong Type")
            c = 0
        expect ZeroDivisionError:
            print("Division by 0")
            c = 0
        expect IndexError:
            print("out of range")
            c = 0
        finally:
            new_list.append(c)
        return new_list
