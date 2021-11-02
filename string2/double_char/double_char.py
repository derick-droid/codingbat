"""
Given a string, return a string where for every char in the original, there are two chars.

double_char('The') → 'TThhee'
double_char('AAbb') → 'AAAAbbbb'
double_char('Hi-There') → 'HHii--TThheerree'

"""


def double_char(str):
    new_string = " "
    for ch in range(len(str)):
        after_double = str[ch] + str[ch]
        new_string += after_double
    return new_string


