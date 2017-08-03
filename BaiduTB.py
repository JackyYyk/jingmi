# -*- coding: utf-8 -*-

"""
# @Time    : 2017/8/1 23:10

# @Author  : Kun
"""
import urllib
import urllib2
import re

#百度贴吧爬虫类
class BDTB:

    #初始化，传入基地址，是否只看楼主的参数
    def __init__(self,baseUrl,seeLZ):
        self.baseUrl = baseUrl
        self.seeLZ = '?see_lz='+str(seeLZ)

    #传入页码，获取该页帖子的代码
    def getPage(self,pageNum):
        try:
            url = self.baseUrl + self.seeLZ + '&pn=' + str(pageNum)
            request = urllib2.Request(url)
            response = urllib2.urlopen(request)
            print response.read().decode('utf-8')
            return response
        except urllib2.URLError, e:
            if hasattr(e, "reason"):
                print u"连接百度贴吧失败，错误原因", e.reason
                return None

baseUrl = 'http://tieba.baidu.com/p/3138733512'
bdtb = BDTB(baseUrl, 1)
bdtb.getPage(1)