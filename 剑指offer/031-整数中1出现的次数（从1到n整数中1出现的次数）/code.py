def NumberOf1Between1AndN_Solution(n):
    # write code here
    res = 0
    i = 1  # 个位开始
    while n // i != 0:
        high = n//(i*10) # 高位数
        current = (n//i) % 10  # 第i位数
        low = n - (n//i) * i  # 低位数
        if current == 0:
            res += high * i
        elif current == 1:
            res += high * i + low + 1
        else:
            res += (high+1) * i
        i *= 10
    return res

print(NumberOf1Between1AndN_Solution(20))

我的解法

class Solution:
    def NumberOf1Between1AndN_Solution(self, n):
        # 第一种，不考虑时间复杂度
        # count = 0
        # for i in range(1, n + 1):
        #     for j in str(i):
        #         if j == '1':
        #             count += 1
        # return count

        # 第二种，简化事件复杂度
        # 起始参数的设定，从第一个开始，之后每次往右移动1个，即*10
        precise = 1
        # 参数位左侧的可能数量
        highValue = 1
        # 位数，用作乘方运算
        count = 0
        # 最后的要返回的总数量
        sumNum = 0
        # 当参数位左侧不为0时循环
        while highValue != 0:
            # 取出高位
            highValue = n // (precise * 10)
            # 取出参数位（每循环一次变一下）
            midValue = (n // precise) % 10
            # 取出低位
            lowValue = n % precise
            # 每次都*10
            precise = precise * 10
            # 参数位分三种情况
            # 第一种，参数位等于0，若是该位想为1的话，只能进1，向左侧的可能性借1，右侧为10^count种可能性
            if midValue == 0:
                num = (highValue -1 +1) * pow(10, count)
            # 第二种，参数位大于1，就不用向左侧去借位，右侧为10^count种可能性
            elif midValue > 1:
                num = (highValue + 1) * pow(10, count)
            # 第三种，参数位就是1，有lowValue + 1个是需要进位的，其余不需要进位
            else:
                num = highValue * pow(10, count) + lowValue + 1
            # 每次循环都更新总数量的值
            sumNum += num
            # 更新count
            count += 1
        # 返回结果
        return sumNum
