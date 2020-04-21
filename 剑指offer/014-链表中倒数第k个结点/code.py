class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

#快指针先往前走k步，注意判断边界，然后快慢一起走，当快指针为none的时候，慢指针走到了倒数第k个节点
def FindKthToTail(head, k):
    # write code here
    if not head: return None
    fast_p = head
    slow_p = head
    for _ in range(k):
        if fast_p:
            fast_p = fast_p.next
        else:
            return None
    while fast_p:
        fast_p = fast_p.next
        slow_p = slow_p.next
    return slow_p
我的解法：

#Python设置两个指针，p1，p2，先让p2走k-1步，然后再一起走，直到p2为最后一个 时，p1即为倒数第k个节点
    def FindKthToTail(self, head, k):
        # write code here
        if head==None or k<=0:
            return None
        #设置两个指针，p2指针先走（k-1）步，然后再一起走，当p2为最后一个时，p1就为倒数第k个 数
        p2=head
        p1=head
        #p2先走，走k-1步，如果k大于链表长度则返回 空，否则的话继续走
        while k>1:
            if p2.next!=None:
                p2=p2.next
                k-=1
            else:
                return None
#两个指针一起 走，一直到p2为最后一个,p1即为所求
        while p2.next!=None:
            p1=p1.next
            p2=p2.next
        return p1
