"""
@author: wangye(Wayne)
@license: Apache Licence
@file: Sort the People.py
@time: 20220930
@contact: wang121ye@hotmail.com
@site:  wangyendt@github.com
@software: PyCharm

# code is far away from bugs.
"""

from typing import *


class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        return [names[i] for i in sorted(range(len(names)), key=lambda x: -heights[x])]
