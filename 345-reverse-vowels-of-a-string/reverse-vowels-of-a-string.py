class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = list(s)
        l = 0
        r = len(s) - 1
        vowel = ['a','e','i','o','u']
        while(l<r):
            if s[l].lower() not in vowel:
                l += 1
            elif s[r].lower() not in vowel:
                r -= 1
            else:
                s[l],s[r] = s[r],s[l]
                l += 1
                r -= 1
        return ''.join(s)
        