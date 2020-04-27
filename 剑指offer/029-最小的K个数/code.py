
def sink(array, k):
    n = len(array)
    left = 2 * k + 1
    right = 2 * k + 2
    if left >= n: return
    min_i = left 
    if right < n and array[left] > array[right]:
        min_i = right
    if array[min_i] < array[k]:
        array[min_i], array[k] = array[k], array[min_i]
        sink(array, min_i)

def build_heap(list):
    n = len(list)
    for i in range(n//2, -1, -1):
        sink(list, i)

    return list

def GetLeastNumbers_Solution(tinput, k):
    if k > len(tinput): return []
    heap = build_heap(tinput)  # 建堆o(n)复杂度
    res = []
    for _ in range(k):  # 取topk o(klogn)复杂度
        heap[0], heap[-1] = heap[-1], heap[0]
        res.append(heap.pop())
        sink(heap, 0)
    return res


print(GetLeastNumbers_Solution([4,5,1,6,2,7,3,8],4))


# 我的解法
# 堆排序
class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        # 第一种
        # if len(tinput) < k:
        #     return []
        # ret = sorted(tinput)
        # return ret[:k]

        # 第二种,使用最大堆
        # 创建或者是插入最大堆
        def createMaxHeap(num):
            maxHeap.append(num)
            currentIndex = len(maxHeap) - 1
            while currentIndex != 0:
                parentIndex = (currentIndex - 1) >> 1
                if maxHeap[parentIndex] < maxHeap[currentIndex]:
                    maxHeap[parentIndex], maxHeap[currentIndex] = maxHeap[currentIndex], maxHeap[parentIndex]
                    currentIndex = parentIndex
                else:
                    break

        # 调整最大堆，头节点发生改变
        def adjustMaxHeap(num):
            if num < maxHeap[0]:
                maxHeap[0] = num

            maxHeapLen = len(maxHeap)
            index = 0
            while index < maxHeapLen:
                leftIndex = index * 2 + 1
                rightIndex = index * 2 + 2
                if rightIndex < maxHeapLen:
                    if maxHeap[rightIndex] < maxHeap[leftIndex]:
                        largerIndex = leftIndex
                    else:
                        largerIndex = rightIndex
                elif leftIndex < maxHeapLen:
                    largerIndex = leftIndex
                else:
                    break

                if maxHeap[index] < maxHeap[largerIndex]:
                    maxHeap[index], maxHeap[largerIndex] = maxHeap[largerIndex], maxHeap[index]
                index = largerIndex

        maxHeap = []
        tinputLen = len(tinput)

        if tinputLen < k or k <= 0:
            return []

        for i in range(tinputLen):
            if i < k:
                createMaxHeap(tinput[i])
            else:
                adjustMaxHeap(tinput[i])

        return sorted(maxHeap)

