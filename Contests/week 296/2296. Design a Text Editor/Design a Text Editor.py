#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Design a Text Editor.py 
@time: 2022/06/05
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""


class TextEditor:

    def __init__(self):
        self.text = []
        self.cur = 0

    def addText(self, text: str) -> None:
        self.text[self.cur:self.cur] = list(text)
        self.cur += len(text)

    def deleteText(self, k: int) -> int:
        ret = self.cur - max(0, self.cur - k)
        self.text[max(0, self.cur - k):self.cur] = []
        self.cur = max(0, self.cur - k)
        return ret

    def cursorLeft(self, k: int) -> str:
        self.cur = max(0, self.cur - k)
        return ''.join(self.text[max(0, self.cur - 10):self.cur])

    def cursorRight(self, k: int) -> str:
        self.cur = min(len(self.text), self.cur + k)
        return ''.join(self.text[max(0, self.cur - 10):self.cur])
