"""
@author: wangye(Wayne)
@license: Apache Licence
@file: Minimum Operations to Make the Integer Zero.py
@time: 20230625
@contact: wang121ye@hotmail.com
@site:  wangyendt@github.com
@software: PyCharm

# code is far away from bugs.
"""


class Solution:
    def makeTheIntegerZero(self, num1: int, num2: int) -> int:
        ret = 0
        while bin(num1).count('1') > ret:
            ret += 1
            num1 -= num2
            if num1 < ret and num2 > 0:
                return -1
        return ret


so = Solution()
print(so.makeTheIntegerZero(num1=3, num2=-2))
