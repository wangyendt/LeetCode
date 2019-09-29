# !/usr/bin/env python
# -*- coding: utf-8 -*-
# author: wang121ye
# datetime: 2019/9/24 22:21
# software: PyCharm


class Solution:
    """
    老板给度度熊n个数，每一次从a[i]中取出一个最大的减去n，其他的n-1个数加上1，一直重复到
    最大的a[i]<n，执行次数为k
    老板想知道最少执行多少次操作使得n个数都小于n呢
    2<=n<=50
    1<=a[i]<=10^18
    """

    def get_min_k_less_than_n(self, A):
        n = len(A)


if __name__ == '__main__':
    so = Solution()
    print(so.get_min_k_less_than_n([2,3,4]))
