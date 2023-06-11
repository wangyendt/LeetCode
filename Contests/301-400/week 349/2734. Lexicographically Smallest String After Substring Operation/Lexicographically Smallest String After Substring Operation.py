"""
@author: wangye(Wayne)
@license: Apache Licence
@file: Lexicographically Smallest String After Substring Operation.py
@time: 20230611
@contact: wang121ye@hotmail.com
@site:  wangyendt@github.com
@software: PyCharm

# code is far away from bugs.
"""


class Solution:
    def smallestString(self, s: str) -> str:
        ret = []
        change = False
        if s[0] == 'a' and len(set(s)) == 1:
            return s[:-1] + 'z'
        for i, t in enumerate(s):
            if t == 'a':
                if change:
                    ret.extend(list(s[i:]))
                    break
                ret.append(t)
            else:
                ret.append(chr(ord(t) - 1))
                change = True
        return ''.join(ret)


so = Solution()
print(so.smallestString(s="cbabc"))
print(so.smallestString(s="acbbc"))
