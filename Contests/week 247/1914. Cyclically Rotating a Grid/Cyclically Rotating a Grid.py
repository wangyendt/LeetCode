#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Cyclically Rotating a Grid.py 
@time: 2021/06/27
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *


class Solution:
    def rotateGrid(self, A: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(A), len(A[0])
        # print(m, n)
        for c in range(min(m, n) // 2):
            # tl = (c, c)
            # bl = (m - 1 - c, c)
            # br = (m - 1 - c, n - 1 - c)
            # tr = (c, n - 1 - c)
            h, w = m - 2 * c, n - 2 * c
            kk = k % ((h + w - 2) * 2)
            for kkk in range(kk):
                res = A[c][c]
                for j in range(c, n - 1 - c):
                    A[c][j] = A[c][j + 1]
                for i in range(c, m - 1 - c):
                    A[i][n - 1 - c] = A[i + 1][n - 1 - c]
                for j in range(n - 1 - c, c, -1):
                    A[m - 1 - c][j] = A[m - 1 - c][j - 1]
                for i in range(m - 1 - c, c, -1):
                    A[i][c] = A[i - 1][c]
                A[c + 1][c] = res
        return A


so = Solution()
print(so.rotateGrid(A=[[40, 10], [30, 20]], k=1))
print(so.rotateGrid([[3970, 1906, 3608, 298, 3072, 3546, 1502, 773, 4388, 3115, 747, 3937],
                     [2822, 304, 4179, 1780, 1709, 1058, 3645, 681, 2910, 2513, 4357, 1038],
                     [4471, 2443, 218, 550, 2766, 4780, 1997, 1672, 4095, 161, 4645, 3838],
                     [2035, 2350, 3653, 4127, 3208, 4717, 4347, 3452, 1601, 3725, 3060, 2270],
                     [188, 2278, 81, 3454, 3204, 1897, 2862, 4381, 3704, 2587, 743, 3832],
                     [996, 4499, 66, 2742, 1761, 1189, 608, 509, 2344, 3271, 3076, 108],
                     [3274, 2042, 2157, 3226, 2938, 3766, 2610, 4510, 219, 1276, 3712, 4143],
                     [744, 234, 2159, 4478, 4161, 4549, 4214, 4272, 701, 4376, 3110, 4896],
                     [4431, 1011, 757, 2690, 83, 3546, 946, 1122, 2216, 3944, 2715, 2842],
                     [898, 4087, 703, 4153, 3297, 2968, 3268, 4717, 1922, 2527, 3139, 1516],
                     [1086, 1090, 302, 1273, 2292, 234, 3268, 2284, 4203, 3838, 2227, 3651],
                     [2055, 4406, 2278, 3351, 3217, 2506, 4525, 233, 3829, 63, 4470, 3170],
                     [3797, 3276, 1755, 1727, 1131, 4108, 3633, 1835, 1345, 1293, 2778, 2805],
                     [1215, 84, 282, 2721, 2360, 2321, 1435, 2617, 1202, 2876, 3420, 3034]], 405548684))

o1 = [[188, 2035, 4471, 2822, 3970, 1906, 3608, 298, 3072, 3546, 1502, 773],
      [996, 1058, 3645, 681, 2910, 2513, 4357, 4645, 3060, 743, 3076, 4388],
      [3274, 1709, 1997, 1672, 4095, 161, 3725, 2587, 3271, 1276, 3712, 3115],
      [744, 1780, 4780, 3452, 1601, 3704, 2344, 219, 701, 4376, 3110, 747],
      [4431, 4179, 2766, 4347, 509, 4510, 4272, 1122, 2216, 3944, 2715, 3937],
      [898, 304, 550, 4717, 4381, 946, 3546, 4717, 1922, 2527, 3139, 1038],
      [1086, 2443, 218, 3208, 2862, 4214, 4549, 3268, 4203, 3838, 2227, 3838],
      [2055, 2350, 3653, 4127, 1897, 2610, 3766, 2968, 2284, 63, 4470, 2270],
      [3797, 2278, 81, 3454, 3204, 608, 1189, 3297, 3268, 3829, 2778, 3832],
      [1215, 4499, 66, 2742, 1761, 2938, 4161, 83, 234, 233, 1293, 108],
      [84, 2042, 2157, 3226, 4478, 2690, 4153, 1273, 2292, 4525, 1345, 4143],
      [282, 234, 2159, 757, 703, 302, 2278, 3351, 3217, 2506, 1835, 4896],
      [2721, 1011, 4087, 1090, 4406, 3276, 1755, 1727, 1131, 4108, 3633, 2842],
      [2360, 2321, 1435, 2617, 1202, 2876, 3420, 3034, 2805, 3170, 3651, 1516]]

o2 = [[188, 2035, 4471, 2822, 3970, 1906, 3608, 298, 3072, 3546, 1502, 773],
      [996, 1058, 3645, 681, 2910, 2513, 4357, 4645, 3060, 743, 3076, 4388],
      [3274, 1709, 4376, 3944, 2527, 3838, 63, 3829, 233, 4525, 3712, 3115],
      [744, 1780, 1276, 4478, 3226, 2742, 3454, 4127, 3208, 2506, 3110, 747],
      [4431, 4179, 3271, 2690, 83, 4161, 2938, 1761, 4717, 3217, 2715, 3937],
      [898, 304, 2587, 4153, 3297, 946, 3546, 3204, 4347, 3351, 3139, 1038],
      [1086, 2443, 3725, 1273, 2968, 4214, 4549, 1897, 3452, 2278, 2227, 3838],
      [2055, 2350, 161, 2292, 3268, 2610, 3766, 2862, 1601, 302, 4470, 2270],
      [3797, 2278, 4095, 234, 4717, 608, 1189, 4381, 3704, 703, 2778, 3832],
      [1215, 4499, 1672, 3268, 1122, 4272, 4510, 509, 2344, 757, 1293, 108],
      [84, 2042, 1997, 2284, 4203, 1922, 2216, 701, 219, 2159, 1345, 4143],
      [282, 234, 4780, 2766, 550, 218, 3653, 81, 66, 2157, 1835, 4896],
      [2721, 1011, 4087, 1090, 4406, 3276, 1755, 1727, 1131, 4108, 3633, 2842],
      [2360, 2321, 1435, 2617, 1202, 2876, 3420, 3034, 2805, 3170, 3651, 1516]]
