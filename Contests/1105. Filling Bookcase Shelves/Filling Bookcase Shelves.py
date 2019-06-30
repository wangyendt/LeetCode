#!/usr/bin/env python  
# -*- coding:utf-8 -*-  
""" 
@author:  wangye
@file: Filling Bookcase Shelves.py 
@time: 2019/06/30
@contact: wangye.hope@gmail.com
@site:  
@software: PyCharm 
"""

import sys


class Solution:
    def minHeightShelves(self, books: list(list()), shelf_width: int) -> int:
        dp = [sys.maxsize] * (len(books) + 1)
        dp[0] = 0
        for i in range(len(books) + 1):
            availableWidth = shelf_width
            maxHeightInThisRow = 0
            j = i - 1
            while j >= 0 and availableWidth >= books[j][0]:
                availableWidth -= books[j][0]
                maxHeightInThisRow = max(maxHeightInThisRow, books[j][1])
                dp[i] = min(dp[i], dp[j] + maxHeightInThisRow)
                j -= 1
        return dp[-1]


so = Solution()
print(so.minHeightShelves([[1, 1], [2, 3], [2, 3], [1, 1], [1, 1], [1, 1], [1, 2]], 4), 6)
