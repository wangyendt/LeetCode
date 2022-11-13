#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Maximum Number of Non-overlapping Palindrome Substrings.py 
@time: 2022/11/13
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

import bisect


class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        def find_palindromes_in_sub_string(l, r):
            count = 0
            while l >= 0 and r < len(s):
                if s[l] != s[r]:
                    break
                if r + 1 - l >= k:
                    res.append([l, r])
                count += 1
                l -= 1
                r += 1
            return count

        def maxDisjointIntervals(arr):
            arr.sort(key=lambda x: x[1])
            ret = 1
            r1 = arr[0][1]
            for i in range(1, len(arr)):
                l1 = arr[i][0]
                r2 = arr[i][1]
                if l1 > r1:
                    r1 = r2
                    ret += 1
            return ret

        res = []
        for i in range(len(s)):
            find_palindromes_in_sub_string(i - 1, i + 1)
            find_palindromes_in_sub_string(i, i + 1)
            if k == 1:
                res.append([i, i])
        return maxDisjointIntervals(res) if res else 0


so = Solution()
print(so.maxPalindromes(s="abaccdbbd", k=3))
print(so.maxPalindromes(s="adbcda", k=2))
print(so.maxPalindromes("iqqibcecvrbxxj", 1))
print(so.maxPalindromes("a" * 2000, 1000))
