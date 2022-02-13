#!/usr/bin/python
# coding: utf-8
# @Time    : 2022/2/6 2:11
# @Author  : Ye Wang (Wayne)
# @Email   : wang121ye@hotmail.com
# @File    : Minimum Sum of Four Digit Number After Splitting Digits.py
# @Software: PyCharm


class Solution:
    def minimumSum(self, num: int) -> int:
        ret = 1e6
        str_num = str(num)
        for i in range(4):
            n1 = int(str_num[i])
            n2 = int(''.join(sorted(str_num[:i] + str_num[i + 1:])))
            ret = min(ret, n1 + n2)
        for i in range(4):
            for j in range(i + 1, 4):
                n1 = int(''.join(sorted(str_num[i] + str_num[j])))
                n2 = int(''.join(sorted([str_num[k] for k in range(4) if k != i and k != j])))
                ret = min(ret, n1 + n2)
        return ret


so = Solution()
print(so.minimumSum(num=2932))
