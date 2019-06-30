#!/usr/bin/env python  
# -*- coding:utf-8 -*-  
""" 
@author:  wangye
@file: Parsing A Boolean Expression.py 
@time: 2019/06/30
@contact: wangye.hope@gmail.com
@site:  
@software: PyCharm 
"""


class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        def _or(*args):
            return any(args)

        def _and(*args):
            return all(args)

        def _not(args):
            return not args

        return eval(expression.
                    replace('t', 'True').replace('f', 'False').
                    replace('|', '_or').replace('&', '_and').replace('!', '_not')
                    )


so = Solution()
print(so.parseBoolExpr('|(&(t,f,t),!(t))'))
