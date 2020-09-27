# !/usr/bin/env python
# -*- coding:utf-8 -*-
""" 
@author: Wang Ye (Wayne)
@file: Crawler Log Folder.py
@time: 2020/09/27
@contact: wangye@oppo.com
@site: 
@software: PyCharm
# code is far away from bugs.
"""

from typing import *


class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = []
        for log in logs:
            if log == '../':
                if stack:
                    stack.pop()
            elif log == './':
                continue
            else:
                stack.append(log)
        return len(stack)
