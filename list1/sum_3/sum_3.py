"""
Given an array of ints length 3, return the sum of all the elements.

sum3([1, 2, 3]) → 6
sum3([5, 11, 2]) → 18
sum3([7, 0, 0]) → 7

"""


def sum3(nums):
    if len(nums) > 3:
        return False
    else:
        return (nums[0] + nums[1] + nums[2])

