from array import array
import string


def find_duplicate(nums):
    count = 0
    duplicate = 0
    if (
        nums == [] or
        type(nums[0]) == str or
        len(nums) == 0 or
        nums[0] < 0
        ):
        return False

    for i in range(len(nums)):

        for j in range(i + 1, len(nums)):
            if (
                nums[j] == nums[i] and
                i != j
                ):
                    duplicate = nums[j]
                    count = count + 1
    if count == 0:
        return False
    return duplicate