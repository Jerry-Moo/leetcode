class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        threeSumList = []
        for n in range(0,len(nums)-2):
            if n == 0 or ( nums[n] != nums[n-1]):
                left = n + 1
                right = len(nums) -1
                while (left < right):
                    if (nums[left] + nums[right] == -nums[n]):
                        tar = [nums[n],nums[left],nums[right]]
                        threeSumList.append(tar)
                        while (left < right and nums[left] == nums[left+1]):
                            left += 1
                        while (left < right and nums[right] == nums[right-1]):
                            right -= 1
                        left += 1
                        right -=1

                    elif (nums[left] + nums[right] < -nums[n]):
                        while(left < right and nums[left] == nums[left+1]):
                            left += 1
                        left += 1
                    else:
                        while(left < right and nums[right] == nums[right-1]):
                            right -= 1
                        right -= 1
        return threeSumList
