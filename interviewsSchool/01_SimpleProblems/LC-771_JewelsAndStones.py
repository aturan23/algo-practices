"""
Runtime: 24 ms
Memory Usage: 13.4 MB
"""


def numJewelsInStones(jewels, stones):
    """
    :type jewels: str
    :type stones: str
    :rtype: int
    """
    jewelList = list(jewels)
    stoneList = list(stones)

    number = 0

    for i in jewelList:
        number += stoneList.count(i)

    return number

print(numJewelsInStones("aA", "aAAbbbb"))
