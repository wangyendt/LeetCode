#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Count Vowel Strings in Ranges.py 
@time: 2023/02/05
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *


class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        i_vowels = []
        for i, w in enumerate(words):
            if w[-1] in {'a', 'e', 'i', 'o', 'u'} and w[0] in {'a', 'e', 'i', 'o', 'u'}:
                i_vowels.append(1)
            else:
                i_vowels.append(0)
        pre_sum = [0]
        for i in i_vowels:
            pre_sum.append(pre_sum[-1] + i)
        ret = []
        for q1, q2 in queries:
            ret.append(pre_sum[q2 + 1] - pre_sum[q1])
        return ret


so = Solution()
print(so.vowelStrings(
    ["bzmxvzjxfddcuznspdcbwiojiqf", "mwguoaskvramwgiweogzulcinycosovozppl", "uigevazgbrddbcsvrvnngfrvkhmqszjicpieahs", "uivcdsboxnraqpokjzaayedf", "yalc", "bbhlbmpskgxmxosft", "vigplemkoni", "krdrlctodtmprpxwditvcps", "gqjwokkskrb", "bslxxpabivbvzkozzvdaykaatzrpe", "qwhzcwkchluwdnqjwhabroyyxbtsrsxqjnfpadi", "siqbezhkohmgbenbkikcxmvz", "ddmaireeouzcvffkcohxus", "kjzguljbwsxlrd", "gqzuqcljvcpmoqlnrxvzqwoyas", "vadguvpsubcwbfbaviedr", "nxnorutztxfnpvmukpwuraen",
     "imgvujjeygsiymdxp", "rdzkpk", "cuap", "qcojjumwp", "pyqzshwykhtyzdwzakjejqyxbganow", "cvxuskhcloxykcu", "ul", "axzscbjajazvbxffrydajapweci"]
    , [[4, 4], [6, 17], [10, 17], [9, 18], [17, 22], [5, 23], [2, 5], [17, 21], [5, 17], [4, 8], [7, 17], [16, 19], [7, 12], [9, 20], [13, 23], [1, 5], [19, 19]]))
