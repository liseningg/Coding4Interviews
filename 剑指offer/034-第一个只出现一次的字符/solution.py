def FirstNotRepeatingChar(s):
    # write code here
    map = {}
    for i in range(len(s)):
        map[s[i]] = map.get(s[i], 0) + 1
    for i in range(len(s)):
        if map[s[i]] == 1:
            return i
    return -1

print(FirstNotRepeatingChar('abac'))


我的解法
#方法一：利用数组自己建立个哈希表
class Solution:
    def FirstNotRepeatingChar(self, s):
        # write code here
        if s==' ':
            return -1
        hashtable=[0]*256
        for i in s:
            hashtable[ord(i)] += 1
        for i in s:
            if hashtable[ord(i)]==1:
                return s.index(i)
        return -1
 
#方法二：利用python自带的字典
class Solution:
    def FirstNotRepeatingChar(self, s):
        # write code here
        if s==' ':
            return -1
        d=dict()
        #第一次遍历字符串，将每个字符的次数存入字典
        for i in s:    
            d[i]=d.get(i,0)+1
        #第二次遍历字符串，检查每个字符出现的次数
        for i in s:
            if d[i]==1:   #O(1)
                return s.index(i)
        return -1
