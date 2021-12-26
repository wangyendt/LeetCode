#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Find All Possible Recipes from Given Supplies.py 
@time: 2021/12/26
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *
import collections


class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        indeg = collections.defaultdict(int)
        graph = collections.defaultdict(list)
        for r, ing in zip(recipes, ingredients):
            indeg[r] = len(ing)
            for i in ing: graph[i].append(r)

        ans = []
        queue = collections.deque(supplies)
        recipes = set(recipes)
        while queue:
            x = queue.popleft()
            if x in recipes: ans.append(x)
            for xx in graph[x]:
                indeg[xx] -= 1
                if indeg[xx] == 0: queue.append(xx)
        return ans
