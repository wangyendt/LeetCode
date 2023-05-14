"""
@author: wangye(Wayne)
@license: Apache Licence
@file: Neighboring Bitwise XOR.py
@time: 20230514
@contact: wang121ye@hotmail.com
@site:  wangyendt@github.com
@software: PyCharm

# code is far away from bugs.
"""

from typing import *


class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        origin = [0]
        for d in derived[:-1]:
            origin.append(origin[-1] ^ d)
        # print(origin)
        if origin[0] ^ origin[-1] == derived[-1]:
            return True
        return False


so = Solution()
print(so.doesValidArrayExist(derived=[1, 1]))
