#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Construct String With Repeat Limit.py 
@time: 2022/02/20
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

import collections


class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        cnter = collections.Counter(s)
        s2 = list(sorted(set(s), reverse=True))
        ret = []
        while s2:
            print(f'{"".join(ret)=},{s2=},{cnter=}')
            if cnter[s2[0]] <= repeatLimit:
                ret.append(s2[0] * cnter[s2[0]])
                cnter[s2[0]] = 0
                s2.pop(0)
            else:
                cnter[s2[0]] -= repeatLimit
                ret.append(s2[0] * repeatLimit)
                if len(s2) >= 2:
                    if cnter[s2[1]] > 0:
                        ret.append(s2[1])
                        cnter[s2[1]] -= 1
                        if cnter[s2[1]] == 0:
                            s2[1:2] = []
                else:
                    break
        return ''.join(ret)


so = Solution()
# print(so.repeatLimitedString(s="cczazcc", repeatLimit=3))
print(so.repeatLimitedString("xyutfpopdynbadwtvmxiemmusevduloxwvpkjioizvanetecnuqbqqdtrwrkgt", 1))
print("zyxyxwxwvwvuvuvututstrtrtqpqpqponononmlmkmkjigifiededededcbaba")