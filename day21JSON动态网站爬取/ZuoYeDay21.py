# -*- coding:utf-8 -*-
import requests
from myUtils import ProxiesUtils, handleData
from day21JSON动态网站爬取 import utils
import time, random, multiprocessing

pl_url_list = ["https://question.jd.com/question/getQuestionAnswerList.action?callback=jQuery2844970&page={" \
               "}&productId=1466921387".format(i) for i in range(1, 100)]
ceshi_url = "https://question.jd.com/question/getQuestionAnswerList.action?callback=jQuery2844970&page=1&productId=1466921387"


# 1 到 100页的评论连接

def st(queue, url_list):
    proxies_list = []
    info = utils.infoList()
    i = 0
    while True:
        if i == len(url_list):
            break
        while True:
            if queue.empty():
                break
            dic = queue.get()
            proxies_list.append(dic)
        if len(proxies_list) > 5:
            try:
                proxies_list_len = len(proxies_list)
                get_proxy = random.randint(0, len(proxies_list) - 1)
                print(proxies_list_len, "\\", get_proxy)
                res = requests.get(url_list[i], headers=info.getHeaders(),
                                   proxies=proxies_list[get_proxy])
                data = res.content.decode("utf-8")[len("jQuery2844970("):-2:]
                content = handleData.jSonExtract("$..content", data)
                nicName = handleData.jSonExtract("$..nickName", data)
                # if type(content) != 'list' and type(nicName) != 'list':
                #     print("==========返回类型错误==========")
                #     print(type(content), type(nicName))
                #     continue
                # print(type(content), type(nicName))
                for m, n in dict(zip(nicName, content)).items():
                    print(m, n, sep=":\n\t")
            except Exception as e:
                print(e)
                i -= 1
        else:
            print("{}/5".format(len(proxies_list)))
            time.sleep(3)
        i += 1


if __name__ == '__main__':
    queue = multiprocessing.Queue()
    mp1 = multiprocessing.Process(target=ProxiesUtils.getProxies, args=(queue, ceshi_url))
    mp2 = multiprocessing.Process(target=st, args=(queue, pl_url_list))
    mp1.start()
    mp2.start()
    mp1.join()
    mp2.join()
