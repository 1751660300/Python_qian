# -*- coding:utf-8 -*-
import multiprocessing
from myUtils import autoProxiesSpider
from myUtils import ProxiesUtils
if __name__ == '__main__':

    url_list = ["http://www.wpuic.net.cn/index.html"]
    queue = multiprocessing.Queue()
    t1 = multiprocessing.Process(target=autoProxiesSpider.st, args=(queue, url_list))
    t2 = multiprocessing.Process(target=ProxiesUtils.getProxies, args=(queue, url_list[0]))
    t1.start()
    t2.start()
    t1.join()
    t2.join()