"""
@author: wangye(Wayne)
@license: Apache Licence
@file: Minimum Cost to Make All Characters Equal.py
@time: 20230528
@contact: wang121ye@hotmail.com
@site:  wangyendt@github.com
@software: PyCharm

# code is far away from bugs.
"""


class Solution:
    def minimumCost(self, s: str) -> int:
        def flip_to(t: str, target: int):
            ret = 0
            N = len(t)
            sign = 0
            if N % 2 == 1 and int(t[N // 2]) != (sign + target) % 2:
                ret += N // 2 + 1
                sign = 1 - sign
            for i in range(N // 2 - 1, -1, -1):
                if int(t[i]) != (sign + target) % 2:
                    ret += i + 1
                    sign = 1 - sign
            t = t[::-1]
            sign = 0
            for i in range(N // 2 - 1, -1, -1):
                if int(t[i]) != (sign + target) % 2:
                    ret += i + 1
                    sign = 1 - sign
            return ret

        return min(flip_to(s[:], 1), flip_to(s[:], 0))
