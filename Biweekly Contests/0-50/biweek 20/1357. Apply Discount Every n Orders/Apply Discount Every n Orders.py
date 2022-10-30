#!/usr/bin/env python
# encoding: utf-8

"""
@author: Wayne
@contact: wangye.hope@gmail.com
@software: PyCharm
@file: Apply Discount Every n Orders
@time: 2020/2/26 16:30
"""


class Cashier:

    def __init__(self, n: int, discount: int, products: list, prices: list):
        self.counter = 0
        self.n = n
        self.discount = discount
        self.product_to_price = {}

        for index, product in enumerate(products):
            self.product_to_price[product] = prices[index]

    def getBill(self, products: list, amount: list) -> float:
        ret = 0
        self.counter += 1

        for index, product in enumerate(products):
            ret += self.product_to_price[product] * amount[index]

        if self.counter == self.n:
            ret -= (self.discount * ret) / 100
            self.counter = 0

        return ret

# Your Cashier object will be instantiated and called as such:
# obj = Cashier(n, discount, products, prices)
# param_1 = obj.getBill(product,amount)
