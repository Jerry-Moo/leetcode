class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        rint = 0
        start = False
        while True:
            if len(s) == 0:
                return rint
            elif not start:
                if s[-rint-1] == " ":
                    s = s[0:-1]
                else:
                    start = True
            elif start and rint < len(s) and s[-rint-1] != " ":
                rint += 1
            else:
                return rint        

