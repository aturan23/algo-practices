"""
Runtime: 88 ms
Memory Usage: 19.7 MB
"""
from timeit import default_timer as timer


def containsDuplicate(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    return not len(set(nums)) == len(nums)


start = timer()
inputValue = [1, 2, 1]
outputValue = containsDuplicate(inputValue)
end = timer()
print(end - start)
print("Output: ", outputValue)
