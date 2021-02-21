"""
Runtime: 20 ms
Memory Usage: 14 MB
"""
from timeit import default_timer as timer


def decompressRLElist(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    arr = []
    temp = []
    tempNum = 0
    for index in range(len(nums)):
        i = index + 1
        if i % 2 != 0:
            tempNum = nums[index]
        elif i % 2 == 0:
            temp.append(nums[index])
            arr += temp * tempNum
            temp = []
            tempNum = 0

    return arr


start = timer()
inputValue = [1,2,3,4]
outputValue = decompressRLElist(inputValue)
end = timer()
print(end - start)
print("Output: ", outputValue)
