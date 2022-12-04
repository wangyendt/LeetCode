"""
@author: wangye(Wayne)
@license: Apache Licence
@file: Circular Sentence.py
@time: 20221204
@contact: wang121ye@hotmail.com
@site:  wangyendt@github.com
@software: PyCharm

# code is far away from bugs.
"""


class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        words = sentence.split(' ')
        last = ''
        for w in words:
            if last and w[0] != last:
                break
            last = w[-1]
        else:
            if sentence[0] == sentence[-1]:
                return True
        return False
