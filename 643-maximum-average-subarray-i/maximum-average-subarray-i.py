class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        avg = float('-inf')
        currentsum = 0
        for i in range(len(nums)):
            currentsum += nums[i]
            if i >= k-1:
                avg = max(avg,currentsum/k)
                currentsum -= nums[i-k+1]
        return avg
        