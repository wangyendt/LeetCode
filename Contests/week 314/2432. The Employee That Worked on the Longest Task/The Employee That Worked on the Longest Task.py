"""
@author: wangye(Wayne)
@license: Apache Licence
@file: The Employee That Worked on the Longest Task.py
@time: 20221009
@contact: wang121ye@hotmail.com
@site:  wangyendt@github.com
@software: PyCharm

# code is far away from bugs.
"""

from typing import *


class Solution:
    def hardestWorker(self, n: int, logs: List[List[int]]) -> int:
        ret_worker, max_working_time, pre_working_time = -1, 0, 0
        logs.insert(0, [-1, 0])
        for i, (log_id, log_leave_time) in enumerate(logs):
            if i:
                if log_leave_time - pre_working_time > max_working_time:
                    max_working_time = log_leave_time - pre_working_time
                    ret_worker = log_id
                elif log_leave_time - pre_working_time == max_working_time:
                    if log_id < ret_worker:
                        ret_worker = log_id
            pre_working_time = log_leave_time
        return ret_worker


so = Solution()
print(so.hardestWorker(70, [[36, 3], [1, 5], [12, 8], [25, 9], [53, 11], [29, 12], [52, 14]]))
