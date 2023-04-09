"""
@author: wangye(Wayne)
@license: Apache Licence
@file: Minimum Operations to Reduce an Integer to 0.py
@time: 20230331
@contact: wang121ye@hotmail.com
@site:  wangyendt@github.com
@software: PyCharm

# code is far away from bugs.
"""


class Solution:
    def minOperations(self, n: int) -> int:
        ret = 0
        while n:
            if n % 2 == 0:
                n >>= 1
            elif n & 2 > 0:
                n += 1
                ret += 1
            else:
                n >>= 2
                ret += 1
        return ret


so = Solution()
print(so.minOperations(27), 3)
print(so.minOperations(39), 3)
