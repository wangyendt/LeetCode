#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""=================================================
@Project -> File   ：LeetCode -> Filter Restaurants by Vegan-Friendly, Price and Distance
@IDE    ：PyCharm
@Author ：Wang Ye (Wayne)
@Date   ：2020/1/26 10:45
@Desc   ：
=================================================="""


class Solution:
    def filterRestaurants(self, restaurants: list(list()), veganFriendly: int, maxPrice: int, maxDistance: int) -> list:
        ret = []
        for rest in restaurants:
            if (veganFriendly == 1 and rest[2] == 1 or veganFriendly == 0) and \
                    rest[3] <= maxPrice and rest[4] <= maxDistance:
                ret.append((rest[0], rest[1]))
        return [r[0] for r in sorted(ret, key=lambda x: (-x[1], -x[0]))]


so = Solution()
print(so.filterRestaurants(
    restaurants=[[1, 4, 1, 40, 10], [2, 8, 0, 50, 5], [3, 8, 1, 30, 4], [4, 10, 0, 10, 3], [5, 1, 1, 15, 1]],
    veganFriendly=1, maxPrice=50, maxDistance=10))
print(so.filterRestaurants(
    restaurants=[[1, 4, 1, 40, 10], [2, 8, 0, 50, 5], [3, 8, 1, 30, 4], [4, 10, 0, 10, 3], [5, 1, 1, 15, 1]],
    veganFriendly=0, maxPrice=50, maxDistance=10))
print(so.filterRestaurants(
    restaurants=[[1, 4, 1, 40, 10], [2, 8, 0, 50, 5], [3, 8, 1, 30, 4], [4, 10, 0, 10, 3], [5, 1, 1, 15, 1]],
    veganFriendly=0, maxPrice=30, maxDistance=3))
