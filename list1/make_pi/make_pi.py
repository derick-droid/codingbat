"""
Return an int array length 3 containing the first 3 digits of pi, {3, 1, 4}.

make_pi() → [3, 1, 4]

"""


def make_pi(nums):
    if len(nums) < 3:
        return False
    else:
        if nums[:4] == [3, 1, 4]:
            return True

        else:
            return False


