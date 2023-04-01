"""
@author: wangye(Wayne)
@license: Apache Licence
@file: Divide Players Into Teams of Equal Skill.py
@time: 20221204
@contact: wang121ye@hotmail.com
@site:  wangyendt@github.com
@software: PyCharm

# code is far away from bugs.
"""

from typing import *


class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        n = len(skill)
        target = 2 * sum(skill) // n
        for i in range(n // 2):
            if skill[i] + skill[~i] != target:
                return -1
        return sum(skill[i] * skill[~i] for i in range(n // 2))
