#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Number of Orders in the Backlog.py 
@time: 2021/03/21
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *
import heapq


class Solution:
    def getNumberOfBacklogOrders(self, orders: List[List[int]]) -> int:
        buy = []
        sell = []
        for prc, amt, ot in orders:
            if ot == 0:
                if not sell:
                    heapq.heappush(buy, [-prc, amt])
                else:
                    while amt > 0:
                        if not sell:
                            heapq.heappush(buy, [-prc, amt])
                            break
                        s, a = sell[0]
                        if prc >= s:
                            if amt < a:
                                sell[0][1] -= amt
                                break
                            else:
                                amt -= a
                                heapq.heappop(sell)
                                # if amt > 0:
                                #     heapq.heappush(buy, [-prc, amt])
                                #     break
                        else:
                            heapq.heappush(buy, [-prc, amt])
                            break
            else:
                if not buy:
                    heapq.heappush(sell, [prc, amt])
                else:
                    while amt > 0:
                        if not buy:
                            heapq.heappush(sell, [prc, amt])
                            break
                        b, a = buy[0]
                        b = abs(b)
                        if prc <= b:
                            if amt < a:
                                buy[0][1] -= amt
                                break
                            else:
                                amt -= a
                                heapq.heappop(buy)
                                # if amt > 0:
                                #     heapq.heappush(sell, [prc, amt])
                                #     break
                        else:
                            heapq.heappush(sell, [prc, amt])
                            break
            print(prc, amt, ot, buy, sell)
        ret = 0
        for b in buy:
            ret += b[1]
        for s in sell:
            ret += s[1]
        return ret % (10 ** 9 + 7)


so = Solution()
print(so.getNumberOfBacklogOrders(orders=[[10, 5, 0], [15, 2, 1], [25, 1, 1], [30, 4, 0]]))
print(so.getNumberOfBacklogOrders(orders=[[7, 1000000000, 1], [15, 3, 0], [5, 999999995, 0], [5, 1, 1]]))
