#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Number of People Aware of a Secret.py 
@time: 2022/07/03
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""


class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        dp = [0] * n
        mod = 10 ** 9 + 7
        ret = 0
        for i in range(n):
            if i < delay:
                dp[i] = 1 if i == 0 else 0
            else:
                for j in range(i - delay, max(-1, i - forget), -1):
                    dp[i] = (dp[i] + dp[j]) % mod
                if i >= forget:
                    ret = (ret - dp[i - forget]) % mod
        # print(dp)
        return (ret + sum(dp)) % mod


so = Solution()
print(so.peopleAwareOfSecret(n=6, delay=2, forget=4))
print(so.peopleAwareOfSecret(n=8, delay=2, forget=4))
print(so.peopleAwareOfSecret(4, 1, 4))
