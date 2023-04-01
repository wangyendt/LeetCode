#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Design Memory Allocator.py 
@time: 2022/12/11
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

import collections


class Allocator:

    def __init__(self, n: int):
        self.n = n
        self.A = [0] * n
        self.free_num = [0] * (n + 1)
        for i in range(n):
            self.free_num[i] = n - i

    def allocate(self, size: int, mID: int) -> int:
        ret = -1
        # print(f'{size=},{mID=},{self.free_num=}')
        for i in range(self.n):
            if self.free_num[i] >= size:
                self.A[i:i + size] = [mID] * size
                self.free_num[i:i + size] = [0] * size
                ret = i
                break
        return ret

    def free(self, mID: int) -> int:
        cnt = 0
        # print(f'before free: {self.free_num=}, {self.A=},{mID=}')
        for i in range(self.n - 1, -1, -1):
            if self.A[i] == mID:
                self.A[i] = 0
                # if i < self.n - 1:
                # self.free_num[i] = self.free_num[i + 1] + 1
                for j in range(i, -1, -1):
                    if self.free_num[j] == 0 and j != i:
                        break
                    self.free_num[j] = self.free_num[j + 1] + 1
                cnt += 1
        # print(f'after free: {self.free_num=}, {self.A=},{mID=}')
        return cnt


import sys

sys.path.append('../..')
from Tools.API_utils import *

# call_me(Allocator, ["Allocator", "allocate", "allocate", "allocate", "free", "allocate", "allocate", "allocate", "free", "allocate", "free"],
#         [[10], [1, 1], [1, 2], [1, 3], [2], [3, 4], [1, 1], [1, 1], [1], [10, 2], [7]])
# call_me(Allocator, ["Allocator", "allocate", "allocate", "allocate", "free", "free", "allocate", "free", "allocate"],
#         [[7], [7, 8], [8, 7], [6, 2], [9], [8], [7, 6], [9], [10, 9]])
call_me(Allocator,
        ["Allocator", "allocate", "allocate", "allocate", "allocate", "free", "free", "free", "allocate", "allocate", "allocate", "allocate", "free", "free", "free", "free", "free", "free", "free", "allocate", "free", "free", "allocate", "free", "allocate", "allocate", "free", "free", "free", "allocate", "allocate", "allocate", "allocate", "free", "allocate", "free", "free", "allocate", "allocate", "allocate", "allocate", "allocate", "allocate", "allocate", "free", "free",
         "free", "free"],
        [[50], [12, 6], [28, 16], [17, 23], [50, 23], [6], [10], [10], [16, 8], [17, 41], [44, 27], [12, 45], [33], [8], [16], [23], [23], [23], [29], [38, 32], [29], [6], [40, 11], [16], [22, 33], [27, 5], [3], [10], [29], [16, 14], [46, 47], [48, 9], [36, 17], [33], [14, 24], [16], [8], [2, 50], [31, 36], [17, 45], [46, 31], [2, 6], [16, 2], [39, 30], [33], [45], [30], [27]])
