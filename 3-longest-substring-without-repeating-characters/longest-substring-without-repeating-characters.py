class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        currentCount = 0
        check = ''
        for i in range(len(s)):
            if s[i] not in check:
                check += s[i]
                currentCount += 1
            else:
                ans = max(currentCount, ans)
                index = check.index(s[i])
                check = check[index + 1:] + s[i]
                currentCount = len(check)
        ans = max(currentCount, ans)
        return ans
