def found_duplicate(nums):
    count = 0
    duplicate = 0
    for i in range(len(nums)):

        for j in range(i + 1, len(nums)):
            if (nums[j] == nums[i]):
                duplicate = nums[j]
                count = count + 1
    if count == 0:
        return False
    return duplicate


def find_duplicate(nums):
    if (nums == [] or type(nums[0]) == str or len(nums) == 0 or nums[0] < 0):
        return False

    return found_duplicate(nums)
