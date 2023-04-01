#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Apply Discount to Prices.py 
@time: 2022/05/29
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""


class Solution:
    def discountPrices(self, sentence: str, discount: int) -> str:
        res = sentence.split(' ')
        ret = []
        for i, s in enumerate(res):
            if len(s) > 1 and s[0] == '$' and all(c in '0123456789' for c in s[1:]):
                num = int(s[1:])
                ret.append(f'${num * (100 - discount) / 100:.2f}')
            else:
                ret.append(s)
        return ' '.join(ret)


so = Solution()
print(so.discountPrices("$76111 ab $6 $", 48))
