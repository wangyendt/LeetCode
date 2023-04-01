# !/usr/bin/env python
# -*- coding: utf-8 -*-
# author: wang121ye
# datetime: 2019/10/20 11:31
# software: PyCharm


class Solution:
    def checkStraightLine(self, coordinates: list(list())) -> bool:
        for i in range(1, len(coordinates)):
            dx, dy = coordinates[i][0] - coordinates[i - 1][0], coordinates[i][1] - coordinates[i - 1][1]
            if i > 1 and ((dx * dx_ + dy * dy_) ** 2 != (dx ** 2 + dy ** 2) * (dx_ ** 2 + dy_ ** 2)):
                return False
            dx_, dy_ = dx, dy
        return True


so = Solution()
print(so.checkStraightLine([[1, 1], [2, 2], [3, 4], [4, 5], [5, 6], [7, 7]]))
print(so.checkStraightLine([[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]]))
print(so.checkStraightLine([[-3, -2], [-1, -2], [2, -2], [-2, -2], [0, -2]]))
