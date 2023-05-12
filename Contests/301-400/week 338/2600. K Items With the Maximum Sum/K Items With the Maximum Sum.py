"""
@author: wangye(Wayne)
@license: Apache Licence
@file: K Items With the Maximum Sum.py
@time: 20230512
@contact: wang121ye@hotmail.com
@site:  wangyendt@github.com
@software: PyCharm

# code is far away from bugs.
"""


class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        if k <= numOnes:
            return k
        elif k <= numOnes + numZeros:
            return numOnes
        return numOnes - (k - numOnes - numZeros)
