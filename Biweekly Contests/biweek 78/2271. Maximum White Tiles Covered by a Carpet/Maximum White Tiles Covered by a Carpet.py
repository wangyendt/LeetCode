#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Maximum White Tiles Covered by a Carpet.py 
@time: 2022/05/15
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

import bisect
from typing import *


class Solution:
    def maximumWhiteTiles(self, tiles: List[List[int]], carpetLen: int) -> int:
        tiles.sort(key=lambda x: x[0])
        presum = [0]
        res = []
        for l, r in tiles:
            presum.append(presum[-1] + r - l + 1)
            res.append(l)
            res.append(r)
        ret = 0
        for i, (l, r) in enumerate(tiles):
            idx = bisect.bisect_right(x=l + carpetLen - 1, a=res)
            if idx >= len(res):
                ret = max(ret, presum[-1] - presum[i])
                break
            m = idx // 2
            cur = presum[m] - presum[i]
            if idx & 1:
                cur += l + carpetLen - 1 - tiles[m][0] + 1
            ret = max(ret, cur)
        return ret
