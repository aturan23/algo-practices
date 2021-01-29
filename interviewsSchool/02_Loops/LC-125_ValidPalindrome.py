"""
Runtime: 32 ms
Memory Usage: 15.5 MB
"""


def isPalindrome(s):
    """
    :type s: str
    :rtype: bool
    """
    import re
    s = re.sub(r'[\W_]', '', s).lower()
    left = 0
    right = len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1

    return True


inputValue = "A man, a plan, a canal: Panama"
outputValue = isPalindrome(inputValue)

print("Output: ", outputValue)
