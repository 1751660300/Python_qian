# -*- coding:utf-8 -*-
import urllib.request
import json
import jsonpath
import time

end_page = int(input('请输入爬取的结束页码:'))
for i in range(0, end_page + 1):
    print('第%s页开始爬取------' % (i + 1))
    url = 'https://sclub.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98vv385&productId=52322470877&score=0&sortType=5&page={}&pageSize=10&isShadowSku=0&fold=1 '
    # 'https://sclub.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98vv319&productId=10421264905&score=0&sortType=5&page=0&pageSize=10&isShadowSku=0&fold=1'
    url = url.format(i)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36',
        'Referer': 'https://item.jd.com/52322470877.html'
    }

    request = urllib.request.Request(url=url, headers=headers)
    content = urllib.request.urlopen(request).read().decode('gbk')
    content = content.strip('fetchJSON_comment98vv385();')
    obj = json.loads(content)
    comments = obj['comments']
    fp = open('京东.txt', 'a', encoding='utf8')
    for comment in comments:
        # 评论时间
        creationTime = comment['creationTime']
        # 评论人
        nickname = comment['nickname']
        # 评论内容
        contents = comment['content']
        # 评论图片
        if 'images' in comment:
            img_src = jsonpath.jsonpath(comment, '$..images[*].imgUrl')
            img_src = 'https:' + str(img_src).strip('[]')
        else:
            img_src = '无图片'
        item = {
            '评论时间': creationTime,
            '用户': nickname,
            '评论内容': contents,
            '图片地址': img_src,
        }
        string = str(item)
        fp.write(string + '\n')
    print('第%s页完成----------' % (i + 1))
    time.sleep(4)
    fp.close()
