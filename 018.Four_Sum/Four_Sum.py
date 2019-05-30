class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        targetList = []
        nums = sorted(nums)
        for n in range(0, len(nums)-3):
            if n == 0 or (n > 0 and nums[n] != nums[n-1]):
                for m in range(n+1, len(nums)-2):
                    if (m == n+1) or (m > n + 1 and nums[m] != nums[m-1]):
                        left = m+1
                        right = len(nums) - 1
                        sums = target - nums[m] - nums[n]
                        while(left < right):
                            if (nums[left] + nums[right] == sums):
                                targ = [nums[m],nums[n],nums[left],nums[right]]
                                if targ not in targetList:
                                    targetList.append(targ)
                                while(left<right and nums[left] == nums[left+1]):
                                    left += 1
                                while(left<right and nums[right]== nums[right-1]):
                                    right -= 1
                                left += 1
                                right -=1

                            elif (nums[left] + nums[right] < sums):
                                while(left < right and nums[left] == nums[left+1]):
                                    left += 1
                                left += 1
                            else:
                                while (left < right and nums[right] == nums[right -1]):
                                    right -= 1
                                right -= 1


        return targetList