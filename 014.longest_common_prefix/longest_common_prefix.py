class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        strings = ""
        temp = ""
        count = len(strs) #3
        sep = 0
        cnt = 0
        if count == 0:
            return strings
        elif count == 1:
            strings = ''+ strs[0] +''
            return strings
        else:
            while True:
                if cnt < count-1:
                    if len(strs[cnt]) > 0 and len(strs[cnt+1]) > 0 and len(strs[cnt]) > sep and len(strs[cnt+1]) > sep:
                        if strs[cnt][sep] == strs[cnt+1][sep]:
                            temp = strs[cnt][sep]
                            cnt += 1
                        else:
                            break
                    else:
                        break
                elif cnt == count-1:
                    strings += temp
                    cnt = 0
                    temp = ""
                    sep +=1
            return strings
