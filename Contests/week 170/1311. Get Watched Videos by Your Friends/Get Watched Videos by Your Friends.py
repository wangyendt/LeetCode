#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""=================================================
@Project -> File   ：LeetCode -> Get Watched Videos by Your Friends
@IDE    ：PyCharm
@Author ：Wang Ye (Wayne)
@Date   ：2020/1/7 18:08
@Desc   ：
=================================================="""

import collections


class Solution:
    def watchedVideosByFriends(self, watchedVideos: list(list()), friends: list(list()), id: int, level: int) -> list:
        bfs, visited = {id}, {id}
        for _ in range(level):
            bfs = {j for i in bfs for j in friends[i] if j not in visited}
            visited |= bfs
        freq = collections.Counter([v for idx in bfs for v in watchedVideos[idx]])
        return sorted(freq.keys(), key=lambda x: (freq[x], x))
