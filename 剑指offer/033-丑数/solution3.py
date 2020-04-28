def GetUglyNumber_Solution(index):
    # write code here
    if index <= 1: return index
    res = [1] * index
    i2, i3, i5 = 0, 0, 0
    for i in range(1, index):
        res[i] = min(res[i2]*2, min(res[i3]*3, res[i5]*5))
        if res[i] == res[i2]*2: i2 += 1
        if res[i] == res[i3]*3: i3 += 1
        if res[i] == res[i5]*5: i5 += 1
    return res[-1]


print(GetUglyNumber_Solution(700))

我的解法
class Solution:
    def GetUglyNumber_Solution(self, index):
        # write code here
        if index <= 0:
            return 0
        # 2的指针
        twoPointer = 0
        # 3的指针
        threePointer = 0
        # 5的指针
        fivePointer = 0
        # 丑数列表
        uglyList = [1]
        # uglyList的计数
        count = 1
        # 当计数小于index，就一直循环
        while count < index:
            # 找到三者中的最小值
            minValue = min(uglyList[twoPointer] * 2,
                           uglyList[threePointer] * 3,
                           uglyList[fivePointer] * 5)
            # 添加进uglyList
            uglyList.append(minValue)
            # 若是当前uglyList的最后一个值等于uglyList[twoPointer]*2，就将2的指针往后移动一个
            if uglyList[-1] == uglyList[twoPointer] * 2:
                twoPointer += 1
            # 若是当前uglyList的最后一个值等于uglyList[twoPointer]*3，就将3的指针往后移动一个
            if uglyList[-1] == uglyList[threePointer] * 3:
                threePointer += 1
            # 若是当前uglyList的最后一个值等于uglyList[twoPointer]*5，就将5的指针往后移动一个
            if uglyList[-1] == uglyList[fivePointer] * 5:
                fivePointer += 1
            # count自增1
            count += 1
        # 最终返回丑数列表的最后一个值即为第index个丑数
        return uglyList[-1]
