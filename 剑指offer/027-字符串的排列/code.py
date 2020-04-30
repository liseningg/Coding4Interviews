
def helper(s):
    if len(s) == 1:
        return s[0]
    res = []
    for i in range(len(s)):
        l = helper(s[:i] + s[i+1:])
        for j in l:
            res.append(s[i] + j)

    return res

def Permutation(ss):
    # write code here
    if not ss: return []
    words = list(ss)
    return list(sorted(set(helper(words))))

print(Permutation('aa'))


我的解法
若字符串长度小于等于1，直接返回字符串本身；
使用set作为容器存放排列结果，可以自动去重；
依次将每一个元素取出放到排列的第一个位置，拼接上除了此元素以外的剩余元素的全排列，即为整个字符串的全排列；
按字典排序并返回。
class Solution:
    def Permutation(self, ss):
        if len(ss) <= 1:
            return ss
        res = set()
        # 遍历字符串，固定第一个元素，第一个元素可以取a,b,c...，然后递归求解
         # 依次将每一个元素取出放到排列的第一个位置，拼接上除了此元素以外的剩余元素的全排列，即为整个字符串的全排列
        for i in range(len(ss)):
            for j in self.Permutation(ss[:i] + ss[i+1:]): # 依次固定了元素，其他的全排列（递归求解）
                res.add(ss[i] + j) # 集合添加元素的方法add(),集合添加去重（若存在重复字符，排列后会存在相同，如baa,baa）
        return sorted(res)         # sorted()能对可迭代对象进行排序,结果返回一个新的list
