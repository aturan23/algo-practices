"""
Runtime: 28 ms
Memory Usage: 13.8 MB
"""
from timeit import default_timer as timer

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next


# start = timer()
# inputValue = [1,2,3,0,0,0]
# outputValue = merge(inputValue)
# end = timer()
# print(end - start)
# print("Output: ", outputValue)
