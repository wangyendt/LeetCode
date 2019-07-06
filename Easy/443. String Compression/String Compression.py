# !/usr/bin/env python
# -*- coding: utf-8 -*-
# author: wang121ye
# datetime: 2019/7/6 16:13
# software: PyCharm
from itertools import groupby


class Solution:
    def compress(self, chars):
        i = 0
        for x, gx in groupby(chars):
            chars[i] = x
            i += 1
            n = 0
            for _ in gx:
                n += 1
            if n > 1:
                for x in str(n):
                    chars[i] = x
                    i += 1
        return i
