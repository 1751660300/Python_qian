# -*- coding:utf-8 -*-
import time
import greenlet


def w():
    while True:
        print("=====*=====")
        time.sleep(0.5)
        r.switch()


def r():
    while True:
        print("=====/=====")
        time.sleep(0.5)
        w.switch()


if __name__ == '__main__':
    w = greenlet.greenlet(w)
    r = greenlet.greenlet(r)
    w.switch()
