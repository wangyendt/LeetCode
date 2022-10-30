#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Check if Word Equals Summation of Two Words.py 
@time: 2021/05/30
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""


class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        letters = {v: str(k) for k, v in enumerate('abcdefghij')}

        def get_num(word):
            s1 = []
            for w in word:
                s1.append(letters[w])
            # print(''.join(s1))
            return int(''.join(s1))

        return get_num(firstWord) + get_num(secondWord) == get_num(targetWord)


so = Solution()
print(so.isSumEqual(firstWord="acb", secondWord="cba", targetWord="cdb"))
