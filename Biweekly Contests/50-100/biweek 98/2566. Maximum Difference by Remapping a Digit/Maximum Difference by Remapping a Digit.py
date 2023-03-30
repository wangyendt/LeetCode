"""
@author: wangye(Wayne)
@license: Apache Licence
@file: Maximum Difference by Remapping a Digit.py
@time: 20230330
@contact: wang121ye@hotmail.com
@site:  wangyendt@github.com
@software: PyCharm

# code is far away from bugs.
"""


class Solution:
    def minMaxDifference(self, num: int) -> int:
        s = str(num)
        mx = int(s.replace(s[0], '9'))
        for i in range(10):
            if str(i) in s:
                mx = max(mx, int(s.replace(str(i), '9')))
        mn = s.replace(s[0], '0')
        return int(mx) - int(mn)


so = Solution()
print(so.minMaxDifference(num=867))
