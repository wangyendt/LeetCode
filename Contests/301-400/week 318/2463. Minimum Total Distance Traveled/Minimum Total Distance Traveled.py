#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Minimum Total Distance Traveled.py 
@time: 2022/11/06
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *


class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        robot.sort()
        factory.sort()

        # calculate the total limit for first k factories and store them in the array
        fac_prefix_sum = [0]
        for _, limit in factory:
            fac_prefix_sum.append(fac_prefix_sum[-1] + limit)

        # dp[i][j] is the minimumTotalDistance for assignning the first i robots to the first j factories
        # when num_robots == 0, total distance should be 0 anyway
        # when num_factories == 0, if there is any robot, we have no way to assign it, set value to -1.
        dp = [[0] * (len(factory) + 1)] + [[-1] + [None] * len(factory) for _ in range(len(robot))]

        def helper(num_robots, num_factories):
            if dp[num_robots][num_factories] is None:
                # when do not have enough limits to repair robot, set value to -1
                if fac_prefix_sum[num_factories] < num_robots:
                    dp[num_robots][num_factories] = -1
                else:
                    # get the position and limit of the right most factory
                    idx, limit = factory[num_factories - 1]
                    best = -1
                    # total distance for all robot going to the right most factory
                    cur_distance = 0

                    # loop through number of robots assginning to the right most factory, max number if min(limit, num_robots)
                    for i in range(min(num_robots, limit) + 1):
                        cur = helper(num_robots - i, num_factories - 1)
                        if cur >= 0:
                            cur += cur_distance
                            if best < 0 or cur < best:
                                best = cur
                        cur_distance += abs(robot[num_robots - 1 - i] - idx)
                    dp[num_robots][num_factories] = best
            return dp[num_robots][num_factories]

        return helper(len(robot), len(factory))
