#!/usr/bin/python3


def safe_print_division(a, b):
    # a function that divides 2 integers and prints the results
    try:
        ans = a / b
    except (TypeError, ZeroDivisionError):
        ans = None
    finally:
        print("Inside result: {}".format(ans))
    return ans
