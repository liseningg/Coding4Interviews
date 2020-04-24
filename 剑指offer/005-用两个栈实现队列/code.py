class CQueue(object):

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def appendTail(self, value):
        self.stack1.append(value)
    
    def deleteHead(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop(-1))
        if len(self.stack2) == 0: 
            return -1
        return self.stack2.pop(-1)

我的解法
class Solution:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
    def push(self, node):
        self.stack1.append(node)
        # write code here 
    def pop(self):
        if self.stack2 == []:
            while self.stack1:
                a = self.stack1.pop()
                self.stack2.append(a)
        return self.stack2.pop()
        # return xx
