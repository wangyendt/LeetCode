# !/usr/bin/env python
# -*- coding: utf-8 -*-
# author: wang121ye
# datetime: 2019/7/12 18:02
# software: PyCharm

class Solution:
    def licenseKeyFormatting(self, S: str, K: int) -> str:
        if not S: return ''
        S = ''.join(S.split('-')).upper()
        if len(S) < K: return S
        d, r = divmod(len(S), K)
        return S[:r] + '-' * (1 if r else 0) + '-'.join([S[r + K * i:r + K * i + K] for i in range(d)])


so = Solution()
# print(so.licenseKeyFormatting(S="5F3Z-2e-9-w", K=4))
print(so.licenseKeyFormatting(S="aaa", K=4))
