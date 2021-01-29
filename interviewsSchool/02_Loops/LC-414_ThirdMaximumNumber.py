"""
Runtime: 56 ms
Memory Usage: 14.6 MB
"""


def thirdMax(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    uniqset = set(nums)
    arr = list(uniqset)
    if len(arr) == 1: return arr[0]
    if len(arr) == 2:
        return arr[0] if arr[0] > arr[1] else arr[1]

    firstMax = max([arr[0], arr[1]])
    secondMax = min([arr[0], arr[1]])

    for i in arr:
        if i > firstMax:
            secondMax = firstMax
            firstMax = i
        elif i > secondMax:
            secondMax = i

    arr.remove(firstMax)
    arr.remove(secondMax)

    maximum = arr[0]
    for i in arr:
        if i > maximum:
            maximum = i

    return maximum


print(thirdMax([3, 2, 1, 3, 54, 10]))
