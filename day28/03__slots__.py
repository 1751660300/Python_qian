# -*- coding:utf-8 -*-
import types


class w(object):
    # __slots__ = ('s', 'm')

    def __init__(self, s, m):
        self.s = s
        self.m = m

    def p(self):
        print(self.s, self.m)


if __name__ == '__main__':
    def p(self):
        print(self.m, self.s, self.s1)


    w1 = w(1, 2)
    w1.p()
    w1.s1 = 3
    print(w1.s1)
    w1.p2 = types.MethodType(p, w1)
    w1.p2()
