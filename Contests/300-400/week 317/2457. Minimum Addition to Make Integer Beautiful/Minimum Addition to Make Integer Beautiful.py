#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Minimum Addition to Make Integer Beautiful.py 
@time: 2022/10/30
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""


class Solution:
    def makeIntegerBeautiful(self, n: int, target: int) -> int:
        def get_valid_num(m: int):
            m_str_list = ['0'] + list(str(m))
            cur = 0
            for i, t in enumerate(m_str_list):
                if i == 0: continue
                cur += int(t)
                if cur > target:
                    m_str_list[i - 1] = str(int(m_str_list[i - 1]) + 1)
                    m_str_list = m_str_list[:i] + ['0'] * (len(m_str_list) - i)
                    carry = 0
                    for j in range(i - 1, -1, -1):
                        tmp = int(m_str_list[j]) + carry
                        if tmp > 9:
                            m_str_list[j] = str(tmp % 10)
                            carry = tmp // 10
                        else:
                            m_str_list[j] = str(tmp)
                            carry = 0
                    return get_valid_num(int(''.join(m_str_list)))
            return m

        return get_valid_num(n) - n


so = Solution()
# print(so.makeIntegerBeautiful(n=16, target=6))
print(so.makeIntegerBeautiful(204932336,16))