#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Delete Duplicate Folders in System.py 
@time: 2021/07/27
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *
import collections


class Solution:
    def deleteDuplicateFolder(self, paths: List[List[str]]) -> List[List[str]]:
        tree = {}
        child_hashes = collections.defaultdict(list)

        # build directories tree
        for path in paths:
            node = tree
            for folder in path:
                if folder not in node:
                    node[folder] = {}
                node = node[folder]

            # iterate all children in sorted order and hash them as tuple,
            # then add current node key to hash and return

        def dfs(node, node_key, parent):
            child_tuple = tuple(dfs(node[key], key, node) for key in sorted(node.keys()))
            child_hash = hash(child_tuple)
            if child_tuple:
                child_hashes[child_hash].append((parent, node_key))
            return hash((child_hash, node_key))

        dfs(tree, None, None)

        # find all subtree with the same hash and delete them from the tree
        for duplicates in child_hashes.values():
            if len(duplicates) > 1:
                for parent, node_key in duplicates:
                    del parent[node_key]

            # simple dfs to collect all "root -> ... -> leaf" paths

        def dfs_collect_paths(node, current, res):
            for key in node.keys():
                res.append(current + [key])
                dfs_collect_paths(node[key], current + [key], res)
            return res

        return dfs_collect_paths(tree, [], [])
