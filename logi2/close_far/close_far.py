"""
Given three ints, a b c, return True if one of b or c is "close" (differing from a by at most 1),
while the other is "far", differing from both other values by 2 or more. Note: abs(num) computes the absolute
value of a number.

close_far(1, 2, 10) → True
close_far(1, 2, 3) → False
close_far(4, 1, 3) → True
"""


def close_far(a, b, c):
    diff_a_b = abs(a - b)
    diff_a_c = abs(a - c)
    diff_b_c = abs(b - c)

    if diff_a_b <= 1 and diff_b_c >= 2 and diff_a_c >= 2:
        return True
    elif diff_a_c <= 1 and diff_b_c >= 2 and diff_a_b >= 2:
        return True
    elif diff_b_c <= 1 and diff_a_c >= 2 and diff_a_b >= 2:
        return True
    else:
        return False


v = close_far(1, 2, 3)
