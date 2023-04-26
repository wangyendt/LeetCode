"""
@author: wangye(Wayne)
@license: Apache Licence
@file: Calculate Delayed Arrival Time.py
@time: 20230423
@contact: wang121ye@hotmail.com
@site:  wangyendt@github.com
@software: PyCharm

# code is far away from bugs.
"""


class Solution:
    def findDelayedArrivalTime(self, arrivalTime: int, delayedTime: int) -> int:
        return (arrivalTime + delayedTime) % 24
