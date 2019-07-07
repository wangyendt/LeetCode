#!/usr/bin/env python  
# -*- coding:utf-8 -*-  
""" 
@author:  wangye
@file: Defanging and IP Address.py 
@time: 2019/07/07
@contact: wangye.hope@gmail.com
@site:  
@software: PyCharm 
"""


class Solution:
    def defangIPaddr(self, address: str) -> str:
        return address.replace('.', '[.]')
