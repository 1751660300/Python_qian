# -*- coding:utf-8 -*-
import time

for i in range(10000000):
    print(i)
i = time.process_time()
print(i)
print(i)
list = [k for k in range(10000000)]
i1 = time.process_time()
for j in list:
    print(j)
print(i, "  ", time.process_time() - i1)
