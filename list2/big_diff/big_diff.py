"""
Given an array length 1 or more of ints, return the difference between the largest and smallest
values in the array. Note: the built-in min(v1, v2) and max(v1, v2) functions return the smaller or
larger of two values.

big_diff([10, 3, 5, 6]) → 7
big_diff([7, 2, 10, 9]) → 8
big_diff([2, 10, 7, 2]) → 8
"""


def big_diff(nums):
    large = 0
    small = sorted(nums)  # sorting the array from largetest to the smallest
    if len(nums) <= 1:
        print(nums[0])
    else:
        for number in nums:
            if number > large:
                large = number

    return (large - small[0])

