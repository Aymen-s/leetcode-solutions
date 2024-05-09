class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res = []    
        if len(s) < len(p): return res 
        pArray, sArray = [0] * 26, [0] * 26
        for c in p:
            pArray[ord(c)-ord('a')] += 1
        init = s[:len(p)]
        for c in init:
            sArray[ord(c)-ord('a')] += 1

        for i in range(len(s)-len(p)+1):
            if pArray == sArray: res.append(i)
            sArray[ord(s[i])-ord('a')] -= 1
            if i < len(s)-len(p):
                sArray[ord(s[i+len(p)])-ord('a')] += 1 
  
        return res    


        