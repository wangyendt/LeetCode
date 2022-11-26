"""
@author: wangye(Wayne)
@license: Apache Licence
@file: Minimum Penalty for a Shop.py
@time: 20221126
@contact: wang121ye@hotmail.com
@site:  wangyendt@github.com
@software: PyCharm

# code is far away from bugs.
"""


class Solution:
    def bestClosingTime(self, customers: str) -> int:
        customers = customers + 'Y'
        mn, mni = sum(1 for c in customers if c == 'Y'), 0
        cur = mn
        for i, c in enumerate(customers):
            if i > 0:
                if customers[i - 1] == 'Y':
                    cur -= 1
                else:
                    cur += 1
            # print(f'{i=},{c=},{cur=}')
            if cur < mn:
                mni = i
                mn = cur
        return mni


so = Solution()
print(so.bestClosingTime(customers="YYNY"))
print(so.bestClosingTime(customers="NNNNN"))
print(so.bestClosingTime(customers="YYYY"))
print(so.bestClosingTime(customers="YYYN"))
