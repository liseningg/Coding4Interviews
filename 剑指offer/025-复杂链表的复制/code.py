class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None


# 返回 RandomListNode
def Clone(pHead):
    # write code here
    if not pHead: return None
    p = pHead
    new_h = RandomListNode(p.label)
    pre_p = new_h
    random_map = {pHead: new_h}
    p = p.next
    while p:
        new_p = RandomListNode(p.label)
        random_map[p] = new_p
        pre_p.next = new_p
        pre_p = pre_p.next
        p = p.next
    p = pHead
    new_p = new_h
    while p:
        random_p = p.random
        if random_p:
            new_p.random = random_map[random_p]

        p = p.next
        new_p = new_p.next

    return new_h

p = RandomListNode(1)
p.next = RandomListNode(2)
p.next.next = RandomListNode(3)
p.next.next.next = RandomListNode(4)
p.next.next.next.next = RandomListNode(5)
print(Clone(p))



class Solution:
    # 返回 RandomListNode
    def Clone(self, pHead):
        # 深拷贝也可以
        # return copy.deepcopy(pHead)

        # 复制一个一样的node，并且添加到之前的链表的每一个node后面
        if pHead == None:
            return None

        pTmp = pHead
        while pTmp:
            node = RandomListNode(pTmp.label)
            node.next = pTmp.next
            pTmp.next = node
            pTmp = node.next  #将指针移动到下一个被复制的节点

        # 实现新建的node的random的指向
        pTmp = pHead
        while pTmp:
            if pTmp.random:
                pTmp.next.random = pTmp.random.next
            pTmp = pTmp.next.next

        # 断开原来的node和新node的连接
        pTmp = pHead
        newHead = pHead.next #保存复制链表后的第二个元素的地址
        pNewTmp = pHead.next
        while pTmp:
            pTmp.next = pTmp.next.next
            if pNewTmp.next:
                pNewTmp.next = pNewTmp.next.next
                pNewTmp = pNewTmp.next
            pTmp = pTmp.next
        return newHead
