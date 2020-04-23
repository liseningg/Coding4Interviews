### 前序遍历，深度优先遍历dfs
class Solution(object):
    def __init__(self):
        self.result_all = []
        self.array = []

    def pathSum(self, root, expectNumber):
        if not root: return []
        self.array.append(root.val)
        expectNumber -= root.val
        if expectNumber == 0 and not root.left and not root.right:
            self.result_all.append(self.array[:])
        self.pathSum(root.left, expectNumber)
        self.pathSum(root.right, expectNumber)
        self.array.pop()
        return self.result_all
    
我的方法

    def FindPath(self, root, expectNumber):
        # 若根结点为空，就返回空列表
        if root == None:
            return []

        # 定义最终返回列表
        ret = []
        # 定义保存路径的二维列表
        supportArrayList = [[root.val]]
        # 定义广度优先遍历的列表
        support = [root]
        # 当support中有值时一直循环
        while support:
            # 取出support中的第一个值，结点
            tmpNode = support[0]
            # 取出supportArrayList中的第一个值，列表，存放路径
            tmpArrayList = supportArrayList[0]
            # 如果取出的节点为叶子叶节点，就判断tmpArrayList的和是否和目标值相等，若相等就将其列表（路径）添加到返回列表当中
            if tmpNode.left == None and tmpNode.right == None:
                if sum(tmpArrayList) == expectNumber:
                    ret.insert(0, tmpArrayList)
            # 如果有左子结点，就执行下面
            if tmpNode.left:
                # 将左子结点添加到广度优先列表中
                support.append(tmpNode.left)
                # 将tmpArrayList进行浅拷贝得到newTmpArrayList
                newTmpArrayList = copy.copy(tmpArrayList)
                # 给newTmpArrayList添加左子结点的值
                newTmpArrayList.append(tmpNode.left.val)
                # 将newTmpArrayList添加到supportArrayList
                supportArrayList.append(newTmpArrayList)
            # 如果有右子结点，就执行下面
            if tmpNode.right:
                # 将右子结点添加到广度优先列表中
                support.append(tmpNode.right)
                # 将tmpArrayList进行浅拷贝得到newTmpArrayList
                newTmpArrayList = copy.copy(tmpArrayList)
                # 给newTmpArrayList添加左子结点的值
                newTmpArrayList.append(tmpNode.right.val)
                # 将newTmpArrayList添加到supportArrayList
                supportArrayList.append(newTmpArrayList)
            # 删除广度优先的列表的第一个值
            support.pop(0)
            # 删除保存路径的二维列表的第一个值
            supportArrayList.pop(0)
        # 返回最终结果
        return ret
    
    
这个方法不懂
class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, expectNumber):
        if not root:
            return []
        tmp = []
        if  not root.left and not root.right and root.val == expectNumber:
            return [[root.val]]
        else:
            left = self.FindPath(root.left,expectNumber-root.val)
            right = self.FindPath(root.right,expectNumber-root.val)
            for item in left+right:
                tmp.append([root.val]+item)
        return tmp
