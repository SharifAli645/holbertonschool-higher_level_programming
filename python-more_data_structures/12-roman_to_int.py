#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or not isinstance(roman_string, str):
        return 0
    roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500,
             "M": 1000}
    cnt = 0
    last = 0
    for ele in reversed(roman_string):
        if roman.get(ele) >= last:
            cnt = roman.get(ele) + cnt
            last = roman.get(ele)
        else:
            cnt = cnt - roman.get(ele)
    return cnt
