import time
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 动态规划 求解
        if n == 1:
            return 1
        elif n == 2:
            return 2
        else:
            res = 0
            i, j = 1, 2
            k = 3
            while (k <= n):
                res = i + j 
                i = j
                j = res
                k += 1
        return res
