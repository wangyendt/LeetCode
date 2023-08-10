# author: wangye(Wayne)
# license: Apache Licence
# file: Number of Black Blocks.py
# time: 2023-08-10-10:19:33
# contact: wang121ye@hotmail.com
# site:  wangyendt@github.com
# software: PyCharm
# code is far away from bugs.


import collections
from typing import *


class Solution:
    def countBlackBlocks(self, m: int, n: int, coordinates: List[List[int]]) -> List[int]:
        dict1 = collections.defaultdict(int)
        for i, j in coordinates:
            for x in range(i - 1, i + 1):
                for y in range(j - 1, j + 1):
                    if 0 <= x < m - 1 and 0 <= y < n - 1:
                        dict1[(x, y)] += 1
        dict2 = collections.Counter(dict1.values())
        return [(m - 1) * (n - 1) - sum(dict2.values()), dict2[1], dict2[2], dict2[3], dict2[4]]
