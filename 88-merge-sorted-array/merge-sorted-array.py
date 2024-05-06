class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = len(nums1) - 1
        while i>=m:
            nums1.pop(i)
            i -= 1
        nums1 += nums2
        nums1.sort()
        return nums1
        