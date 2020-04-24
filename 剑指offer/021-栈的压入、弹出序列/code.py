def IsPopOrder(pushV, popV):
    # write code here
    stack = []
    i = 0
    for v in pushV:
        stack.append(v)
        while stack and stack[-1] == popV[i]:
            i += 1
            stack.pop(-1)
    if not stack:
        return True
    else:
        return False
    

print(IsPopOrder([1, 2, 3, 4, 5], [4,3,5,1,2]))

我的解法：
class Solution:
    def IsPopOrder(self, pushV, popV):
        # write code here
        if len(pushV) != len(popV) or not pushV:
            return False
        stack = []
        for i in pushV:
            stack.append(i)
            while len(stack) and stack[-1] == popV[0]: 
#len(stack)表示对stack剩下的值与popV进行比较，当len（stack）=0时，while停止循环
                stack.pop()
                popV.pop(0)
        if stack:
            return False
        return True
