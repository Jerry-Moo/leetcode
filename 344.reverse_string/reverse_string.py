class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        if len(s) <= 1:
            return s
        else:
            for n in range(0,len(s)/2):
                s[n], s[len(s)-n-1] = s[len(s)-n-1], s[n]
        