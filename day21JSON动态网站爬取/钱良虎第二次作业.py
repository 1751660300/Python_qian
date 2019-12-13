# -*- coding:utf-8 -*-
import urllib.request
import json
import jsonpath

url = 'https://sclub.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98vv385&productId=52322470877&score=0&sortType=5&page=1&pageSize=10&isShadowSku=0&fold=1 '
headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36',
        'Referer': 'https://item.jd.com/52322470877.html'
    }
res = urllib.request.Request(url, headers=headers)
content = urllib.request.urlopen(res).read().decode('gbk')
content = content.strip("fetchJSON_comment98vv385();")
data = json.loads(content)
nickname = jsonpath.jsonpath(data, '$..nickname')
referenceName = jsonpath.jsonpath(data, expr='$..content')
for i, j in dict(zip(nickname, referenceName)).items():
    print(i, ":\n  ", j)
