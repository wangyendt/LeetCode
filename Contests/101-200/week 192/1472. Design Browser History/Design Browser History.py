#!/usr/bin/env python
# encoding: utf-8

"""
@author: Wayne
@contact: wangye.hope@gmail.com
@software: PyCharm
@file: Design Browser History
@time: 2020/06/07 10:42
"""


class BrowserHistory:

    def __init__(self, homepage: str):
        self.stack = []
        self.cur = 0
        self.visit(homepage)

    def visit(self, url: str) -> None:
        self.stack = self.stack[:self.cur+1]
        self.stack.append(url)
        self.cur = len(self.stack)-1

    def back(self, steps: int) -> str:
        self.cur -= min(self.cur, steps)
        return self.stack[self.cur]

    def forward(self, steps: int) -> str:
        self.cur += min(len(self.stack)-1-self.cur, steps)
        return self.stack[self.cur]

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)