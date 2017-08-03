# -*- coding: utf-8 -*-

"""
# @Time    : 2017/7/29 22:48

# @Author  : Kun
"""
import re
import urllib
import urllib2

page = 1
url = 'http://www.qiushibaike.com/hot/page/' + str(page)
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'
headers = { 'User-Agent' : user_agent }
try:
    request = urllib2.Request(url, headers = headers)
    response = urllib2.urlopen(request)
    content = response.read().decode('utf-8')
    pattern = re.compile('<div.*?author clearfix">.*?<h2>(.*?)</h2>.*?<span>(.*?)</span>.*?class="stats".*?class="number">(.*?)</i>',re.S)
    items = re.findall(pattern, content)
    for item in items:
        print item[0], item[1], item[2]
except urllib2.URLError, e:
    if hasattr(e,"code"):
        print e.code
    if hasattr(e,"reason"):
        print e.reason
