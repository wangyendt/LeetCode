"""
@author: wangye(Wayne)
@license: Apache Licence
@file: Partition String Into Substrings With Values at Most K.py
@time: 20230103
@contact: wang121ye@hotmail.com
@site:  wangyendt@github.com
@software: PyCharm

# code is far away from bugs.
"""


class Solution:
    def minimumPartition(self, s: str, k: int) -> int:
        curr, ret = 0, 1
        for d in s:
            if int(d) > k:
                return -1
            curr = 10 * curr + int(d)
            if curr > k:
                ret += 1
                curr = int(d)
        return ret
