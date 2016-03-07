#-*-coding:utf8-*-
import requests
import re
import sys
import time
import random
reload(sys)
sys.setdefaultencoding( "utf-8" )

def get_review(new_link):
    html = requests.get(new_link,headers = ua[random.randint(0,10)])
    #不同的景点建立序号
    f = open('location7.txt','a')
    #提取文本评论
    txt = re.findall('<div class="J_brief-cont">(.*?)</div>',html.text,re.S)
    print len(txt)
    for each in txt:
        #print each
        f.write(each)
    f.close()

old_url = 'http://www.dianping.com/shop/1768267/review_more?pageno=1'
total_page = 194
ua = [{'User-Agent':'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.'},
      {'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50'},
      {'User-Agent':'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;'},
      {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36'},
      {'User-Agent':'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)'},
      {'User-Agent':'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)'},
      {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1'},
      {'User-Agent':'Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11'},
      {'User-Agent':'Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11'},
      {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11'},
      {'User-Agent':'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; TencentTraveler 4.0)'}]

#实现翻页功能
for i in range(54,total_page+1):
    new_link = re.sub('pageno=\d+','pageno=%d'%i,old_url,re.S)
    time.sleep(random.randint(1,10))
    print i
    get_review(new_link)

