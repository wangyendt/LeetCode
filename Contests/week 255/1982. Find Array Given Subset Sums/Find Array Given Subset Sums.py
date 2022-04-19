#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Find Array Given Subset Sums.py 
@time: 2021/08/22
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *


class Solution:
    def recoverArray(self, n: int, sums: List[int]) -> List[int]:
        BIAS = -min(sums)

        st = SortedList()
        for x in sums:
            st.add(x + BIAS)
        st.discard(st[0])
        ans = [st[0]]

        for i in range(1, n):
            for msk in range(1 << i):  # 找出所有子集和
                if (msk >> (i - 1)) & 1:  # 避免重复删除(保证ans最新的一位被取到)
                    sm = 0
                    for j in range(i):
                        if (msk >> j) & 1:
                            sm += ans[j]
                    st.discard(sm)
            ans.append(st[0])

        for i in range(1 << n):  # 找出一个和为BIAS的子集
            sm = 0
            for j in range(n):
                if (i >> j) & 1:
                    sm += ans[j]
            if sm == BIAS:
                for j in range(n):
                    if (i >> j) & 1:
                        ans[j] = -ans[j]
                break
        return ans
