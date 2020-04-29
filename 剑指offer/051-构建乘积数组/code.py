class Solution:
    def multiply(self, A):
        # write code here
        B = [1] * len(A)
        temp = 1
        for i in range(1, len(A)):   #这里range的范围要看B是从哪里开始的
            temp *= A[i-1]
            B[i] *= temp
        temp = 1
        for i in range(len(A)-2, -1, -1):  #B从n-2开始，0结束，A根据B来取对应的值
            temp *= A[i+1]
            B[i] *= temp
        return B


# [0, 1, 1]
# [1, 0, 1]
# [1, 1, 0]
