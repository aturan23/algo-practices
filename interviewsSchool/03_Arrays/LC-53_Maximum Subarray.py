"""
Runtime: 40 ms
Memory Usage: 14.3 MB
"""
from timeit import default_timer as timer


def maxSubArray(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    maxSub, curSum = nums[0], 0

    for n in nums:
        if curSum < 0:
            curSum = 0
        curSum += n
        maxSub = max(maxSub, curSum)
    return maxSub


start = timer()
inputValue = [-2,1,-3,4,-1,2,1,-5,4]
outputValue = maxSubArray(inputValue)
end = timer()
print(end - start)
print("Output: ", outputValue)
