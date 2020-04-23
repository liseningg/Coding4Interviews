class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def TreeDepth(self, pRoot):
        # write code here
        if not pRoot: return 0
        queue = [pRoot]
        deep = 0
        while queue:
            # 记录同层节点的个数
            n = len(queue)
            for _ in range(n):
                # 将同层节点依次出队
                node = queue.pop(0)
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            deep += 1
        return deep
                
递归方法

class Solution:
    def TreeDepth(self, pRoot):
        # write code here
        # 使用层次遍历
        # 当树为空直接返回0
        if pRoot is None:
            return 0
        # 方法2：使用递归
        # 如果该树只有一个结点，它的深度为1.如果根节点只有左子树没有右子树，
        # 那么树的深度为左子树的深度加1；同样，如果只有右子树没有左子树，
        # 那么树的深度为右子树的深度加1。如果既有左子树也有右子树，
        # 那该树的深度就是左子树和右子树的最大值加1.
        count = max(self.TreeDepth(pRoot.left), self.TreeDepth(pRoot.right)) + 1
        return count
