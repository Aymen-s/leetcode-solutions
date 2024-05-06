class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        index = 0
        n = len(nums)
        for i in nums:
            if i != 0:
                nums[index] = i
                index += 1
        for i in range(index,n):
            nums[i] = 0
        