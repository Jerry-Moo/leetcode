class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        strings = "1"
        for count in range(0,n-1):
            sub = 0
            temp = ""
            while sub < len(strings):
                cnt = 1
                while sub < len(strings) - 1 and strings[sub] == strings[sub+1]:
                    cnt += 1
                    sub += 1
                temp = temp + str(cnt) + strings[sub]
                sub += 1
            strings = temp
        return strings
        

test = Solution()
test.countAndSay(5)