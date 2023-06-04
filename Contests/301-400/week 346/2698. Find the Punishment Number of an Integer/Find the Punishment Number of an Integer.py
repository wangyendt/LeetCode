"""
@author: wangye(Wayne)
@license: Apache Licence
@file: Find the Punishment Number of an Integer.py
@time: 20230524
@contact: wang121ye@hotmail.com
@site:  wangyendt@github.com
@software: PyCharm

# code is far away from bugs.
"""


class Solution:
    def punishmentNumber(self, n: int) -> int:
        # This is a method to check if s is possible to make s with su and cache_sum
        def possible(sum_added, cache_sum, n, target):
            # We have two choices, either to use the first character of n or combine it with the sum that we have
            if not n:
                return target == sum_added + cache_sum
            num = int(n[0])
            cas = cache_sum
            # This is case when we add the first number to already present sum: possible(sum_added,cas*10+num, n[1:], target)
            # Case when we add this as a digit, so we add cache_sum to already present sum: possible(sum_added+cas,num, n[1:], target)
            return possible(sum_added, cas * 10 + num, n[1:], target) or possible(sum_added + cas, num, n[1:], target)

        # print(possible(0,0 ,str(81), 9))
        ans = 0
        for i in range(1, n + 1):
            # We see how many are possible
            if possible(0, 0, str(i * i), i):
                ans += i * i
        return ans
