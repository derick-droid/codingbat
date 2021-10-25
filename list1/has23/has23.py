"""
Given an int array length 2, return True if it contains a 2 or a 3.

has23([2, 5]) → True
has23([4, 3]) → True
has23([4, 5]) → False

"""


def has23(nums):
    if len(nums) == 2:
        if 2 in nums[0:] or 3 in nums[0:] :
            return True
        else:
            return False
    else:
        return False

