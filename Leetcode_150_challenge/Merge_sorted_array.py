from typing import List

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        if n == 0 :return
        len1 = len(nums1)
        last_ind = len1-1
        while n > 0 and m > 0 :
            if nums2[n-1] >= nums1[m-1]:
                nums1[last_ind] = nums2[n-1]
                n-=1
            else:
                nums1[last_ind] = nums1[m-1]
                m-=1
            last_ind-=1
        while n > 0:
            nums1[last_ind] = nums2[n-1]
            n-=1
            last_ind-=1