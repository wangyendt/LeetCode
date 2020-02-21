#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""=================================================
@Project -> File   ：LeetCode -> Tweet Counts Per Frequency
@IDE    ：PyCharm
@Author ：Wang Ye (Wayne)
@Date   ：2020/2/21 18:28
@Desc   ：
=================================================="""

import collections


class TweetCounts:

    def __init__(self):
        self.a = collections.defaultdict(list)

    def recordTweet(self, name: str, time: int):
        self.a[name].append(time)

    def getTweetCountsPerFrequency(self, freq: str, name: str, startTime: int, endTime: int) -> list:
        row = self.a[name]
        row.sort()
        i = bisect.bisect_left(row, startTime)
        i -= 2
        if i < 0: i = 0

        if freq == 'minute':
            fv = 60
        elif freq == 'hour':
            fv = 60 * 60
        else:
            fv = 24 * 60 * 60

        Q, _ = divmod(endTime - startTime, fv)
        Q += 1
        ans = [0] * Q
        for i in range(i, len(row)):
            t = row[i]
            if t > endTime: break
            if t >= startTime:
                d = t - startTime
                q, r = divmod(d, fv)
                ans[q] += 1
        return ans

# Your TweetCounts object will be instantiated and called as such:
# obj = TweetCounts()
# obj.recordTweet(tweetName,time)
# param_2 = obj.getTweetCountsPerFrequency(freq,tweetName,startTime,endTime)
