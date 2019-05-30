# -*- utf-8 -*-
# 判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
     
        for i in range(0,len(str(x))/2):
            if str(x)[i] != str(x)[len(str(x))-i-1]:
                return False
        return True