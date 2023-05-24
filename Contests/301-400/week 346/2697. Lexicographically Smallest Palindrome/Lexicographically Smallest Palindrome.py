"""
@author: wangye(Wayne)
@license: Apache Licence
@file: Lexicographically Smallest Palindrome.py
@time: 20230524
@contact: wang121ye@hotmail.com
@site:  wangyendt@github.com
@software: PyCharm

# code is far away from bugs.
"""


class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        mid = ''
        if len(s) % 2 == 1:
            mid = s[len(s) // 2]
            s_list = list(s[:len(s) // 2]) + list(s[len(s) // 2 + 1:])
        else:
            s_list = list(s)
        for i in range(len(s) // 2 - 1, -1, -1):
            if s[i] != s[~i]:
                s_list[i] = s_list[~i] = min(s[i], s[~i])
        if mid:
            s_list.insert(len(s_list) // 2, mid)
        return ''.join(s_list)


so = Solution()
print(so.makeSmallestPalindrome(s="egcfe"))
print(so.makeSmallestPalindrome(s="abcd"))
