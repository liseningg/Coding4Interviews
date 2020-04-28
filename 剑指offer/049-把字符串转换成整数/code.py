class Solution:
    def StrToInt(self, s):
        # write code here
        res = 0
        flag = 1
        for i in range(len(s)):
            if i == 0 and s[i] == '+':
                continue
            elif i == 0 and s[i] == '-':
                flag = -1
                continue
            n = ord(s[i]) - ord('0')
            if n>=0 and n<=9:
                res = 10 * res + n
            else:
                return False
        return res * flag

print(Solution().StrToInt('-1234'))
我的解法
class Solution:
    def StrToInt(self, s):
        # write code here
        numlist=['0','1','2','3','4','5','6','7','8','9','+','-']
        sum=0
        label=1#正负数标记
        if s=='':
            return 0
        for string in s:
            if string in numlist:#如果是合法字符
                if string=='+':
                    label=1
                    continue    #为什么要用continue
                if string=='-':
                    label=-1
                    continue
                else:
                    sum=sum*10+numlist.index(string)
            if string not in numlist:#非合法字符
                sum=0
                break#跳出循环
        return sum*label
