class MinStack(object):

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, node):
        # write code here
        self.stack.append(node)
        if not self.min_stack:
            self.min_stack.append(node)
        else:
            if self.min_stack[-1] < node:
                self.min_stack.append(self.min_stack[-1])
            else:
                self.min_stack.append(node)
    def pop(self):
        # write code here
        self.stack.pop(-1)
        self.min_stack.pop(-1)
    
    def top(self):
        # write code here
        if self.stack:
            return self.stack[-1]
        else:
            return []

    def min(self):
        # write code here
        return self.min_stack[-1]
    
我的解法        
class Solution:
    def __init__(self):
        self.item = []
        self.assist = []
    def push(self, node):
        min = self.min()
        if node < min or not min:  #刚开始执行push的时候min是没有值的，如果不加or not min条件的话if语句不成立，则不能入栈assist
            self.assist.append(node)
        else:
            self.assist.append(min)
        # write code here
        self.item.append(node) 
    def pop(self):
        if self.item != []:
            self.assist.pop()
            return self.item.pop()
        # write code here
    def top(self):
        # write code here
        if self.item != []:
            return self.item[len(self.item) - 1]
    def min(self):
        if self.item:
            return self.assist[-1]
