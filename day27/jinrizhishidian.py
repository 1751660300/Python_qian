# -*- coding:utf-8 -*-
class english(object):
    def __init__(self, s):
        self.word_list = s.split(" ")
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index > len(self.word_list) - 1:
            raise StopIteration()
        self.index += 1
        return self.word_list[self.index - 1]


p = english("we are the world")
for i in p:
    print(i)
