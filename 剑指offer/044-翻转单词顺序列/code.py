class Solution:
    def ReverseSentence(self, s):
        # write code here
        stack = [n for n in s.split(' ')]
        stack.reverse()
        return ' '.join(stack)

print(Solution().ReverseSentence("I am a student."))

我的解法
1
class Solution:
    def ReverseSentence(self, s):
        # write code here
        return " ".join(s.split(" ")[::-1])

2
class Solution:
    def ReverseSentence(self, s):
        # write code here
        alist = s.split(" ")
        stacklist = []
        for i in alist:
            stacklist.append(i)
        result = []
        for _ in range(len(stacklist)):
            result.append(stacklist.pop())
        return " ".join(result)
