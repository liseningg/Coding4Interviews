# -*- coding:utf-8 -*-
class Solution:
    def maxInWindows(self, num, size):
        # write code here
        if size == 0: return []
        queue = []
        res = []
        for i in range(len(num)):
            # 过期
            while queue and queue[0] <= i-size:
                queue.pop(0)
            # 挤走小数
            while queue and num[queue[-1]] < num[i]:
                queue.pop(-1)
            queue.append(i)
            if i < size - 1: 
                continue
            res.append(num[queue[0]])
        return res

做了等于没做版
# -*- coding:utf-8 -*-
class Solution:
    def maxInWindows(self, num, size):
        res, i = [], 0
        while size > 0 and i + size - 1 < len(num):
            res.append(max(num[i:i + size]))
            i += 1
        return res
