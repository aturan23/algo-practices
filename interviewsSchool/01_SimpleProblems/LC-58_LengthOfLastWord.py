"""
Runtime: 24 ms
Memory Usage: 13.6 MB
"""

def lengthOfLastWord(s):
    arr = s.split()
    length = len(arr)
    return 0 if length == 0 else len(arr[-1])

print(lengthOfLastWord("Hello World"))