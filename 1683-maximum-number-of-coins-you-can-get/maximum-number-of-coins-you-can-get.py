class Solution(object):
    def maxCoins(self, piles):
        """
        :type piles: List[int]
        :rtype: int
        """
        piles.sort()
        l = 0
        r = len(piles) - 1
        sum = 0
        while l < r:
            l += 1
            r -= 1
            sum += piles[r]
            r -= 1
        return sum
            
        