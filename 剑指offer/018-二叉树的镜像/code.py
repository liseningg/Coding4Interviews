

def Mirror(root):
    # write code here
    if not root:
        return None
    tmp = Mirror(root.right)
    root.right = Mirror(root.left)
    root.left = tmp
    return root

我的解法

    def Mirror(self, root):
        # write code here
        if root != None:
            root.left,root.right = root.right,root.left
            self.Mirror(root.left)
            self.Mirror(root.right)
            
