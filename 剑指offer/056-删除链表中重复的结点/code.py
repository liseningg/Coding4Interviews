class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteDuplication(self, pHead):
        # write code here
        head = ListNode(0)
        head.next = pHead
        p = head
        q = head.next
        while q and q.next:
            if q.next.val == q.val:
                while q.next and q.next.val == q.val:
                    q.next = q.next.next
                p.next = q.next
                q = p.next
            else:
                p = q
                q = q.next
        return head.next
