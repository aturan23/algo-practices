"""
Runtime: 168 ms
Memory Usage: 15.6 MB
"""
from timeit import default_timer as timer


def merge(nums1, m, nums2, n):
    """
    :type nums1: List[int]
    :type m: int
    :type nums2: List[int]
    :type n: int
    :rtype: None Do not return anything, modify nums1 in-place instead.
    """
    l = m + n - 1
    while m > 0 and n > 0:
        if nums2[n - 1] >= nums1[m - 1] and nums2[n - 1] >= nums1[l]:
            nums1[l] = nums2[n - 1]
            l -= 1
            m -= 1
            n -= 1


start = timer()
nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
outputValue = merge(nums1, m, nums2, n)
end = timer()
print(end - start)
print("Output: ", outputValue)
