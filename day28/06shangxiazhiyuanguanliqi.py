# -*- coding:utf-8 -*-
with open("01__new__shiyong.py", "r") as f:
    # print(f.readline())
    # print(f.readline())
    # print(f.readlines())
    while True:
        s = f.readline()
        if s != "\n":
            print(s)
        else:
            break


class p(object):
    def __enter__(self):
        print("i am up text management")
        return 1

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("i am down text management")


if __name__ == '__main__':
    p1 = p()
    with p1 as f:
        print("zhixing")
        print(f)