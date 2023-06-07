#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        print("Inside result: ", end="")
        res = a / b
    except Exception:
        res = None
        return None
    finally:
        print("{}".format(res))
        return res
