"""
@author: wangye(Wayne)
@license: Apache Licence
@file: Frequency Tracker.py
@time: 20230508
@contact: wang121ye@hotmail.com
@site:  wangyendt@github.com
@software: PyCharm

# code is far away from bugs.
"""

import collections


class FrequencyTracker:

    def __init__(self):
        self.number_freq = collections.defaultdict(int)
        self.freqs = collections.defaultdict(int)

    def add(self, number: int) -> None:
        self.freqs[self.number_freq[number]] = max(0, self.freqs[self.number_freq[number]] - 1)
        self.number_freq[number] += 1
        self.freqs[self.number_freq[number]] += 1

    def deleteOne(self, number: int) -> None:
        if self.number_freq[number] > 0:
            self.freqs[self.number_freq[number]] -= 1
            self.number_freq[number] -= 1
            self.freqs[self.number_freq[number]] += 1

    def hasFrequency(self, frequency: int) -> bool:
        return self.freqs[frequency] > 0
