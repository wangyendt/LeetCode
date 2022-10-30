#!/usr/bin/env python
# encoding: utf-8

"""
@author: Wayne
@contact: wangye.hope@gmail.com
@software: PyCharm
@file: Course Schedule IV
@time: 2020/05/30 22:44
"""


class Course:
    def __init__(self, ind):
        self.ind = ind
        self.prev = []
        self.post = []


class Solution:
    def checkIfPrerequisite(self, n: int, prerequisites: list(list()), queries: list(list())) -> list:
        courses = {i: Course(i) for i in range(n)}
        for pre in prerequisites:
            courses[pre[1]].prev.append(pre[0])
        ret = []
        answer = dict()
        for q1, q2 in queries:
            if (q1, q2) in answer:
                ret.append(answer[(q1, q2)])
                continue
            stack = [q2]
            rubbish = set()
            while stack:
                s = stack.pop()
                if s in rubbish: continue
                if q1 == s:
                    ret.append(True)
                    answer[(q1, q2)] = True
                    break
                else:
                    for pre in courses[s].prev:
                        stack.append(pre)
                rubbish.add(s)
            else:
                ret.append(False)
                answer[(q1, q2)] = False
        return ret


so = Solution()
print(so.checkIfPrerequisite(n=2, prerequisites=[[1, 0]], queries=[[0, 1], [1, 0]]))
print(so.checkIfPrerequisite(n=2, prerequisites=[], queries=[[1, 0], [0, 1]]))
print(so.checkIfPrerequisite(n=3, prerequisites=[[1, 2], [1, 0], [2, 0]], queries=[[1, 0], [1, 2]]))
print(so.checkIfPrerequisite(n=3, prerequisites=[[1, 0], [2, 0]], queries=[[0, 1], [2, 0]]))
print(so.checkIfPrerequisite(n=5, prerequisites=[[0, 1], [1, 2], [2, 3], [3, 4]],
                             queries=[[0, 4], [4, 0], [1, 3], [3, 0]]))
