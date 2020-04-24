
class Solution:
    def Print(self, pRoot):
        # write code here
        if not pRoot: return []
        res = []
        queue = [pRoot]
        j = -1
        while queue:
            j += 1
            n = len(queue)
            temp = []
            for _ in range(n):
                node = queue.pop(0)
                temp.append(node.val)
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            if j % 2:
                temp.reverse()
            res.append(temp)
        return res
    
我的解法
class Solution:
    def Print(self, pRoot):
        # 如果二叉树为空，就返回空
        if pRoot == None:
            return []
        # 定义奇数行，从左到右
        stack1 = [pRoot]
        # 定义偶数行，从右到左
        stack2 = []
        # 定义返回的顺序列表
        ret = []
        # 当奇数行或者偶数行都不为空时循环
        while stack1 or stack2:
            # 如果奇数行有值
            if stack1:
                # 临时列表
                tmpRet = []
                # 如果奇数行有值，就一直循环
                while stack1:
                    # 临时弹出数据
                    tmpNode = stack1.pop()
                    # 临时列表里面添加临时数据的值
                    tmpRet.append(tmpNode.val)
                    # 如果有临时数据的左节点
                    if tmpNode.left:
                        # 就在偶数行添加临时数据的左节点
                        stack2.append(tmpNode.left)
                    # 如果有临时数据的右节点
                    if tmpNode.right:
                        # 就在偶数行添加临时数据的右节点
                        stack2.append(tmpNode.right)
                # 在返回的顺利列表里面添加临时列表
                ret.append(tmpRet)
            # 如果偶数行有值
            if stack2:
                # 临时列表
                tmpRet = []
                # 如果奇数行有值，就一直循环
                while stack2:
                    # 临时弹出数据
                    tmpNode = stack2.pop()
                    # 临时列表里面添加临时数据的值
                    tmpRet.append(tmpNode.val)
                    # 如果有临时数据的右节点
                    if tmpNode.right:
                        # 就在偶数行添加临时数据的右节点
                        stack1.append(tmpNode.right)
                    # 如果有临时数据的左节点
                    if tmpNode.left:
                        # 就在偶数行添加临时数据的左节点
                        stack1.append(tmpNode.left)
                # 在返回的顺利列表里面添加临时列表
                ret.append(tmpRet)
        # 返回顺序列表
        return ret
