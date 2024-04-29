class Solution:
    def isPalindrome(self, x: int) -> bool:
        n = 0
        o = x
        while x > 0:
            m = x % 10
            n = n * 10 + m
            x //= 10
        return o == n
        