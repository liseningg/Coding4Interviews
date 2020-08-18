def FindGreatestSumOfSubArray(array):
    # write code here
    max = array[0]
    dp = [0] * (len(array) + 1)
    dp[0] = array[0]
    for i in range(1, len(array)):
        if dp[i-1] < 0:
            dp[i] = array[i]
        else:
            dp[i] = array[i] + dp[i-1]
        if dp[i] > max:
            max = dp[i]
    return max


print(FindGreatestSumOfSubArray([6,-3,-2,7,-15,1,2,2]))

我的解法
class Solution:
    def FindGreatestSumOfSubArray(self, array):
        maxNum = None
        tmpNum = 0
        for i in array:
            # 如果maxNum为空，就赋值为i
            if maxNum == None:
                maxNum = i
            # 如果tmpNum加上一个数还比这个数小，就把tmpNum重新赋值成这个数
            if tmpNum +i < i:
                tmpNum = i
            # 如果相加是不小于i的，就一直加下去
            else:
                tmpNum += i
            # 如果最大值小于加的值，就把最大值替换为这个值
            if maxNum < tmpNum:
                maxNum = tmpNum
        # 最终返回最大值
        return maxNum

# 递归
该题目思路:
dp[i]表示以元素array[i]结尾的最大连续子数组和.
以[-2,-3,4,-1,-2,1,5,-3]为例
可以发现,
dp[0] = -2
dp[1] = -3
dp[2] = 4
dp[3] = 3
以此类推,会发现
dp[i] = max{dp[i-1]+array[i],array[i]}.

# -*- coding:utf-8 -*-
class Solution:
    def FindGreatestSumOfSubArray(self, array):
        # write code here
        n = len(array)
        dp = [ i for i in array]
        for i in range(1,n):
            dp[i] = max(dp[i-1]+array[i],array[i])
         
        return max(dp)


 -*- coding:utf-8 -*-
class Solution:
    def FindGreatestSumOfSubArray(self, array):
        # write code here
        max_nums = [-1] * len(array)
        max_nums[0] = array[0]
        max_num = array[0]
        for i in range(1,len(array)):
            
            if max_num + array[i] > array[i]:
                max_nums[i] = max_num + array[i]
                max_num = max_num + array[i]
            else:
                max_nums[i] = array[i]
                max_num = array[i]
        return max(max_nums)
             
