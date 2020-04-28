def sum(n):
    try:
        1 % n
        return n + sum(n-1)
    except:
        return 0


class Solution:
    def Sum_Solution(self, n):
        return sum(n)


print(Solution().Sum_Solution(10))

我的解法
不能用乘除法、循环和条件判断语句，就用位运算代替乘除法，用递归代替循环，用短路替代条件判断（不过此题用不上乘除法）。

从n开始往回加；
使用ans and，与运算的短路原理，若ans为0了就跳出递归；
使用递归代替循环做加法。
# -*- coding:utf-8 -*-
class Solution:
    def Sum_Solution(self, n):
        ans = n
        tmp = ans and self.Sum_Solution(n - 1)
        ans += tmp
        return ans
