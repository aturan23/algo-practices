"""
Runtime: 32 ms
Memory Usage: 15.5 MB
"""
from timeit import default_timer as timer


def increasingTriplet(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    uniqueSet = set(nums)
    arr = list(uniqueSet)
    length = len(arr)
    exists = False
    for i in range(length):
        for j in range(i + 1, length):
            for k in range(j + 1, length):
                if arr[i] < arr[j] < arr[k]:
                    exists = True

    return exists


start = timer()
inputValue = [5,4,3,2,1]
outputValue = increasingTriplet(inputValue)
end = timer()
print(end - start)
print("Output: ", outputValue)
