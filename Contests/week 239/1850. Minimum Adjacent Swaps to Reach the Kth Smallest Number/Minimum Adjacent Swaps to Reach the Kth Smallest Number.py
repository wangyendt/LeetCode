#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Minimum Adjacent Swaps to Reach the Kth Smallest Number.py 
@time: 2021/05/02
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""


class Solution:
    def getMinSwaps(self, num: str, k: int) -> int:

        # 1: get the kth value
        # 2: count the steps to swap

        def get_swap_count(nums, nums0) -> int:
            count = 0
            for i in range(len(nums)):
                if nums[i] != nums0[i]:

                    index = i + 1
                    while nums0[index] != nums[i]:
                        index += 1

                    # print(i, index)
                    while index != i:
                        nums0[index], nums0[index - 1] = nums0[index - 1], nums0[index]
                        # print("after swap: ", ("").join(nums0))
                        count += 1
                        index -= 1
            return count

        def get_next_smart_num(nums) -> str:
            # find the rightest one to swap
            i = len(nums) - 2
            while i > 0 and int(nums[i]) >= int(nums[i + 1]):
                i -= 1

            # print("first digit need to swap: ", nums[i])

            j = len(nums) - 1
            while int(nums[j]) <= int(nums[i]):
                j -= 1

            # print("second digit need to swap with first one: ", nums[j])

            # swap i an j
            nums[i], nums[j] = nums[j], nums[i]
            # print("after swapped: ", ("").join(nums))

            # we need to sort all digit after i
            nums = nums[:i + 1] + sorted(nums[i + 1:])
            # print("after sorted: ", ("").join(nums))

            return nums

        # print("original: ", num)
        nums = [c for c in num]
        nums0 = [c for c in num]
        for i in range(k):
            nums = get_next_smart_num(nums)
            # print("{}-th smart num is: {}".format(i+1, ("").join(nums)))

        return get_swap_count(nums, nums0)
