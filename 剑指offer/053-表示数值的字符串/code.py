class Solution:
    # s字符串
    def isNumeric(self, s):
        # write code here
        sign, point, hasE = False, False, False
        for i in range(len(s)):
            if s[i].lower() == 'e':
                if hasE: return False
                if i == len(s)-1: return False
                hasE = True
            elif s[i] == '+' or s[i] == '-':
                if sign and s[i-1].lower() != 'e': return False
                if not sign and i > 0 and s[i-1].lower() != 'e': return False
                sign = True
            elif s[i] == '.':
                if hasE or point: return False
                point = True
            elif ord(s[i]) < ord('0') or ord(s[i]) > ord('9'):
                return False

            
            return True
我的解法
依次判断每种情况：
指数符号：'e','E'后面必须跟数字，且只能出现一次；
正负数符号：'+','-'只能出现在头部或者'e','E'后；
小数符号：只能出现一次；
每个字符是否在数字范围。
# -*- coding:utf-8 -*-
class Solution:
    # s字符串
    def isNumeric(self, s):
        # 分别记录符号位、小数点、e是否出现
        sign, decimal, has_e = False, False, False
        for i, v in enumerate(s):
            if v =='e' or v =='E':
                if i == len(s) - 1:     # e后面跟数字
                    return False
                if has_e:
                    return False
                has_e = True
            elif v == '+' or v == '-':  # 不在头部出现的符号必须在指数部分头部（e之后）
                if sign and s[i - 1] != 'e' and s[i - 1] != 'E':
                    return False
                if not sign and i != 0 and s[i - 1] != 'e' and s[i - 1] != 'E':
                    return False
                sign = True
            elif v == '.':
                if has_e or decimal:    # 指数部分不能有小数点，小数点不能出现两次
                    return False
                decimal = True
            elif v < '0' or v > '9':
                return False
        return True
题解二
正则表达式

import re
# -*- coding:utf-8 -*-
class Solution:
    # s字符串
    def isNumeric(self, s):
    	return re.match(r'^[+-]?[0-9]*(\.[0-9]+)?([eE][+-]?[0-9]+)?$', s)
    
