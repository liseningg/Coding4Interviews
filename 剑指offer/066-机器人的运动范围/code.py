class Solution(object):
    def movingCount(self, m, n, k):
        """
        :type m: int
        :type n: int
        :type k: int
        :rtype: int
        """
        rows = m
        cols = n
        threshold = k
        array = []
        for i in range(rows):
            res = []
            for j in range(cols):
                res.append(getN(i, j))
            array.append(res)
        visited = [[0] * len(array[0]) for _ in range(len(array))]
        return BFS(array, 0, 0, threshold, visited)

def getN(i, j):
    res = 0
    while i:
        res += (i % 10)
        i //= 10
    while j:
        res += (j % 10)
        j //= 10
    return res

def BFS(array, i, j, threshold, visited):
    if i<0 or j<0 or i>len(array)-1 or j>len(array[0])-1 or array[i][j]>threshold or visited[i][j]:
        return 0
    res = 1
    visited[i][j] = 1
    res += BFS(array, i+1, j, threshold, visited)
    res += BFS(array, i-1, j, threshold, visited)
    res += BFS(array, i, j+1, threshold, visited)
    res += BFS(array, i, j-1, threshold, visited)
    return res

我的解法
# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.count = 0
 
    def movingCount(self, threshold, rows, cols):
        # 标志是否走过，没走过的标0，走过标1
        flag = [[0 for i in range(cols)] for j in range(rows)]
        self.find_way(flag, 0, 0, threshold)
        return self.count
 
    def find_way(self, flag, i, j, threshold):
        # 1. 越界返回
        if i < 0 or j < 0 or i >= len(flag) or j >= len(flag[0]):
            return
 
        # 2. 超过阈值返回
        tmp_i = list(map(int, list(str(i))))
        tmp_j = list(map(int, list(str(j))))
        if sum(tmp_i) + sum(tmp_j) > threshold:
            return
 
        # 已经走过的位置，返回
        if flag[i][j]: return
 
        # 此位置没走过，计数加一
        flag[i][j] = 1
        self.count += 1
 
        # 向四个方向继续走
        self.find_way(flag, i + 1, j, threshold)
        self.find_way(flag, i - 1, j, threshold)
        self.find_way(flag, i, j + 1, threshold)
        self.find_way(flag, i, j - 1, threshold)
