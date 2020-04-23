def PrintFromTopToBottom(root):
    # write code here
    if not root: return []
    queue = [root]
    res = []
    while queue:
        n = len(queue)
        for _ in range(n):
            if not queue: break
            node = queue.pop(0)
            res.append(node.val)
            if node.left:             
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    return res

我的解法

    def PrintFromTopToBottom(self, root):
        # write code here 
        if not root:
            return []
        queue,result = [],[]
        queue.append(root)
        while len(queue) > 0:
            node = queue.pop(0)
            result.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return result
    
