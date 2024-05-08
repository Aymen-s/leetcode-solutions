class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        ans = ''
        n = 0
        for i in range(len(s)):
            if n < len(spaces) and i == spaces[n]:
                ans += " "
                n += 1
            ans += s[i] 
        return ans

            
        