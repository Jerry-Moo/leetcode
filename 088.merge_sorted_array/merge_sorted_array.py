class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        for sep in range(0,n):
            nums1.pop()
        cnt = 0
        temp = 0
        while True:
            if len(nums2) == 0 or m == 0:
                for num in range(0,len(nums2)):
                    nums1.append(nums2[num])
                break
            elif nums2[temp] <= nums1[cnt]:
                nums1.insert(cnt,nums2[temp])
                nums2.pop(temp)
            elif nums2[temp] > nums1[cnt]:
                if cnt < len(nums1)-1:
                    cnt += 1
                else:
                    nums1.append(nums2[temp])
                    nums2.pop(temp)
        