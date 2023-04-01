#!/usr/bin/env python  
# -*- coding:utf-8 -*-  
""" 
@author:  wangye
@file: Maximum Number of Coins You Can Get.py 
@time: 2020/08/24
@contact: wangye.hope@gmail.com
@site:  
@software: PyCharm 
"""


class Solution:
    def maxCoins(self, piles: list) -> int:
        n = len(piles) // 3
        ret = 0
        piles.sort()
        for i in range(n):
            ret += piles[-(i + 1) * 2]
        return ret
