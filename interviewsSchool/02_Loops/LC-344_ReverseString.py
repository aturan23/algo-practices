"""
Runtime: 184 ms
Memory Usage: 21.1 MB
"""
from timeit import default_timer as timer


def reverseString(s):
    """
    :type s: List[str]
    :rtype: None Do not return anything, modify s in-place instead.
    """
    l = 0
    r = len(s) - 1
    while l < r:
        temp = s[l]
        s[l] = s[r]
        s[r] = temp
        l += 1
        r -= 1

    return s


start = timer()
inputValue = ["h","e","l","l","o"]
outputValue = reverseString(inputValue)
end = timer()
print(end - start)
print("Output: ", outputValue)
