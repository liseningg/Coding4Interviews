class Solution(object):
    def getIntersectionNode(self, pHead1, pHead2):
        p1, n_p1 = pHead1, 0
        p2, n_p2 = pHead2, 0
        while p1:
            p1 = p1.next
            n_p1 += 1
        while p2:
            p2 = p2.next
            n_p2 += 1
        if n_p1 < n_p2:     # p1指向长链
            pHead1, pHead2 = pHead2, pHead1
            n_p1, n_p2 = n_p2, n_p1

        for _ in range(n_p1 - n_p2):
            pHead1 = pHead1.next
        while pHead1 and pHead2:
            if pHead1 == pHead2:
                return pHead1
            else:
                pHead1 = pHead1.next
                pHead2 = pHead2.next
        return None


我的解法：
    def FindFirstCommonNode(self, pHead1, pHead2):
        # write code here
                # write code here
        if not pHead1 or not pHead2:
            return None
        pTmp1 = pHead1
        pTmp2 = pHead2
        while pTmp1 and pTmp2:
            if pTmp1 == pTmp2:
                return pTmp1
            pTmp1 = pTmp1.next
            pTmp2 = pTmp2.next
        if pTmp1:
            k = 0
            while pTmp1:
                pTmp1 = pTmp1.next
                k += 1
            pTmp1 = pHead1
            pTmp2 = pHead2
            for _ in range(k):
                pTmp1 = pTmp1.next
            while pTmp1 != pTmp2:
                pTmp1 = pTmp1.next
                pTmp2 = pTmp2.next
            return pTmp1
        
        if pTmp2:
            k = 0
            while pTmp2:
                pTmp2 = pTmp2.next
                k += 1
            pTmp1 = pHead1
            pTmp2 = pHead2
            for _ in range(k):
                pTmp2 = pTmp2.next
            while pTmp1 != pTmp2:
                pTmp1 = pTmp1.next
                pTmp2 = pTmp2.next
            return pTmp1
