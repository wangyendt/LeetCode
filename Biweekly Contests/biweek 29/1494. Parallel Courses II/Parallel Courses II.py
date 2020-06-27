#!/usr/bin/env python
# encoding: utf-8

"""
@author: Wayne
@contact: wangye.hope@gmail.com
@software: PyCharm
@file: Parallel Courses II
@time: 2020/06/27 22:53
"""


class Solution:
    def minNumberOfSemesters(self, n: int, dependencies: list(list()), k: int) -> int:
        # Convert course dependencies
        courses_before = {course: [] for course in range(1, n + 1)}
        courses_after = {course: [] for course in range(1, n + 1)}
        for dependency in dependencies:
            x, y = dependency
            courses_before[y].append(x)
            courses_after[x].append(y)
        # Count semesters: greedy approach.
        semester_cnt = 0
        while courses_before:
            # Choose courses which can be taken in this semester
            courses_to_take = []
            for course, dependencies_list in courses_before.items():
                if len(dependencies_list) == 0:
                    courses_to_take.append((course, len(courses_after[course])))
            # Choose which courses actually to take:
            # The more other courses depends on its, the more priority it has in this semester
            courses_to_take.sort(key=lambda x: x[1], reverse=True)
            courses_to_take = courses_to_take[:min(k, len(courses_to_take))]
            # Remove taken courses from dependecies hash maps
            for course, _ in courses_to_take:
                del courses_before[course]
                for depend_course in courses_after[course]:
                    courses_before[depend_course].remove(course)
            semester_cnt += 1
        return semester_cnt
