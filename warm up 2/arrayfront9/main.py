"""
Given an array of ints, return True if one of the first 4 elements in the array is a 9.
The array length may be less than 4.

array_front9([1, 2, 9, 3, 4]) → True
array_front9([1, 2, 3, 4, 9]) → False
array_front9([1, 2, 3, 4, 5]) → False

"""


def array_front9(nums):
    array_4 = nums[:4]
    flag = 0
    if len(nums) < 4:
        for num in nums:
            if num == 9:
                flag = 1
    else:
        for number in array_4:
            if number == 9:
                flag = 1

    if flag == 1:
        return True
    else:
        return False


d = array_front9([1, 2, 6, 3, 4])



