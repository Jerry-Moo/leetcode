# -*- coding:utf-8 -*-
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        count = len(candidates) # 数组数量
        sep = []  # 记录缓存数组的下标
        rList = [] # 记录 符合的数组列表
        st = 0 # 初始化统计下标
        candidates = sorted(candidates) 
        while True:
            if st < count and target >= candidates[st]:
                sep.append(st)
                target -= candidates[st]
            elif target == 0 :
                rList.append([candidates[n] for n in sep])
                st = sep.pop()
                target += candidates[st]
                st += 1
            elif st == count or candidates[st] > target:
                if len(sep) == 0:
                    break
                st = sep.pop()
                target += candidates[st]
                st += 1

        return rList
