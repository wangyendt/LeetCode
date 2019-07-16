# !/usr/bin/env python
# -*- coding: utf-8 -*-
# author: wang121ye
# datetime: 2019/7/16 10:33
# software: PyCharm

class Solution:
    def findWords(self, words: list) -> list:
        ret = []
        group = ['qwertyuiopQWERTYUIOP', 'asdfghjklASDFGHJKL', 'zxcvbnmZXCVBNM']
        dic = {}
        for i in range(len(group)):
            for w in group[i]:
                dic[w] = i
        for w in words:
            if w:
                w_ = w[:]
                w = list(set(w))
                for ww in w:
                    if dic[ww] != dic[w[0]]:
                        break
                else:
                    ret.append(w_)
        return ret


so = Solution()
print(so.findWords(["Hello", "Alaska", "Dad", "Peace"]))
