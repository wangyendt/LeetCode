"""
@author: wangye(Wayne)
@license: Apache Licence
@file: Words Within Two Edits of Dictionary.py
@time: 20221030
@contact: wang121ye@hotmail.com
@site:  wangyendt@github.com
@software: PyCharm

# code is far away from bugs.
"""

from typing import *


class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        def diff(w1, w2):
            ret = 0
            for l1, l2 in zip(w1, w2):
                if l1 != l2:
                    ret += 1
                    if ret > 2:
                        return ret
            return ret

        ret = []
        for i in range(len(queries)):
            for j in range(len(dictionary)):
                if diff(queries[i], dictionary[j]) <= 2:
                    ret.append(queries[i])
                    break
        return ret


so = Solution()
print(so.twoEditWords(["tsl", "sri", "yyy", "rbc", "dda", "qus", "hyb", "ilu", "ahd"],
                      ["uyj", "bug", "dba", "xbe", "blu", "wuo", "tsf", "tga"]))
