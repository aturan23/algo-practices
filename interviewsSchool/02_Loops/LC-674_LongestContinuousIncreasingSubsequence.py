"""
Runtime: 56 ms
Memory Usage: 14.4 MB
"""
from timeit import default_timer as timer


def findLengthOfLCIS(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if len(nums) == 0: return 0

    maxLength = 1
    count = 1

    for i in range(1, len(nums)):
        if nums[i] > nums[i - 1]:
            count += 1
        else:
            count = 1

        maxLength = max(maxLength, count)

    return maxLength


start = timer()
inputValue = [1,3,5,7]
outputValue = findLengthOfLCIS(inputValue)
end = timer()
print(end - start)
print("Output: ", outputValue)
