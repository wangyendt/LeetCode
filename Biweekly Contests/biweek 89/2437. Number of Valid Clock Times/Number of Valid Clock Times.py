#!/usr/bin/env python  
# -*- coding:utf-8 _*-  
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Number of Valid Clock Times.py 
@time: 2022/10/15
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""


class Solution:
    def countTime(self, time: str) -> int:
        def judge(time_str):
            # print(time_str)
            if int(time_str[-2]) >= 6: return False
            if int(time_str[0]) == 2:
                if int(time_str[1]) >= 4:
                    return False
            if int(time_str[0]) > 2:
                return False
            return True

        def helper(ts, digit):
            if '?' not in ts:
                if judge(ts):
                    return 1
                else:
                    return 0
            ret = 0
            if ts[digit - 1] == '?':
                for i in range(10):
                    ret += helper(ts[:digit - 1] + str(i) + ts[digit:], digit + 1)
            else:
                return helper(ts, digit + 1)
            return ret

        return helper(time, 1)

        # res = 0
        # if time[0] == '?':
        #     for i in range(10):
        #         if time[1] == '?':
        #             for j in range(10):
        #                 if time[3] == '?':
        #                     for k in range(10):
        #                         if time[4] == '?':
        #                             for l in range(10):
        #                                 if judge(f'{i}{j}:{k}{l}'):
        #                                     res += 1
        # return res


so = Solution()
print(so.countTime(time="?5:00"))
print(so.countTime(time="0?:0?"))
