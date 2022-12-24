#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Reward Top K Students.py 
@time: 2022/12/24
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *


class Solution:
    def topStudents(self, positive_feedback: List[str], negative_feedback: List[str], report: List[str], student_id: List[int], k: int) -> List[int]:
        reports = []
        positive_feedback_set = set(positive_feedback)
        negative_feedback_set = set(negative_feedback)
        for rep in report:
            res = 3 * sum(1 for r in rep.split(' ') if r in positive_feedback_set)
            res -= sum(1 for r in rep.split(' ') if r in negative_feedback_set)
            reports.append(res)
        # print(reports)
        sorted_idx = list(sorted(range(len(student_id)), key=lambda x: (-reports[x], student_id[x])))
        ret = []
        for i in range(k):
            ret.append(student_id[sorted_idx[i]])
        return ret


so = Solution()
print(so.topStudents(positive_feedback=["smart", "brilliant", "studious"], negative_feedback=["not"], report=["this student is not studious", "the student is smart"], student_id=[1, 2], k=2))
