"""
Given an array of ints, return True if the array contains a 2 next to a 2 somewhere.

has22([1, 2, 2]) → True
has22([1, 2, 1, 2]) → False
has22([2, 1, 2]) → False
"""


def has22(nums):
    if len(nums) <= 1:
        return False

    else:
        for num in range(0, len(nums) - 1):
            if nums[num] == 2 and nums[num + 1] == 2:
               return True

    return False
