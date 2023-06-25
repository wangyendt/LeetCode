"""
@author: wangye(Wayne)
@license: Apache Licence
@file: Robot Collisions.py
@time: 20230625
@contact: wang121ye@hotmail.com
@site:  wangyendt@github.com
@software: PyCharm

# code is far away from bugs.
"""

from typing import *


class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        n = len(positions)

        robots = list(zip(range(n), positions, healths, directions))
        robots.sort(key=lambda x: x[1])

        ans, rights = [0] * n, []

        for i, _, h, d in robots:
            if d == 'R':
                rights.append((i, h))
                continue
            while rights and h:
                enemy = rights[-1]
                if h < enemy[1]:
                    h = 0
                    rights[-1] = (enemy[0], enemy[1] - 1)
                elif h > enemy[1]:
                    rights.pop()
                    h -= 1
                else:
                    rights.pop()
                    h = 0
            if h > 0:
                ans[i] = h

        for i, h in rights:
            ans[i] = h

        return [x for x in ans if x > 0]


so = Solution()
print(so.survivedRobotsHealths(positions=[5, 4, 3, 2, 1], healths=[2, 17, 9, 15, 10], directions="RRRRR"))
print(so.survivedRobotsHealths(positions=[3, 5, 2, 6], healths=[10, 10, 15, 12], directions="RLRL"))
print(so.survivedRobotsHealths(positions=[1, 2, 5, 6], healths=[10, 10, 11, 11], directions="RLRL"))
