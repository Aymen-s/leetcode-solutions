class Solution(object):
    def dividePlayers(self, skill):
        """
        :type skill: List[int]
        :rtype: int
        """
        l = 0
        r = len(skill)-1
        sum = 0
        skill.sort()
        ans = []
        ans1 = []
        tot = 0
        if len(skill) == 2:
            return skill[l]*skill[r]
        else:
            while l<=r:
                ans += [skill[l],skill[r]]
                tot += (skill[l]*skill[r])
                l += 1
                r -= 1
        i = 0
        while i < len(ans):
            ans1.append(ans[i]+ans[i+1])
            i += 2
        if len(set(ans1)) == 1: 
            return tot
        return -1
        
                
            