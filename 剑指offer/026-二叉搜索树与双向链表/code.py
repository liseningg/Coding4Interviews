# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def __init__(self):
        self.pre = None
        
    def Convert(self, root):
        # write code here
        if not root: return None
        self.helper(root)
        while root.left:
            root = root.left
        return root

    def helper(self, cur):
        if not cur: return None
        self.helper(cur.left)
        cur.left = self.pre
        if self.pre:
            self.pre.right = cur
        self.pre = cur
        self.helper(cur.right)
        

非递归版本
    def Convert(self, pRootOfTree):
        if not pRootOfTree:
            return None
         
        p = pRootOfTree
         
        stack = []
        resStack = []
         
        while p or stack:
            if p:
                stack.append(p)
                p = p.left
            else:
                node = stack.pop()
                resStack.append(node)
                p = node.right
             
        resP = resStack[0]
        while resStack:
            top = resStack.pop(0)
            if resStack:
                top.right = resStack[0]
                resStack[0].left = top
         
        return resP
    
递归版本
    def Convert(self, root):
        if not root:
            return None
        if not root.left and not root.right:
            return root
         
        # 将左子树构建成双链表，返回链表头
        left = self.Convert(root.left)
        p = left
         
        # 定位至左子树的最右的一个结点
        while p and p.right:       #p是为了防止p本身为空,p最后走到的是None   p.right是p刚好走到最后一个结点
            p = p.right
         
        # 如果左子树不为空，将当前root加到左子树链表
        if left:
            p.right = root
            root.left = p
         
        # 将右子树构造成双链表，返回链表头
        right = self.Convert(root.right)
        # 如果右子树不为空，将该链表追加到root结点之后
        if right:
            right.left = root
            root.right = right
             
        return left if left else root
