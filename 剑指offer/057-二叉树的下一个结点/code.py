class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

class Solution:
    def GetNext(self, pNode):
        # write code here
        if not pNode: return None
        p = pNode
        if pNode.right:  # 有右子树
            p = pNode.right
            while p.left:
                p = p.left
            return p
         # 没有右子树但是有父亲节点
        while pNode.next and pNode.next.right == pNode:
            pNode = pNode.next
        return pNode.next
    
我的解法：
1.
class Solution:
    def GetNext(self, pNode):
        # write code here
        if pNode.right:#有右子树
            p=pNode.right
            while p.left:
                p=p.left
            return p
        while pNode.next:#无右子树，则找第一个当前节点是父节点左孩子的节点
            if(pNode.next.left==pNode):
                return pNode.next
            pNode = pNode.next#沿着父节点向上遍历
        return  #到了根节点仍没找到，则返回空
    
2.
class Solution:
    def GetNext(self, pNode):
        # 1.寻找右子树，如果存在就一直找到右子树的最左边，就是下一个节点
        # 2.没有右子树，就寻找他的父节点，一直找到它是父节点的左子树，打印父节点
        if pNode.right:
            tmpNode = pNode.right
            while tmpNode.left:
                tmpNode = tmpNode.left
            return tmpNode
        else:
            tmpNode = pNode
            while tmpNode.next:
                if tmpNode.next.left == tmpNode:
                    return tmpNode.next
                tmpNode = tmpNode.next
            return None
