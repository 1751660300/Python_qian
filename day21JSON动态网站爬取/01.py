# -*- coding:utf-8 -*-
import json
import requests
from day21JSON动态网站爬取 import utils
import jsonpath
import retrying
import random
import proxiesUtils

# data = {
#     "adType": "0",
#     "hasAspData": "0",
#     "thumbURL": "https://ss2.bdstatic.com/70cFvnSh_Q1YnxGkpoWK1HF6hhy/it/u=32277841,2072243611&fm=26&gp=0.jpg",
#     "middleURL": "https://ss2.bdstatic.com/70cFvnSh_Q1YnxGkpoWK1HF6hhy/it/u=32277841,2072243611&fm=26&gp=0.jpg",
#     "largeTnImageUrl": "",
#     "hasLarge": 0,
#     "hoverURL": "https://ss2.bdstatic.com/70cFvnSh_Q1YnxGkpoWK1HF6hhy/it/u=32277841,2072243611&fm=26&gp=0.jpg",
#     "pageNum": 60,
#     "objURL": "ippr_z2C$qAzdH3FAzdH3Fj_z&e3Bitri5p5f_z&e3Bkwt17_z&e3Bv54AzdH3Fkwtg75AzdH3Foi=0da,9nmAzdH3Fft2g=mu9c0bmvwnm9an9uaulbvwa8l1unccacAzdH3F8b1bkvnjk8ncnnuwwmncdcluwa1nu18u9an9ckuk_z&e3B3r2",
#     "fromURL": "ippr_z2C$qAzdH3FAzdH3Fooo_z&e3Bg754t_z&e3Bv54AzdH3F1jwsAzdH3Fswypopy6_z&e3Bip4s",
#     "fromURLHost": "www.nuomi.com",
#     "currentIndex": "",
#     "width": 719,
#     "height": 436,
#     "type": "jpg",
#     "is_gif": 0,
#     "strategyAssessment": "5234_0_0_0",
#     "filesize": "",
#     "bdSrcType": "0",
#     "di": "30910",
#     "pi": "0",
#     "is": "0,0",
#     "imgCollectionWord": ""
# }
# s = json.dumps(data)
# print(s, type(s))
url = "http://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=result&queryWord=%E7%99%BE%E5%BA%A6%E5%A4%B4%E5%83%8F&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=&ic=&hd=&latest=&copyright=&word=%E7%99%BE%E5%BA%A6%E5%A4%B4%E5%83%8F&s=&se=&tab=&width=&height=&face=0&istype=2&qc=&nc=1&fr=&expermode=&force=&pn={}&rn=30&gsm=&1575974931806="
i = 30
info = utils.infoList()
headers = info.getHeaders()
# proxies = proxiesUtils.getProxies()


@retrying.retry(stop_max_attempt_number=1)
def res(u):
    while True:
        # p = proxies[random.randint(1, len(proxies))]
        p = {'http': 'http://182.34.37.211:9999'}
        print(p)
        re = requests.get(u, headers=headers)
        if re.status_code == 200:
            return re.content
        else:
            break
        # else:
        #     if len(proxies) == 0:
        #         return None
        #     else:
        #         proxies.remove(p)


def op(s, text):
    try:
        file = open("./tup/" + s + ".jpg", "wb")
        file.write(text)
        file.close()
    except Exception as e:
        print(e)
    else:
        return True


while i < 150:
    url = url.format(i)
    print(i, url, sep=": ")
    r = res(url)
    if r is not None:
        r = r.decode("utf-8")
        p_url_list = jsonpath.jsonpath(json.loads(r), "$.data..thumbURL")
        p_title_list = jsonpath.jsonpath(json.loads(r), "$.data..fromPageTitleEnc")
        for j, k in dict(zip(p_title_list, p_url_list)).items():
            print(i, k, sep=": ")
            txt = res(k)
            op(j, txt)
        i += 30
    else:
        break


# s = res(url.format(30))
# ss = json.loads(s)
# print(ss)
# s1 = jsonpath.jsonpath(ss, "$.data..thumbURL")
# print(type(s1))
# file = open("test", "r", encoding="utf-8")
# s = file.read()
# file.close()
# j = json.loads(s)
# jj = j.get("data")
# for i in jj:
#     print(i.get("fromPageTitle"), i.get("middleURL"), sep=": ")
