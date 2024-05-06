class Solution(object):
    def interpret(self, command):
        """
        :type command: str
        :rtype: str
        """
        ans = command.replace("()","o")
        ans = ans.replace("(al)","al")
        return ans
        