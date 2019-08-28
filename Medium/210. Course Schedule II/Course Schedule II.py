# !/usr/bin/env python
# -*- coding: utf-8 -*-
# author: wang121ye
# datetime: 2019/8/28 11:08
# software: PyCharm


class Course:
    def __init__(self, ind):
        self.ind = ind
        self.prev = []
        self.post = []


class Solution:
    def findOrder(self, numCourses: int, prerequisites: list(list())) -> list:
        courses = {i: Course(i) for i in range(numCourses)}
        for pre in prerequisites:
            courses[pre[0]].prev.append(pre[1])
            courses[pre[1]].post.append(pre[0])
        stack, ret = [], []
        stack = [k for k, v in courses.items() if not v.prev]
        while stack:
            s = stack.pop()
            ret.append(s)
            for p in courses[s].post:
                courses[p].prev.remove(s)
                if not courses[p].prev:
                    stack.append(p)
        if len(ret) != numCourses: return []
        return ret


so = Solution()
print(so.findOrder(2, [[1, 0]]))
print(so.findOrder(3, [[1, 0], [2, 1]]))
