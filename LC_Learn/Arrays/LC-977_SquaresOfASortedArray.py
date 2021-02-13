"""
Runtime: 168 ms
Memory Usage: 15.6 MB
"""
from timeit import default_timer as timer


def sortedSquares(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    squares = []
    for num in nums:
        squares.append(num * num)

    squares.sort()
    return squares


start = timer()
inputValue = [-4,-1,0,3,10]
outputValue = sortedSquares(inputValue)
end = timer()
print(end - start)
print("Output: ", outputValue)
