# !/usr/bin/env python
# -*- coding: utf-8 -*-
# author: wang121ye
# datetime: 2019/7/16 19:38
# software: PyCharm

class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join([l[::-1] for l in s.split(' ')])


so = Solution()
print(so.reverseWords('Let\'s take LeetCode contest'))
