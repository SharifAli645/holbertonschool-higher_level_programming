#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None:
        return 0
    roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500,
             "M": 1000}
    cnt = 0
    for ele in roman_string:
        if roman.get(ele) > cnt:
            cnt = roman.get(ele) - cnt
        else:
            cnt = cnt + roman.get(ele)
    return cnt
