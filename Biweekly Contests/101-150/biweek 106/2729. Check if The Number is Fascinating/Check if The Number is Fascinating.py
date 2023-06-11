"""
@author: wangye(Wayne)
@license: Apache Licence
@file: Check if The Number is Fascinating.py
@time: 20230611
@contact: wang121ye@hotmail.com
@site:  wangyendt@github.com
@software: PyCharm

# code is far away from bugs.
"""


class Solution:
    def isFascinating(self, n: int) -> bool:
        res = list(str(n) + str(n * 2) + str(n * 3))
        return '0' not in res and len(res) == set(res) == 9


so = Solution()
print(so.isFascinating(267))
print(so.isFascinating(783))
