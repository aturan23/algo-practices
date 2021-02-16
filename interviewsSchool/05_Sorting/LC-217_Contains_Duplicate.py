"""
Runtime: 44 ms
Memory Usage: 14.7 MB
"""
from timeit import default_timer as timer


def containsDuplicate(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    return len(set(nums)) != len(nums)


start = timer()
inputValue = [1, 2, 1]
outputValue = containsDuplicate(inputValue)
end = timer()
print(end - start)
print("Output: ", outputValue)
