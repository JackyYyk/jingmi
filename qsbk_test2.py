# -*- coding: utf-8 -*-

"""
# @Time    : 2017/7/30 13:39

# @Author  : Kun
"""
# import urllib
import urllib2
import re
# import thread
# import time

#糗事百科爬虫类
class QSBK:

    #初始化方法，定义一些变量
    def __init__(self):
        self.pageIndex = 1
        self.user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'
        #初始化headers
        self.headers = { 'User-Agent' : self.user_agent }
        #存放段子的变量，每一个元素是每一页的段子们
        self.stories = []
        #存放程序是否继续运行的变量
        self.enable = False

    #传入某一页的索引获得页面代码
    def getPage(self,pageIndex):
        try:
            url = 'http://www.qiushibaike.com/hot/page/' + str(pageIndex)
            #构建请求的request
            request = urllib2.Request(url, headers=self.headers)
            #利用urlopen获取页面代码
            response = urllib2.urlopen(request)
            #将页面转换为UTF-8编码
            pageCode = response.read().decode('utf-8')
            return pageCode

        except urllib2.URLError, e:
            if hasattr(e,"reason"):
                print u"连接糗事百科失败，错误原因：", e.reason
                return None

    #传入某一页代码，返回本页段子列表
    def getPageItems(self,pageIndex):
        pageCode = self.getPage(pageIndex)
        if not pageCode:
            print "页面加载失败..."
            return None
        pattern = re.compile('<div.*?author clearfix">.*?<h2>(.*?)</h2>.*?<span>(.*?)</span>.*?class="stats".*?class="number">(.*?)</i>',re.S)
        items = re.findall(pattern, pageCode)
        #用来存储每页的段子们
        pageStories = []
        #遍历正则表达式匹配的信息
        #把信息加入list
        for item in items:
            #把换行<br/>替换为\n
            replaceBR = re.compile('<br/>')
            text = re.sub(replaceBR, "\n", item[1])
            #item[0]是段子的发布者，item[1]是内容，item[2]是点赞个数
            #strip()方法用于移除字符转头尾指定的字符（默认为空格）
            pageStories.append([item[0].strip(),text.strip(),item[2].strip()])
        return pageStories

    #加载并提取页面的内容，加入列表
    def loadPage(self):
        #如果当前未看的页数少于2页，则加载新一页
        if  self.enable == True:
            if len(self.stories) < 2:
                #获取新一页
                pageStories = self.getPageItems(self.pageIndex)
                #将该页的段子存放到全局list中
                if pageStories:
                    self.stories.append(pageStories)
                    #获取完之后页码索引加一，表示下次读取下一页
                    self.pageIndex +=1

    #调用该方法，每次敲回车打印输出一个段子
    def getOneStory(self, pageStories, page):
        #遍历一页的段子
        for story in pageStories:
            #等待用户输入，raw_input方法返回的是字符串类型
            input = raw_input()
            #每当输入回车一次，判断一下是否要加载新页面
            self.loadPage()
            #如果输入Q则程序结束
            if input == 'Q':
                self.enable = False
                return
            print u"第%d页\n发布人:%s\n赞:%s\n%s" % (page, story[0],story[2],story[1])

    #开始方法
    def star(self):
        print u"正在读取糗事百科，按回车查看新段子，Q退出"
        #使变量为True，程序可以正常运行
        self.enable = True
        #先加载一页内容
        self.loadPage()
        #局部变量，控制当前读到了第几页
        nowPage = 0
        while self.enable:
            if len(self.stories) > 0:
                #从全局list中获取一页的段子
                pageStories = self.stories[0]
                #当前读到的页数加一
                nowPage += 1
                #将全局list中的第一个元素删除，因为已经取出
                del self.stories[0]
                #输出该页的段子
                self.getOneStory(pageStories,nowPage)

if __name__ == '__main__':
    spider = QSBK()
    spider.star()



