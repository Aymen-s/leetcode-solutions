class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        l = 0
        r = 0
        ans = []
        
        while l < len(word1) and r < len(word2):
            if word1[l] > word2[r]:
                ans.append(word1[l])
                l += 1
            elif word1[l] < word2[r]:
                ans.append(word2[r])
                r += 1
            else:
                if word1[l+1:] >= word2[r+1:]:
                    ans.append(word1[l])
                    l += 1
                else:
                    ans.append(word2[r])
                    r += 1
        return "".join(ans) + word1[l:] + word2[r:]