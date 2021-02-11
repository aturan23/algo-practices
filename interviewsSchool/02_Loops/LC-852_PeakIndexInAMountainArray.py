"""
Runtime: 52 ms
Memory Usage: 14.8 MB
"""
from timeit import default_timer as timer


def peakIndexInMountainArray(arr):
    """
    :type arr: List[int]
    :rtype: int
    """
    maxNumIndex = 0
    for i in range(len(arr)):
        if arr[i] > arr[maxNumIndex]:
            maxNumIndex = i

    return maxNumIndex


start = timer()
inputValue = [0, 1, 0]
outputValue = peakIndexInMountainArray(inputValue)
end = timer()
print(end - start)
print("Output: ", outputValue)
