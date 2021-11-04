"""
Return the sum of the numbers in the array, returning 0 for an empty array.
Except the number 13 is very unlucky, so it does not count and numbers that come immediately after a
13 also do not count.

sum13([1, 2, 2, 1]) → 6
sum13([1, 1]) → 2
sum13([1, 2, 2, 1, 13]) → 6
"""


def sum13(nums):
    summation = 0
    if len(nums) > 0 and nums[0] != 13:
        summation = nums[0]
    for num in range(1, len(nums), 1):
        if nums[num] != 13 and nums[num - 1] != 13:
            summation += nums[num]

    return summation


