from ctypes import *
def NumberOf1(n):
    # write code here
    cnt = 0
    while c_int(n).value:
        n = n & (n-1)
        cnt += 1
        print(c_int(n), n)
    return cnt

print(NumberOf1(-3))




# # -*- coding:utf-8 -*-
# class Solution:
#     def NumberOf1(self, n):
#         # write code here
#         return bin(n).replace("0b","").count("1") if n>=0 else bin(2**32+n).replace("0b","").count("1")



class Solution:
    def NumberOf1(self, n):
        # write code here
        count = 0
        if n < 0:
            n = n & 0xffffffff     #对于负数，最高位为1，而负数在计算机是以补码存在的，往右移，符号位不变，符号位1往右移，最终可能会出现全1的情况，导致死循环。与0xffffffff相与，就可以消除负数的影响
        while n: 
            count += 1
            n = (n - 1) & n
        return count
