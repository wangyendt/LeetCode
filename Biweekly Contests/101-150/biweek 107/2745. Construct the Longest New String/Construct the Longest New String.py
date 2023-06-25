"""
@author: wangye(Wayne)
@license: Apache Licence
@file: Construct the Longest New String.py
@time: 20230625
@contact: wang121ye@hotmail.com
@site:  wangyendt@github.com
@software: PyCharm

# code is far away from bugs.
"""


class Solution:
    def longestString(self, x: int, y: int, z: int) -> int:
        return min(x + y + z, x + x + 1 + z, y + y + 1 + z) * 2
