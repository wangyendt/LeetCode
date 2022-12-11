#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Maximum Value of a String in an Array.py 
@time: 2022/12/11
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *
import re


class Solution:
    def maximumValue(self, strs: List[str]) -> int:
        # def maximumValue(strs):
        # Compile a regular expression that matches strings consisting only of digits
        digitRegex = re.compile(r'^\d+$')

        # Initialize the maximum value to 0
        maxValue = 0

        # Loop through the array of strings
        for s in strs:
            # Check if the string consists only of digits using the regular expression
            if digitRegex.match(s):
                # If the string consists only of digits, compute its numeric value in base 10
                value = int(s)
            else:
                # Otherwise, the value of the string is its length
                value = len(s)

            # Update the maximum value if necessary
            maxValue = max(maxValue, value)

        # Return the maximum value
        return maxValue
