class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        # write code here
        map = {}
        res = []
        for n in array:
            map[n] = map.get(n, 0) + 1
        for n in array:
            if map[n] == 1:
                res.append(n)
        return res

我的解法
class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        if len(array) < 2:
            return None

        # 如果两个数相同，那么这两个数的异或操作就相同
        # 两个数异或的结果初始值
        twoNumXor = None
        # 循环array，找到两个数异或的最终结果
        for num in array:
            if twoNumXor == None:
                twoNumXor = num
            else:
                twoNumXor = twoNumXor ^ num
        # 找到这两个数是从第几位开始不一样的（找到第一个1）
        count = 0
        while twoNumXor % 2 == 0:
            twoNumXor //= 2
            count += 1
        # 设置mask为第一个1往后加count个0
        mask = 1 << count
        # 第一个出现一次的数
        firstNum = None
        # 第二次出现一次的数
        secondNum = None
        # 再次循环array
        for num in array:
            # 第一波数，其中会有第一个出现一次的数
            if mask & num == 0:
                if firstNum == None:
                    firstNum = num
                else:
                    firstNum = firstNum ^ num
            # 第二波数，其中会有第二个出现一次的数
            else:
                if secondNum == None:
                    secondNum = num
                else:
                    secondNum = secondNum ^ num
        # 返回这两个只出现一次的数
        return firstNum, secondNum

