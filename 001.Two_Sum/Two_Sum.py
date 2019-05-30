# -*- utf-8 -*-
# 给定一个整数数组和一个目标值，找出数组中和为目标值的两个数。

# 你可以假设每个输入只对应一种答案，且同样的元素不能被重复利用。
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(0,len(nums)):
            for j in range(0, len(nums)):
                if i != j:
                    if (nums[i] + nums[j] == target):
                        return [i,j]