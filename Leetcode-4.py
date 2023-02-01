class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):

        nums1.extend(nums2)　# merge them
        nums1.sort() #sort them

        if len(nums1) % 2 == 0: #mod = 0 whem it is even
            a = len(nums1)//2 #list[a] <-- a have to be int
            return (nums1[a]+nums1[a-1])/2  #index is from 0, not from 1
        else: #when it is odd
            a = len(nums1)//2
            return nums1[a]
