"""
Runtime: 24 ms
Memory Usage: 13.6 MB
"""
from timeit import default_timer as timer


def lengthOfLastWord(s):
    arr = s.split()
    length = len(arr)
    return 0 if length == 0 else len(arr[-1])


start = timer()
inputValue = "Hello World"
outputValue = lengthOfLastWord(inputValue)
end = timer()
print(end - start)
print("Output: ", outputValue)
