# !/usr/bin/env python
# -*- coding: utf-8 -*-
# author: wang121ye
# datetime: 2019/10/20 11:41
# software: PyCharm


class Solution:
    class Tree:
        def __init__(self, val, is_root=False):
            self.val = val
            self.is_root = is_root
            self.children = {}

        def is_sub_folder(self, arr):
            if not arr:
                return True
            else:
                if arr[0] in self.children:
                    return self.children[arr[0]].is_sub_folder(arr[1:])
                else:
                    if self.children or self.is_root:
                        return False
                    else:
                        return True

    def add(self, tree, arr):
        if arr:
            if arr[0] in tree.children:
                self.add(tree.children[arr[0]], arr[1:])
            else:
                tree.children[arr[0]] = self.Tree(arr[0])
                self.add(tree.children[arr[0]], arr[1:])

    def removeSubfolders(self, folder: list) -> list:
        ret = []
        tree = self.Tree('/', True)
        folder = sorted(folder, key=lambda x: len(x.strip('/').split('/')))
        for f in folder:
            f_arr = f.strip('/').split('/')
            if not tree.is_sub_folder(f_arr):
                ret.append(f)
                self.add(tree, f_arr)
        return ret


so = Solution()
print(so.removeSubfolders(["/a", "/a/b", "/c/d", "/c/d/e", "/c/f"]))
print(so.removeSubfolders(["/a", "/a/b/c", "/a/b/d"]))
print(so.removeSubfolders(["/a/b/c", "/a/b/ca", "/a/b/d"]))
print(so.removeSubfolders(["/ah/al/am", "/ah/al"]))
