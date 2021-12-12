#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Maximum Fruits Harvested After at Most K Steps.py 
@time: 2021/12/12
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *
import bisect


class Solution:
    def maxTotalFruits(self, A: List[List[int]], pos: int, k: int) -> int:
        amt = {}
        for a, b in A:
            amt[a] = b

        # Every position with fruit except the start position.
        position = [a for a, b in A if a != pos]
        lft, rgt, n = [], [], len(position)

        idx = bisect.bisect_right(position, pos)

        # Right pre-sum
        cur_f = 0
        for i in range(idx, n):
            cur_pos = position[i]
            cur_f += amt[cur_pos]
            rgt.append([cur_pos - pos, cur_f])

        # Left pre-sum
        cur_f = 0
        for i in range(idx - 1, -1, -1):
            cur_pos = position[i]
            cur_f += amt[cur_pos]
            lft.append([pos - cur_pos, cur_f])

        # Go right then turn left
        ans = 0
        for r_dist, r_f in rgt:
            if r_dist <= k:
                cur_f = r_f
                l_dist = k - 2 * r_dist
                if l_dist > 0:  # Check fruit collected from the left side.
                    idx = bisect.bisect_right(lft, [l_dist, float('inf')])
                    if idx > 0:
                        cur_f += lft[idx - 1][1]
                ans = max(ans, cur_f)
            else:
                break

        # Go left then turn right
        for l_dist, l_f in lft:
            if l_dist <= k:
                cur_f = l_f
                r_dist = k - 2 * l_dist
                if r_dist > 0:  # Check fruit collected from the right side.
                    idx = bisect.bisect_right(rgt, [r_dist, float('inf')])
                    if idx > 0:
                        cur_f += rgt[idx - 1][1]
                ans = max(ans, cur_f)
            else:
                break

        return ans + amt.get(pos, 0)  # Add fruit collected at the start position.


so = Solution()
# print(so.maxTotalFruits(fruits=[[0, 9], [4, 1], [5, 7], [6, 2], [7, 4], [10, 9]], startPos=5, k=4))
# print(so.maxTotalFruits([[1,9],[2,10],[3,1],[5,6],[6,3],[8,2],[9,2],[11,4],[18,10],[22,8],[25,2],[26,2],[30,4],[31,5],[33,9],[34,1],[39,10]],19,9))
print(so.maxTotalFruits(
    [[0, 7], [7, 4], [9, 10], [12, 6], [14, 8],
     [16, 5], [17, 8], [19, 4], [20, 1], [21, 3],
     [24, 3], [25, 3], [26, 1], [28, 10], [30, 9], [31, 6],
     [32, 1], [37, 5], [40, 9]], 21, 30))
