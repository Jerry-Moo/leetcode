# -*- coding:utf-8 -*-
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # [a，b，c，d，e]
        # 从左乘一遍得到[1, a, ab, abc, abcd]
        # 从右乘一遍得到[bcde,acde,abde,abce,abcd]
        res = [1]
        temp = nums[0]
        for n in range(1, len(nums)):
            res.append(temp)
            temp *= nums[n]
        temp = nums[-1]
        print (res)
        for n in range(len(nums)-2,-1,-1):
            res[n] = res[n] * temp
            temp *=  nums[n]

        return res
        