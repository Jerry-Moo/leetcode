# -*- coding:utf-8 -*-
# 给定一个 32 位有符号整数，将整数中的数字进行反转。
# 假设我们的环境只能存储 32 位有符号整数，其数值范围是 [−231,  231 − 1]。根据这个假设，如果反转后的整数溢出，则返回 0。

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        y = ''
        for i in range(0,len(str(abs(x)))):
            y = y + str(abs(x))[-1-i]
        if x > 0:
            if int(y) <= (2**31 -1) and int(y) >= -(2**31):
                return int(y)
            else:
                return 0
        else:
            if int(y) <= (2**31 -1) and int(y) >= -(2**31):
                return 0-int(y)
            else:
                return 0