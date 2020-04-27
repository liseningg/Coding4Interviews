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
