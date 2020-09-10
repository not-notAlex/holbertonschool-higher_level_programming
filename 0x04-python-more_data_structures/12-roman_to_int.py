#!/usr/bin/python3
def roman_to_int(roman_string):
    total = 0
    if not isinstance(roman_string, str):
        return 0
    elif roman_string:
        rom = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        for i in range(0, len(roman_string)):
            if roman_string[i] in list(rom.keys()):
                total += rom[roman_string[i]]
            if (i + 1) < len(roman_string):
                if roman_string[i] == 'I' and roman_string[i + 1] == 'X':
                    total -= 2
                if roman_string[i] == 'I' and roman_string[i + 1] == 'V':
                    total -= 2
                if roman_string[i] == 'X' and roman_string[i + 1] == 'L':
                    total -= 20
                if roman_string[i] == 'X' and roman_string[i + 1] == 'C':
                    total -= 20
                if roman_string[i] == 'C' and roman_string[i + 1] == 'D':
                    total -= 200
                if roman_string[i] == 'C' and roman_string[i + 1] == 'M':
                    total -= 200
    return total
