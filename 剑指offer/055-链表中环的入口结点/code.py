class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def EntryNodeOfLoop(self, pHead):
        # write code here
        head = ListNode(0)
        head.next = pHead
        fast = head
        slow = head
        while True:
            if fast and fast.next:
                fast = fast.next.next
                slow = slow.next
            else:
                return None
            if fast == slow:
                fast = head
                break
        while fast != slow:
            fast = fast.next
            slow = slow.next
        return fast

我的解法

    def EntryNodeOfLoop(self, pHead):
        # 需要定义两个指针，其中一个条两部，一个跳一步
        # 循环跳
        # 要么是快的指针为空（没有环），要么是快慢终又一次相等（有环）
        if pHead == None:
            return None

        fastPointer = pHead
        slowPointer = pHead
        while fastPointer and fastPointer.next:
            fastPointer = fastPointer.next.next
            slowPointer = slowPointer.next
            if fastPointer == slowPointer:
                break

        if fastPointer == None or fastPointer.next == None:
            return None

        # 如果slow走了l的长度，那么fast就走了2l的长度
        # 假设从开始到入口点的长度为s，slow在环里面走的长度是d
        # 那么 l = s + d
        # 假设 slow没走的长度是m，fast走的长度是多少
        # fast走的长度就是 n*(m+d) + d + s = 2l
        # 代入 n*(m+d) + d + s = (m+d) * 2
        # n(m+d) = s+d
        # s = nm + (n-1)d
        # s = m + (n-1)(m+d)

        fastPointer = pHead
        while fastPointer != slowPointer:
            fastPointer = fastPointer.next
            slowPointer = slowPointer.next
        return fastPointer
    
   最后一步还可以这么写
        while fastpoint and slowpoint:
            if fastpoint == slowpoint:
                return fastpoint
            else:
                fastpoint = fastpoint.next
                slowpoint = slowpoint.next
