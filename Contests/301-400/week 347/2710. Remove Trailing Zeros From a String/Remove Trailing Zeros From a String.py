"""
@author: wangye(Wayne)
@license: Apache Licence
@file: Remove Trailing Zeros From a String.py
@time: 20230528
@contact: wang121ye@hotmail.com
@site:  wangyendt@github.com
@software: PyCharm

# code is far away from bugs.
"""


class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        ret = list(num)
        while num and num[-1] == '0':
            ret.pop()
            num = num[:-1]
        else:
            return ''.join(ret)
