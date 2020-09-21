#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    idx = 0
    new_list = []
    while idx < list_length:
        new_item = 0
        try:
            new_item = my_list_1[idx] / my_list_2[idx]
        except IndexError:
            print("out of range")
        except TypeError:
            print("wrong type")
        except ZeroDivisionError:
            print("division by 0")
        finally:
            new_list.append(new_item)
        idx += 1
    return new_list
