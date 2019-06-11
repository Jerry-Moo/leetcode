class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) == 0 or len(s) == 1:
            return s
        else:
            rs = ''
            sep = 0
            temp = ''
            while sep < len(s):
                if s[sep] == ' ':
                    if temp == '':
                        rs += ' '
                    else:
                        temp = list(temp)
                        for i in range(0,len(temp)/2):
                            temp[i], temp[len(temp)-i-1] = temp[len(temp)-i-1], temp[i]
                        rs += ''.join(list(temp))
                        rs += ' '
                        temp = ''
                else:
                    temp += s[sep]
                sep += 1
                if sep == len(s) and temp != '':
                    temp = list(temp)
                    for i in range(0,len(temp)/2):
                        temp[i], temp[len(temp)-i-1] = temp[len(temp)-i-1], temp[i]
                    rs += ''.join(list(temp))
        return rs
