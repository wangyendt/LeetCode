#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :    2020/4/18 22:40
@Author:  wang121ye
@File: Find the Minimum Number of Fibonacci Numbers Whose Sum Is K.py
@Software: PyCharm
"""


class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        def find_floor_fib(des):
            fib = [1, 1]
            while fib[-1] < des:
                fib.append(fib[-2] + fib[-1])
            return fib[-1] if fib[-1] <= des else fib[-2]

        ret = 0
        while k > 0:
            ret += 1
            k -= find_floor_fib(k)
        # print(find_floor_fib(1315152525))
        return ret


so = Solution()
print(so.findMinFibonacciNumbers(7))
print(so.findMinFibonacciNumbers(10))
print(so.findMinFibonacciNumbers(19))
