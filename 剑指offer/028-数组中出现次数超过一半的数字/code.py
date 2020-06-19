def MoreThanHalfNum_Solution(numbers):
    # write code here
    res = None
    cnt = 0
    for i in numbers:  # 留下数组中出现次数最高的数
        if not res:
            res = i
            cnt = 1
        else:
            if i == res:
                cnt += 1
            else:
                cnt -= 1
                if cnt == 0:
                    res = None
    # 判断次数是否大于一半
    cnt = 0 
    for i in numbers:
        if i == res:
            cnt += 1
    if cnt > len(numbers) / 2:
        return res
    else:
        return 0

print(MoreThanHalfNum_Solution([1,2,3,2,2,2,5,4,2]))

我的解法
1        # 时间复杂度O(n), 空间复杂度O(n)
class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        if not numbers:
            return 0
        d=dict()
        c = numbers
        for i in c:    
            d[i]=d.get(i,0)+1
        #第二次遍历字符串，检查每个字符出现的次数
        for i in c:
            if d[i] > len(c) //2 :   #O(1)
                return i
        return 0
    
2       # 想要空间复杂度为O(1)，时间复杂度O(n)
        # 思路：遇到不相同的数据就相互抵消掉，最终剩下的数字就可能是大于一半的数字
def MoreThanHalfNum_Solution(self, numbers):
       numLen = len(numbers)
        last = 0
        lastCount = 0

        for num in numbers:
            if lastCount == 0:
                last = num
                lastCount = 1
            else:
                if num == last:
                    lastCount += 1
                else:
                    lastCount -= 1
        if lastCount == 0:
            return 0
        else:
            # 这种情况是last可能是大于一半的数字
            lastCount = 0
            for num in numbers:
                if num == last:
                    lastCount += 1
            if lastCount > (numLen >> 1):
                return last
        return 0
 

note：

python的sorted函数使用Timesort算法进行排序，平均时间复杂度为O(n*logn)
出现次数大于数组长度一半的元素，在排序后的数组中间位置
方法： 找出排序后在数组中间位置地元素并计算其出现次数，若次数超过数组长度地一半则返回它，否则返回0.

# -*- coding:utf-8 -*-\
class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        # 出现次数大于数组长度一半的元素，在排序后的数组中间位置
        n = len(numbers)
        mostElement = sorted(numbers)[n//2]
        cnt = numbers.count(mostElement)
        return mostElement if cnt > n//2 else 0
