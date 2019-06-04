class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) == 0:
            return False
        elif len(nums) == 1:
            return False
        else:
            # [1,2,3,4,5]
            nums = sorted(nums)
            n = 0
            while n < len(nums) - 1:
                if nums[n] == nums[n+1]:
                    return True
                n += 1
            return False


        