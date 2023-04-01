#!/usr/bin/env python
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Count Number of Rectangles Containing Each Point.py 
@time: 2022/04/24
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *
import bisect
import collections


class Solution:
    def countRectangles(self, rectangles: List[List[int]], points: List[List[int]]) -> List[int]:
        rectangles = sorted(rectangles)
        rectangle_map = collections.defaultdict(list)
        for l, h in rectangles:
            rectangle_map[h].append(l)

        def contains(x, y):
            count = 0
            for height, widths in rectangle_map.items():
                if height >= y:
                    count += len(widths) - bisect.bisect(widths, x - 1)
            return count

        ret = []
        for x, y in points:
            ret.append(contains(x, y))
        return ret


so = Solution()
print(so.countRectangles(rectangles=[[2, 3], [1, 2], [2, 5]], points=[[2, 1], [1, 4]]))
