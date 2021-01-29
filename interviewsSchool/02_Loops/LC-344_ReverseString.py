"""
Runtime: 184 ms
Memory Usage: 21.1 MB
"""


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


inputValue = ["h","e","l","l","o"]
outputValue = reverseString(inputValue)

print("Output: ", outputValue)
