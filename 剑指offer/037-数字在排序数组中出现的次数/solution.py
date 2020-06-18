def biSearch(data, k):
    low = 0
    high = len(data) - 1
    while low <= high:
        mid = (low + high) // 2
        if data[mid] > k:
            high = mid - 1
        elif data[mid] < k:
            low = mid + 1
    return high

def GetNumberOfK(data, k):
    # write code here
    if not data: return 0
    return biSearch(data, k+0.5) - biSearch(data, k-0.5)

print(GetNumberOfK([3,3,3, 4],3))


我的解法
1（易理解）
```
# -*- coding:utf-8 -*-
class Solution:
    def GetNumberOfK(self, data, k):
        # write code here
        #left  左边<k  右边>=k
        #right 左边<=k 右边>k
        #right-left+1
        if not data:
            return 0
        l,r = 0,len(data)-1
        while l<r:
            mid = (l+r) /2
            if data[mid] < k:
                l = mid +1
            else:
                r = mid
        if data[l] != k:
            return 0
        left = l
        l,r = 0,len(data)-1

        while l<r:
            mid = (l+r+1)/2    #右边点不一样， 右边需要落到偏右边一个位置，如果不加1的话，可能会漏掉一个数
            if data[mid] <= k:
                l = mid
            else:
                r = mid -1
        right = r
        return right-left+1
```
  
2
# -*- coding:utf-8 -*-
class Solution:
    def GetNumberOfK(self, data, k):
        # write code here
        if not data:  return 0
 
        # 二分查找，找出第一次出现的下标
        def get_first(data, k):
            l, r = 0, len(data) - 1
            while l <= r:
                m = l + (r - l)//2
                if data[m] < k:
                    l = m + 1
                else:
                    r = m - 1
            return l
 
        # 找出最后一次出现的下标
        def get_last(data, k):
            l, r = 0, len(data) - 1
            while l <= r:
                m = l + (r - l)//2
                if data[m] <= k:
                    l = m + 1
                else:
                    r = m - 1
            return r
         
        first_index = get_first(data, k)
        last_index = get_last(data, k)
        return last_index - first_index + 1
