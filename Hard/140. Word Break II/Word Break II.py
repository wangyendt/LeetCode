# !/usr/bin/env python
# -*- coding: utf-8 -*-
# author: wang121ye
# datetime: 2019/7/8 17:03
# software: PyCharm

class Solution:
    def wordBreak(self, s, wordDict):
        res = []
        self.dfs(s, wordDict, '', res)
        return res

    def dfs(self, s, dic, path, res):
        if self.check(s, dic):
            if not s:
                res.append(path[:-1])
                return  # backtracking
            for i in range(1, len(s) + 1):
                if s[:i] in dic:
                    # dic.remove(s[:i])
                    self.dfs(s[i:], dic, path + s[:i] + " ", res)

    def check(self, s, dic):
        dp = [False for i in range(len(s) + 1)]
        dp[0] = True
        for i in range(1, len(s) + 1):
            for j in range(i):
                if dp[j] and s[j:i] in dic:
                    dp[i] = True
        return dp[-1]


so = Solution()
# print(so.wordBreak("catsanddog", ["cat", "cats", "and", "sand", "dog"]))
print(so.wordBreak(
    "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
    ["a", "aa", "aaa", "aaaa", "aaaaa", "aaaaaa", "aaaaaaa", "aaaaaaaa", "aaaaaaaaa", "aaaaaaaaaa"]))
