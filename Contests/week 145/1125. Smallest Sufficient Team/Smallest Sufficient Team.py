#!/usr/bin/env python  
# -*- coding:utf-8 -*-  
""" 
@author:  wangye
@file: Smallest Sufficient Team.py 
@time: 2019/07/14
@contact: wangye.hope@gmail.com
@site:  
@software: PyCharm 
"""

import math, collections


class Solution:
    def smallestSufficientTeam(self, req_skills: list, people: list(list())) -> list:
        for i, skills in enumerate(people):
            people[i] = set(skills)
        for i, i_skills in enumerate(people):
            for j, j_skills in enumerate(people):
                if i != j and i_skills.issubset(j_skills):
                    people[i] = set()
        skills_to_people = collections.defaultdict(set)
        for i, skills in enumerate(people):
            for skill in skills:
                skills_to_people[skill].add(i)
            people[i] = set(skills)
        self.unmet_skills = set(req_skills)
        self.smallest_length = math.inf
        self.current_team = []
        self.best_team = []

        def meet_skill(skill=0):
            if not self.unmet_skills:
                if self.smallest_length > len(self.current_team):
                    self.smallest_length = len(self.current_team)
                    self.best_team = self.current_team[::]
                return

            if req_skills[skill] not in self.unmet_skills:
                return meet_skill(skill + 1)

            for i in skills_to_people[req_skills[skill]]:
                skills_added_by_person = people[i].intersection(self.unmet_skills)
                self.unmet_skills = self.unmet_skills - skills_added_by_person
                self.current_team.append(i)

                # Do the recursive call to further build the team.
                meet_skill(skill + 1)

                self.current_team.pop()
                self.unmet_skills = self.unmet_skills.union(skills_added_by_person)

        meet_skill()
        return self.best_team


so = Solution()
print(so.smallestSufficientTeam(req_skills=["java", "nodejs", "reactjs"],
                                people=[["java"], ["nodejs"], ["nodejs", "reactjs"]]))
