"""
@author: wangye(Wayne)
@license: Apache Licence
@file: Minimum Additions to Make Valid String.py
@time: 20230416
@contact: wang121ye@hotmail.com
@site:  wangyendt@github.com
@software: PyCharm

# code is far away from bugs.
"""


class Solution:
    def addMinimum(self, word: str) -> int:
        k, prev = 0, 'z'
        for c in word:
            k += c <= prev
            prev = c
        return k * 3 - len(word)


so = Solution()
print(so.addMinimum(word="ccababbaccbbca"))
print(so.addMinimum("aaaaab"))
