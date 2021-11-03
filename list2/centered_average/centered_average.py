"""
Return the "centered" average of an array of ints, which we'll say is the mean average of the values,
except ignoring the largest and smallest values in the array. If there are multiple copies of the smallest
value, ignore just one copy, and likewise for the largest value. Use int division to produce the final average. You may assume that the array is length 3 or more.

centered_average([1, 2, 3, 4, 100]) → 3
centered_average([1, 1, 5, 5, 10, 8, 7]) → 5
centered_average([-10, -4, -2, -4, -2, 0]) → -3
"""


def centered_average(nums):
    real_list = sorted(nums)
    total = 0
    count = 0
    if len(nums) < 3:
        print(False)
    elif len(nums) == 3:
        print(real_list[1])
    elif len(nums) > 3:
        for items in real_list[1:-1]:
            count += 1
        for number in real_list[1:-1]:
            total += number

    return total // count






#


