"""
@author: wangye(Wayne)
@license: Apache Licence
@file: Minimum String Length After Removing Substrings.py
@time: 20230524
@contact: wang121ye@hotmail.com
@site:  wangyendt@github.com
@software: PyCharm

# code is far away from bugs.
"""


class Solution:
    def minLength(self, s: str) -> int:
        s_pre = s_cur = s
        while True:
            s_cur = s_cur.replace("AB", "")
            s_cur = s_cur.replace("CD", "")
            if len(s_cur) == len(s_pre):
                break
            s_pre = s_cur
        return len(s_cur)
