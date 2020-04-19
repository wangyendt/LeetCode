#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :    2020/4/19 10:43
@Author:  wang121ye
@File: Display Table of Food Orders in a Restaurant.py
@Software: PyCharm
"""


class Solution:
    def displayTable(self, orders: list(list())) -> list(list()):
        menus = sorted(list(set(a[2] for a in orders)))
        menus_dic = {m: i for i, m in enumerate(menus)}
        customers = sorted(list(set(a[1] for a in orders)), key=lambda x: int(x))
        customers_dic = {c: i for i, c in enumerate(customers)}
        # print(menus)
        # print(customers)
        m, n = len(customers), len(menus)
        ret = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        ret[0][0] = 'Table'
        for i in range(1, n + 1):
            ret[0][i] = menus[i - 1]
        for i in range(1, m + 1):
            ret[i][0] = customers[i - 1]
        for order in orders:
            ret[customers_dic[order[1]] + 1][menus_dic[order[2]] + 1] += 1
        ret = [[str(ret[i][j]) for j in range(len(ret[0]))] for i in range(len(ret))]
        return ret


so = Solution()
print(so.displayTable(
    orders=[["David", "3", "Ceviche"], ["Corina", "10", "Beef Burrito"], ["David", "3", "Fried Chicken"],
            ["Carla", "5", "Water"], ["Carla", "5", "Ceviche"], ["Rous", "3", "Ceviche"]]))
print(so.displayTable(
    orders=[["James", "12", "Fried Chicken"], ["Ratesh", "12", "Fried Chicken"], ["Amadeus", "12", "Fried Chicken"],
            ["Adam", "1", "Canadian Waffles"], ["Brianna", "1", "Canadian Waffles"]]))
print(so.displayTable(orders=[["Laura", "2", "Bean Burrito"], ["Jhon", "2", "Beef Burrito"], ["Melissa", "2", "Soda"]]))
