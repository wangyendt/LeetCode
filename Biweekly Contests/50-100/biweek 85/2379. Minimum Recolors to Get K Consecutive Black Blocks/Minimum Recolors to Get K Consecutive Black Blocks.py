#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Minimum Recolors to Get K Consecutive Black Blocks.py 
@time: 2022/10/08
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

import collections


class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        stack = collections.defaultdict(int)
        ret = len(blocks)
        for i, b in enumerate(blocks):
            stack[b] += 1
            if i >= k - 1:
                ret = min(ret, k - stack['B'])
                # print(stack)
                stack[blocks[i - (k - 1)]] -= 1
        return ret


so = Solution()
print(so.minimumRecolors(blocks="WBWBBBW", k=2))
