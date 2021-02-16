"""
Runtime: 44 ms
Memory Usage: 14.7 MB
"""
from timeit import default_timer as timer


def isAnagram(s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    slist = list(s)
    tlist = list(t)
    slist.sort()
    tlist.sort()
    return slist == tlist


start = timer()
inputValue1 = "anagram"
inputValue2 = "nagaram"
outputValue = isAnagram(inputValue1, inputValue2)
end = timer()
print(end - start)
print("Output: ", outputValue)
