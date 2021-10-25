"""
Given a string of even length, return the first half. So the string "WooHoo" yields "Woo".

first_half('WooHoo') → 'Woo'
first_half('HelloThere') → 'Hello'
first_half('abcdef') → 'abc'

"""


def first_half(str):
    if len(str) % 2 == 0:
        index = str[:int(len(str) / 2)]
        return index
    else:
        return False


