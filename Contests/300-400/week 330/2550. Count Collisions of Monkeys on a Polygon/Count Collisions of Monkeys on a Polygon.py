"""
@author: wangye(Wayne)
@license: Apache Licence
@file: Count Collisions of Monkeys on a Polygon.py
@time: 20230131
@contact: wang121ye@hotmail.com
@site:  wangyendt@github.com
@software: PyCharm

# code is far away from bugs.
"""


class Solution:
    def monkeyMove(self, n: int) -> int:
        mod = 10 ** 9 + 7
        return (pow(2, n, mod) - 2) % mod
