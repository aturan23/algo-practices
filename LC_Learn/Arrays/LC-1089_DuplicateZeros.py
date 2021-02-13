"""
Runtime: 56 ms
Memory Usage: 13.7 MB
"""
from timeit import default_timer as timer


def duplicateZeros(arr):
    """
    :type arr: List[int]
    :rtype: None Do not return anything, modify arr in-place instead.
    """
    i = 0
    while i < len(arr):
        if arr[i] == 0:
            arr.insert(i + 1, 0)
            i += 1
            del arr[-1]
        i += 1

start = timer()
inputValue = [1,0,2,3,0,4,5,0]
outputValue = duplicateZeros(inputValue)
end = timer()
print(end - start)
print("Output: ", outputValue)
