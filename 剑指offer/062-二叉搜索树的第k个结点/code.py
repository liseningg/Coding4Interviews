
class Solution:
    # 返回对应节点TreeNode
    
    def KthNode(self, pRoot, k):
        # write code here
        if not pRoot: return None
        stack = []
        while pRoot or stack:
            while pRoot:
                stack.append(pRoot)
                pRoot = pRoot.left
            pRoot = stack.pop()
            k -= 1
            if k == 0:
                return pRoot
            pRoot = pRoot.right
            
递归法
class Solution:
    # 返回对应节点TreeNode
    def KthNode(self, pRoot, k):
        # write code here
        res = []
        def preorder(pRoot):
            if not pRoot:
                return None
            preorder(pRoot.left)
            res.append(pRoot)
            preorder(pRoot.right)
        preorder(pRoot)
        if len(res) < k or k <1:
            return None
        return res[k-1]
