"""
Runtime: 24 ms
Memory Usage: 13.5 MB
"""
from timeit import default_timer as timer


def runningSum(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    temp = 0
    arr = []
    for num in nums:
        temp += num
        arr.append(temp)

    return arr


start = timer()
inputValue = [1, 2, 3, 4, 5]
outputValue = runningSum(inputValue)
end = timer()
print(end - start)
print("Output: ", outputValue)
