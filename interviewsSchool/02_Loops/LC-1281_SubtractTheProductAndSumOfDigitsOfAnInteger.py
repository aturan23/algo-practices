"""
Runtime: 20 ms
Memory Usage: 13.4 MB
"""
from timeit import default_timer as timer


def subtractProductAndSum(n):
    """
    :type n: int
    :rtype: int
    """
    arr = list(map(int, str(n)))

    multiply = 1
    summary = 0
    for i in arr:
        multiply *= i
        summary += i

    return multiply - summary


start = timer()
inputValue = 234
outputValue = subtractProductAndSum(inputValue)
end = timer()
print(end - start)
print("Output: ", outputValue)
