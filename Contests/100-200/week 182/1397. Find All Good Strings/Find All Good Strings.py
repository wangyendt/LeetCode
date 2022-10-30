#!/usr/bin/env python  
# -*- coding:utf-8 -*-  
""" 
@author:  wangye
@file: Find All Good Strings.py 
@time: 2020/04/01
@contact: wangye.hope@gmail.com
@site:  
@software: PyCharm 
"""


class Solution:
    def findGoodStrings(self, n: int, s1: str, s2: str, evil: str) -> int:
        if s1 > s2: return 0
        mod = 1_000_000_000 + 7

        # if s1 and s2 have common prefix that includes evil string - there will be no solution
        # if we wouldn't do it - we'll need a lot more checks when calculate bs[]
        for i in range(n):
            if s1[i] != s2[i]:
                break
        if evil in s1[:i]:
            return 0

        # baking first dp - for first letters
        # dp[z] shows how many strings have z-th
        m = len(evil)
        dp = [0] * 26
        for i in range(ord(s1[0]), ord(s2[0]) + 1):
            dp[i - ord("a")] = 1
        # dp for bad string - bs
        bs = [0] * m
        if ord(s1[0]) <= ord(evil[0]) and ord(evil[0]) <= ord(s2[0]):
            bs[0] = 1
        # will bake future dp's based on prev-dp
        prev = dp
        # check if we have finished badString string in dp
        if bs[m - 1] > 0:
            dp[ord(evil[-1]) - ord("a")] -= bs[m - 1]

            # calculating dp for all other letters
        for i in range(1, n):
            presum = (sum(prev) - 2) % mod
            # next letter may start from any of previous, so we take sum()
            # but we should decrease by 2 to take care of border-case-string
            # if we should count them - we'll return them in next cycle
            dp = [presum] * 26
            # there are 1 string that was equal to s1[0:i) and added up into all letters
            # and one for s2[0:i] we excluded them in  "presum=(sum(prev)-2) % mod"
            # now we should count it in for every letter that >=s1[i] and <=s2[i]
            for j in range(26):
                if ord("a") + j >= ord(s1[i]):
                    dp[j] += 1
                if ord("a") + j <= ord(s2[i]):
                    dp[j] += 1
                dp[j] = dp[j] % mod

            # calculating all growing evil strings (except new one from i-th position) in reverse order
            for j in range(1, m)[::-1]:
                l = ord(evil[j]) - ord("a")
                bs[j] = bs[j - 1]
                if i < j: continue
                # if evil slided by the edge, and current symbol "slips" from it - we should decrease it by 1
                # for the edge string that will not hold
                if evil[:j] == s1[i - j:i] and evil[j] < s1[i]:
                    bs[j] -= 1
                    bs[j] = bs[j] % mod
                    continue
                if evil[:j] == s2[i - j:i] and evil[j] > s2[i]:
                    bs[j] -= 1
                    bs[j] = bs[j] % mod
            # check if
            # we should do it before assigning bs[0] - new evil string startin i-th position
            # if first char of evil-string equals last - this string should be excluded from
            # future calculations
            # decrease dp[evil[-1]] by bs[-1] - those are string with evel substring

            l = ord(evil[-1]) - ord("a")
            dp[l] = (dp[l] - bs[-1]) % mod

            # plus there is something like a "data race" () if len(evil)==1

            l = ord(evil[0]) - ord("a")
            if len(evil) == 1:
                dp[l] = 0
            # now start calculating new evil string rising from i-th position (should be zero if len(evil)==1)
            bs[0] = dp[l]

            # get ready for next step
            prev = dp

        return sum(dp) % mod


so = Solution()
print(so.findGoodStrings(n=2, s1="aa", s2="da", evil="b"))
print(so.findGoodStrings(n=8, s1="leetcode", s2="leetgoes", evil="leet"))
print(so.findGoodStrings(n=2, s1="gx", s2="gz", evil="x"))
