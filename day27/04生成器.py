# -*- coding:utf-8 -*-
# 使用()创建生成器

# num_list = (i for i in range(10))  # 生成器对象
# print(next(num_list))


def t_yield():
    print("__________")
    while True:
        for i in range(10):
            res = yield i
            print("res:", res)


if __name__ == '__main__':
    t = t_yield()
    print(next(t))
    print(next(t))
    print(t.send(7))

