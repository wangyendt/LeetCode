# !/usr/bin/env python
# -*- coding: utf-8 -*-
# author: wang121ye
# datetime: 2019/10/27 12:13
# software: PyCharm


import collections


class Solution:
    def maxLength(self, arr: list) -> int:
        arr = [list(set(a)) for a in arr if len(a) == len(set(a))]
        if not arr:
            return 0
        n = len(arr)
        connected = collections.defaultdict(int)
        for i in range(n):
            for j in range(i + 1, n):
                if len(arr[i]) + len(arr[j]) > len(set(arr[i] + arr[j])):
                    connected[1 << (n - 1 - i)] |= 1 << (n - 1 - j)
                    connected[1 << (n - 1 - j)] |= 1 << (n - 1 - i)
        ret = {'res': 0}

        def helper(mask, cur, cur_val):
            # print(mask, cur, cur_val)

            def int_log(v):
                ilog = 0
                while v:
                    ilog += 1
                    v >>= 1
                return ilog - 1

            while mask:
                last = mask & (-mask)
                is_overlap = connected[last] & cur
                mask &= mask - 1
                if not is_overlap:
                    offset = len(arr[-1 - int_log(last)])
                    ret['res'] = max(ret['res'], cur_val + offset)
                    helper(mask, cur | last, cur_val + offset)

        helper(2 ** n - 1, 0, 0)
        return ret['res']


so = Solution()
print(so.maxLength(arr=["un", "iq", "ue"]))
print(so.maxLength(arr=["cha", "r", "act", "ers"]))
print(so.maxLength(arr=["abcdefghijklmnopqrstuvwxyz"]))
print(so.maxLength(["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l"]))
print(so.maxLength(["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p"]))
print(so.maxLength(["abcdefghijklm",
                    "bcdefghijklmn",
                    "cdefghijklmno",
                    "defghijklmnop",
                    "efghijklmnopq",
                    "fghijklmnopqr",
                    "ghijklmnopqrs",
                    "hijklmnopqrst",
                    "ijklmnopqrstu",
                    "jklmnopqrstuv",
                    "klmnopqrstuvw",
                    "lmnopqrstuvwx",
                    "mnopqrstuvwxy",
                    "nopqrstuvwxyz",
                    "opqrstuvwxyza",
                    "pqrstuvwxyzab"]))
print(so.maxLength(["yy", "bkhwmpbiisbldzknpm"]))
print(so.maxLength(["zog", "nvwsuikgndmfexxgjtkb", "nxko"]))
print(so.maxLength(
    ["ogud", "ejipchfydrgl", "b", "kjxmzhnuoisgqvawel", "mizlcgdqebwuotfnk", "bjvkrgeozidytquchlw", "tzjqwumkirxeal",
     "x", "rkpuabmo", "mxndpcqzua"]))
