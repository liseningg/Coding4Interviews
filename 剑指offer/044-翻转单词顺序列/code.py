class Solution:
    def ReverseSentence(self, s):
        # write code here
        stack = [n for n in s.split(' ')]
        stack.reverse()
        return ' '.join(stack)

print(Solution().ReverseSentence("I am a student."))

我的解法
class Solution:
    def ReverseSentence(self, s):
        # write code here
        return " ".join(s.split(" ")[::-1])
