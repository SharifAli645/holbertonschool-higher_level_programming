#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    cnt = 0
    try:
        for i in range(x):
            print("{:d}".format(my_list[i]), end="")
            cnt = cnt + 1
    except:
        print("")
        return cnt
    print("")
    return cnt
