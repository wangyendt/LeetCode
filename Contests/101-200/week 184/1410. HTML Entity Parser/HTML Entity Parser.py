#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :    2020/4/12 10:43
@Author:  wang121ye
@File: HTML Entity Parser.py
@Software: PyCharm
"""


class Solution:
    def entityParser(self, text: str) -> str:
        return text.replace('&quot;', '"').replace(
            '&apos;', '\'').replace('&amp;', '&').replace(
            '&gt;', '>').replace('&lt;', '<').replace('&frasl;', '/')


so = Solution()
print(so.entityParser(text="&amp; is an HTML entity but &ambassador; is not."))
print(so.entityParser(text="and I quote: &quot;...&quot;"))
print(so.entityParser(text="Stay home! Practice on Leetcode :)"))
print(so.entityParser(text="x &gt; y &amp;&amp; x &lt; y is always false"))
print(so.entityParser(text="leetcode.com&frasl;problemset&frasl;all"))
