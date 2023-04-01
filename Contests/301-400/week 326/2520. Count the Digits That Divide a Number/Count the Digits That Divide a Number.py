"""
@author: wangye(Wayne)
@license: Apache Licence
@file: Count the Digits That Divide a Number.py
@time: 20230103
@contact: wang121ye@hotmail.com
@site:  wangyendt@github.com
@software: PyCharm

# code is far away from bugs.
"""


class Solution:
    def countDigits(self, num: int) -> int:
        ret = 0
        n = num
        while n:
            m = n % 10
            if m == 0: continue
            if num % m == 0:
                ret += 1
            n //= 10
        return ret
