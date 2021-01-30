"""
Runtime: 28 ms
Memory Usage: 14.4 MB
"""
from timeit import default_timer as timer


def fizzBuzz(n):
    arr = []
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            arr.append("FizzBuzz")
        elif i % 3 == 0:
            arr.append("Fizz")
        elif i % 5 == 0:
            arr.append("Buzz")
        else:
            arr.append(str(i))
    return arr


start = timer()
inputValue = 15
outputValue = fizzBuzz(inputValue)
end = timer()
print(end - start)
print("Output: ", outputValue)