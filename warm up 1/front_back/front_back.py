"""
Given a string, return a new string where the first and last chars have been exchanged.
front_back('code') → 'eodc'
front_back('a') → 'a'
front_back('ab') → 'ba'

"""


def front_back(str):

    if len(str) == 1:
        return str
    else:
        first = str[:1]
        last = str[-1:]
        remaining = str[1:-1]
    return last + remaining + first




