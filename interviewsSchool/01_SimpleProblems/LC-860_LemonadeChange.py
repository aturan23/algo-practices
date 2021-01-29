"""
Runtime: 24 ms
Memory Usage: 13.4 MB
"""
from timeit import default_timer as timer

def lemonadeChange(bills):
    """
    :type bills: List[int]
    :rtype: bool
    """
    if bills.count(5) == 0:
        return False

    tempBills = []

    while 5 in bills:
        tempBills.append(5)
        bills.remove(5)

    if bills.count(10) > len(tempBills):
        return False

    while 10 in bills:
        bills.remove(10)
        tempBills.remove(5)
        tempBills.append(10)

    while 20 in bills:
        change = 0
        if 10 in tempBills and 5 in tempBills:
            change += 15
            tempBills.remove(5)
            tempBills.remove(10)
        else:
            if tempBills.count(5) == 3:
                change += 15
                tempBills.remove(5)
                tempBills.remove(5)
                tempBills.remove(5)
        if change == 15:
            tempBills.append(20)
            bills.remove(20)

    return len(bills) == 0


start = timer()
result = lemonadeChange([5,5,5,10,20])
end = timer()
print(end - start)
print(result)
