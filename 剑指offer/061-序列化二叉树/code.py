# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.index = -1

    def Serialize(self, root):
        # write code here
        if root:
            return str(root.val) + ' ' +\
                self.Serialize(root.left) + \
                self.Serialize(root.right)
        else:
            return '# '

    def Deserialize(self, s):
        # write code here
        l = s.split()
        self.index += 1
        if self.index >= len(s): 
            return None
        
        if l[self.index] != '#':
            root = TreeNode(int(l[self.index]))
            root.left = self.Deserialize(s)
            root.right = self.Deserialize(s)
        else:
            return None
        return root


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
# root.left.left = TreeNode(4)
root.left.right = TreeNode(5)


print(Solution().Serialize(root))



我的解法
class Solution:
    # 序列化
    def Serialize(self, root):
        retList = []
        def preOrder(root):
            if root == None:
                retList.append('#')
                return
            retList.append(str(root.val))
            preOrder(root.left)
            preOrder(root.right)

        preOrder(root)
        return ' '.join(retList)

    # 反序列化
    def Deserialize(self, s):
        retList = s.split()
        def dePreOrder():
            if retList == []:
                return None
            rootVal = retList.pop(0)
            if rootVal == '#':
                return None
            node = TreeNode(int(rootVal))
            leftNode = dePreOrder()
            rightNode = dePreOrder()
            node.left = leftNode
            node.right = rightNode
            return node

        pRoot = dePreOrder()
        return pRoot
