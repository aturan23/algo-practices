"""
Runtime: 44 ms
Memory Usage: 14.2 MB
"""
from timeit import default_timer as timer


def findKthLargest(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """
    return sorted(nums)[-k]


start = timer()
inputValue = [3,2,1,5,6,4]
outputValue = findKthLargest(inputValue, 2)
end = timer()
print(end - start)
print("Output: ", outputValue)
