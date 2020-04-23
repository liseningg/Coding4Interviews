class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 返回构造的TreeNode根节点
def reConstructBinaryTree(pre, tin):
    # write code here
    if not pre:
        return None
    root_val = pre[0]
    root = TreeNode(root_val)
    for i in range(len(tin)):
        if tin[i] == root_val:
            break
    root.left = reConstructBinaryTree(pre[1:1+i], tin[:i])
    root.right = reConstructBinaryTree(pre[1+i:], tin[i+1:])
    
    return root

def preorder(root):
    if root:
        preorder(root.left)
        print(root.val)
        preorder(root.right)
preorder(reConstructBinaryTree([1,2,3,4,5,6,7],[3,2,4,1,6,5,7]))

我的解法
    def reConstructBinaryTree(self, pre, tin):
        # write code here
        if len(pre) == 0:
            return
        root = TreeNode(pre[0])
        pos = tin.index(pre[0])
        root.left = self.reConstructBinaryTree(pre[1:pos+1],tin[0:pos])
        root.right = self.reConstructBinaryTree(pre[pos+1:],tin[pos+1:])
        return root
