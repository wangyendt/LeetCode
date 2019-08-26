# !/usr/bin/env python
# -*- coding: utf-8 -*-
# author: wang121ye
# datetime: 2019/8/26 14:55
# software: PyCharm


class Solution:
    def invalidTransactions(self, transactions: list) -> list:
        sorted_trans = []
        for tr in transactions:
            time = int(tr.split(',')[1])
            sorted_trans.append((time, tr))
        sorted_trans.sort(key=lambda x: x[0])
        ret = set()
        stack = []
        for tr in sorted_trans:
            name, time, amount, city = tr[1].split(',')
            time, amount = int(time), int(amount)
            if amount > 1000:
                ret.add(tr[1])
            if stack:
                while stack:
                    start_time = stack[0][2]
                    if time - start_time > 60:
                        stack.pop(0)
                    else:
                        break
                for name_, city_, time_, tr_ in stack:
                    if name_ == name and city_ != city:
                        ret.add(tr_)
                        ret.add(tr[1])
            stack.append((name, city, time, tr[1]))
        return list(ret)


so = Solution()
print(so.invalidTransactions(["alice,20,800,mtv", "bob,50,1200,mtv"]))
print(so.invalidTransactions(["alice,20,800,mtv", "alice,50,1200,mtv"]))
print(so.invalidTransactions(["alice,20,800,mtv", "alice,50,100,beijing"]))
print(so.invalidTransactions(["alice,20,800,mtv", "alice,81,100,beijing"]))
