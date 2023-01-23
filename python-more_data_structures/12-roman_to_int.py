#!/usr/bin/python3


roman = {}
roman['I'] = 1
roman['V'] = 5
roman['X'] = 10
roman['L'] = 50
roman['C'] = 100
roman['D'] = 500
roman['M'] = 1000

def roman_to_int(roman_string):

    sum = 0
    n = len(roman_string)

    for i in range(len(roman_string)):
        if roman.get(roman_string[i], 0) == 0:
            return 0

        if i != n - 1 and roman[roman_string[i]] < roman[roman_string[i + 1]]:
            sum += roman[roman_string[i + 1]] - roman[roman_string[i]]
 
        else:
            sum += roman[roman_string[i]]

    return sum
