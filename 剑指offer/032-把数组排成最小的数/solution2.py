import functools
def compare(s1, s2):
    if s1+s2 < s2+s1:
        return -1
    elif s1+s2 == s2+s1:
        return 0
    else:
        return 1

def PrintMinNumber(numbers):
    # write code here
    if not numbers: return ''
    if len(numbers) == 1: return numbers[0]
    str_numbers = [str(n) for n in numbers]

    return ''.join(sorted(str_numbers, key=functools.cmp_to_key(compare)))

print(PrintMinNumber([32, 3, 321]))
    
我的解法
空数组返回空串；
将数组中的数字转化为字符串；
字符串拼接后的字典排序；
拼接返回；
# -*- coding:utf-8 -*-
class Solution:
    def PrintMinNumber(self, numbers):
        if not numbers: return ''

        numbers = list(map(str, numbers))
        #cmp参数其中的规律就是：两两比较，如果返回为正，则交换两者的位置，
        #cmp（x，y） x>y 1 x<y -1 x=y 0
        numbers.sort(cmp=lambda x, y: cmp(x + y, y + x))
        return ''.join(numbers).lstrip('0') or '0'

