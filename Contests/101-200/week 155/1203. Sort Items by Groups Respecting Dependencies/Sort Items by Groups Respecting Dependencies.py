# !/usr/bin/env python
# -*- coding: utf-8 -*-
# author: wang121ye
# datetime: 2019/9/29 21:55
# software: PyCharm


import collections


class Solution:
    def sortItems(self, n: int, m: int, group: list, beforeItems: list(list())) -> list:
        def topo_sort(nodes, in_ds, out_ds):
            q = [n for n in nodes if not in_ds[n]]
            res = []
            while q:
                n = q.pop()
                res += [n]
                for e in out_ds[n]:
                    in_ds[e].remove(n)
                    if not in_ds[e]:
                        q += [e]
            return res if len(res) == len(nodes) else []

        g2i = collections.defaultdict(set)
        for i in range(n):
            if group[i] == -1:
                group[i] = m
                m += 1
            g2i[group[i]].add(i)

        in_ds_g, out_ds_g = collections.defaultdict(set), collections.defaultdict(set)
        in_ds_i, out_ds_i = collections.defaultdict(set), collections.defaultdict(set)

        for i in range(n):
            for j in beforeItems[i]:
                if group[i] == group[j]:
                    in_ds_i[i].add(j)
                    out_ds_i[j].add(i)
                else:
                    in_ds_g[group[i]].add(group[j])
                    out_ds_g[group[j]].add(group[i])

        sorted_group = topo_sort([k for k in g2i], in_ds_g, out_ds_g)
        if not sorted_group:
            return []

        res = []
        for g in sorted_group:
            sorted_items = topo_sort(g2i[g], in_ds_i, out_ds_i)
            if not sorted_items:
                return []
            res += sorted_items
        return res
