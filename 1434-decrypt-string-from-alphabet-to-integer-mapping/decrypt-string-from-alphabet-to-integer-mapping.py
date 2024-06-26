class Solution(object):
    def freqAlphabets(self, s):
        """
        :type s: str
        :rtype: str
        """
        i = 0
        ans = ''
        d = {
            '1': 'a', '2': 'b', '3': 'c', '4': 'd', '5': 'e',
            '6': 'f', '7': 'g', '8': 'h', '9': 'i', '10#': 'j',
            '11#': 'k', '12#': 'l', '13#': 'm', '14#': 'n',
            '15#': 'o', '16#': 'p', '17#': 'q', '18#': 'r',
            '19#': 's', '20#': 't', '21#': 'u', '22#': 'v',
            '23#': 'w', '24#': 'x', '25#': 'y', '26#': 'z'
        }
        while i < len(s):
            if i+2 < len(s) and s[i+2] == "#":
                ans += d[s[i:i+3]]
                i += 3
            else:
                ans += d[s[i]]
                i += 1
        return ans