"""
@author: wangye(Wayne)
@license: Apache Licence
@file: Find the Losers of the Circular Game.py
@time: 20230514
@contact: wang121ye@hotmail.com
@site:  wangyendt@github.com
@software: PyCharm

# code is far away from bugs.
"""

from typing import *


class Solution:
    def circularGameLosers(self, n: int, k: int) -> List[int]:
        start = 0
        i = 1
        seen = {0}
        while True:
            start = (start + i * k) % n
            if start in seen:
                return [j + 1 for j in sorted(list(set(range(n)) - seen))]
            i += 1
            seen.add(start)


so = Solution()
print(so.circularGameLosers(n=5, k=2))
