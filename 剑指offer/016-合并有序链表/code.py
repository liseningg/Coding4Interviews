class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
解法1
def Merge(pHead1, pHead2):
    # write code here
    res = ListNode(0)
    head = res
    while pHead1 and pHead2:
        if pHead1.val <= pHead2.val:
            head.next = pHead1
            head = head.next
            pHead1 = pHead1.next
        else:
            head.next = pHead2
            head = head.next
            pHead2 = pHead2.next
            
    if pHead1:
        head.next = pHead1
    if pHead2:
        head.next = pHead2
    return res.next
解法2
def Merge(self, l1, l2):
    dummy = cur = ListNode(0)
    while l1 and l2:
        if l1.val < l2.val:
            cur.next = l1
            l1 = l1.next
        else:
            cur.next = l2
            l2 = l2.next
        cur = cur.next
    cur.next = l1 or l2
    return dummy.next
递归方法：
def Merge(self, l1, l2):
    if not l1 or not l2:
        return l1 or l2
    if l1.val < l2.val:
        l1.next = self.Merge(l1.next, l2)
        return l1
    else:
        l2.next = self.Merge(l1, l2.next)
        return l2
递归方法优化版：
def Merge(self, pHead1, pHead2):
    # write code here
    if pHead1 and pHead2:
        if pHead1.val > pHead2.val:
            pHead1, pHead2 = pHead2, pHead1
        pHead1.next = self.Merge(pHead1.next, pHead2)
    return pHead1 or pHead2
