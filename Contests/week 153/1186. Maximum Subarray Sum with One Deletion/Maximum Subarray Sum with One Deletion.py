# !/usr/bin/env python
# -*- coding: utf-8 -*-
# author: wang121ye
# datetime: 2019/9/8 11:43
# software: PyCharm


class Solution:
    def maximumSum(self, arr: list) -> int:
        n = len(arr)
        fw, bw = [0] * n, [0] * n
        cur_max = max_so_far = fw[0] = arr[0]
        for i in range(1, n):
            cur_max = max(arr[i], cur_max + arr[i])
            max_so_far = max(max_so_far, cur_max)
            fw[i] = cur_max

        cur_max = max_so_far = bw[- 1] = arr[- 1]
        for i in range(n - 2, -1, -1):
            cur_max = max(arr[i], cur_max + arr[i])
            max_so_far = max(max_so_far, cur_max)
            bw[i] = cur_max

        ret = max_so_far
        for i in range(1, n - 1):
            ret = max(ret, fw[i - 1] + bw[i + 1])

        return ret


so = Solution()
print(so.maximumSum([1, -2, 0, 3]))
print(so.maximumSum([1, -2, -2, 3]))
print(so.maximumSum([-1, -1, -1, -1]))
print(so.maximumSum([8, -1, 6, -7, -4, 5, -4, 7, -6]), 17)
