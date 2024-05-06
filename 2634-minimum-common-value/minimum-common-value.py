class Solution(object):
    def getCommon(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        set_nums1 = set(nums1) 
        
        for num in nums2:
            if num in set_nums1:
                return num
        
        return -1 
    