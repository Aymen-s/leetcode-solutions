class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        i = 1
        while True:
            if (i*n) % 2 == 0:
                return i*n
            i += 1
            
        