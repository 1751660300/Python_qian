# -*- coding:utf-8 -*-
num_list = [1, 2, 3]
list_iterator = iter(num_list)  # 取出迭代器对象
print(list_iterator)
print(next(list_iterator))  # 逐一取出数据
print(next(list_iterator))  # 逐一取出数据
print(next(list_iterator))  # 逐一取出数据
# print(next(list_iterator))  # 逐一取出数据 没有数据的话就会报错


# iter()和next()方法实现了最早的迭代
while True:
    try:
        print(next(list_iterator))
    except StopIteration as e:
        print("迭代完成")
        break
