class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def isEqual(p1, p2):
    if not p1 and not p2:
        return True
    elif p1 and p2 and p1.val == p2.val:
        return True
    else:
        return False

class Solution:
    def isSymmetrical(self, pRoot):
        # write code here
        if not pRoot: return True
        queue = [pRoot]
        while queue:
            n = len(queue)
            if queue[0] != pRoot and n % 2 != 0: 
                return False
            for i in range(n//2):
                if not isEqual(queue[i], queue[-1-i]):
                    return False
            for _ in range(n):
                node = queue.pop(0)
                if not node: continue
                queue.append(node.left)
                queue.append(node.right)
        return True
    
我的解法
class Solution:
    def isSymmetrical(self, pRoot):
        # 定义判断是否镜像的函数
        def isMirror(left, right):
            # 如果两侧都为空，则是镜像的了
            if left == None and right == None:
                return True
            # 若有一侧不为空，则不是镜像的
            elif left == None or right == None:
                return False
            # 如果左侧的值不等于右侧额值，就不是镜像的
            if left.val != right.val:
                return False
            # 递归判断左侧的左侧和右侧的右侧
            ret1 = isMirror(left.left, right.right)
            # 递归判断左侧的右侧和右侧的左侧
            ret2 = isMirror(left.right, right.left)
            # 返回这两个返回值的与
            return ret1 and ret2
        # 如果此二叉树为空，则其也是对称的
        if pRoot == None:
            return True
        # 返回判断此二叉树的左侧和右侧
        return isMirror(pRoot.left, pRoot.right)
