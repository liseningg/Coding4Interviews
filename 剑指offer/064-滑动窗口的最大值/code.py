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
    
双向队列：queue存入num中元素的下标，时间复杂度O(n)。

# -*- coding:utf-8 -*-
class Solution:
    def maxInWindows(self, num, size):
        queue,res,i = [],[],0
        while size > 0 and i < len(num):
            if len(queue) > 0 and i-size+1 > queue[0]:      #若最大值queue[0]不在当前滑窗内，则弹出
                queue.pop(0)
            while len(queue) > 0 and num[queue[-1]] < num[i]: #每次弹出所有比num[i]小的数字，保证队首为当前窗口最大值
                queue.pop()
            queue.append(i)		# 把每次滑动的num下标加入队列
 
            # 每滑动到一个窗口末尾保存这个窗口中的最大值
            if i >= size-1:
                res.append(num[queue[0]])
            i += 1
        return res
