#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    msg = ""
    res = list()
    for i in range(list_length):
        msg = ""
        try:
            res.append(my_list_1[i] / my_list_2[i])
        except TypeError:
            msg = 'wrong type'
            print(msg)
            res.append(0)
        except IndexError:
            msg = 'out of range'
            print(msg)
            res.append(0)
        except ZeroDivisionError:
            msg = 'division by 0'
            print(msg)
            res.append(0)
        finally:
            pass
    return res
