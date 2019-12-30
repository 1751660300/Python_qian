# -*- coding:utf-8 -*-
class w(object):
    def __init__(self):
        self.money = 0

    @property
    def show(self):
        print("name")

    @property
    def price(self):
        return self.money

    @price.setter
    def price(self, money):
        self.money = money

    @price.deleter
    def price(self):
        self.money = 0
        print("init money finished")


if __name__ == '__main__':
    p = w()
    p.show

    print(p.price)
    p.price = 30
    print(p.price)
    del p.price
    print(p.price)
