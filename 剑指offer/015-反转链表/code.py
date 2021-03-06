class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def ReverseList(pHead):
    # write code here

    if not pHead: return None
    head = ListNode(0)
    head.next = pHead
    p = pHead
    while(p.next):
        tp = p.next
        p.next = p.next.next
        tp.next = head.next
        head.next = tp
    return head.next


    # head->4->3->2->1->5
    #                p  tp
    
我的代码
class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        # write code here
        if pHead == None or pHead.next == None:
            return pHead
        pre = None
        cur = pHead
        while cur!=None:
            temp = cur.next
            cur.next = pre
            pre = cur
            cur = temp
            
        return pre
