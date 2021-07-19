# !/usr/bin/env python
# -*- coding:utf-8 -*-
""" 
@author: Wang Ye (Wayne)
@file: Maximum Genetic Difference Query.py
@time: 2021/07/19
@contact: wangye@oppo.com
@site: 
@software: PyCharm
# code is far away from bugs.
"""

from typing import *
import collections


class Trie:
    def __init__(self, *words):
        self.root = dict()
        for word in words:
            self.add(word)

    def add(self, word):
        current_dict = self.root
        for letter in word:
            current_dict = current_dict.setdefault(letter, dict())
        current_dict["_end_"] = True

    def __contains__(self, word):
        current_dict = self.root
        for letter in word:
            if letter not in current_dict:
                return False
            current_dict = current_dict[letter]
        return "_end_" in current_dict

    def find(self, word):
        current_dict = self.root
        res = ""
        for letter in word:
            # try to match "1" to "0" and vice versa
            desired = "1" if letter == "0" else "0"

            if not desired in current_dict:  # if not possible to match
                desired = letter  # settle for the same letter
            res += desired
            current_dict = current_dict[desired]  # advance to the next node in the trie
        return res

    def delete(self, word):
        current_dict = self.root
        nodes = [current_dict]
        objects = []
        for letter in word:
            current_dict = current_dict[letter]
            nodes.append(current_dict)
            objects.append(current_dict)

        del current_dict["_end_"]

        for c, obj in zip(word[::-1], objects[:-1][::-1]):
            if not obj[c]:
                del obj[c]
            else:
                break

        # assert word not in self  # confirm that the number has been removed


class Solution:
    def maxGeneticDifference(self, parents: List[int], queries: List[List[int]]) -> List[int]:
        # maintain a trie while doing dfs

        def makebin(x):
            # convert to binary and prepend zeroes until there are 20 characters
            # we need all binary strings to be of the same length
            return bin(x)[2:].zfill(20)

        query_node_to_query_list = collections.defaultdict(list)
        for i, (node, val) in enumerate(queries):
            query_node_to_query_list[node].append((i, val))

        graph = collections.defaultdict(list)
        for i, x in enumerate(parents):
            graph[x].append(i)

        res = [-1 for _ in queries]
        t = Trie()

        def dfs(node):
            nodestr = makebin(node)
            t.add(nodestr)

            for i, val in query_node_to_query_list[node]:
                valstr = makebin(val)
                targetstr = t.find(valstr)  # find the best target value in the trie
                res[i] = int(targetstr, 2) ^ val  # store the result

            for nex in graph[node]:
                dfs(nex)  # continue with dfs

            t.delete(nodestr)

        dfs(graph[-1][0])  # solve from root

        return res
