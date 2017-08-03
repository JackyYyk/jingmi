# -*- coding: utf-8 -*-

"""
# @Time    : 2017/7/28 23:55

# @Author  : Kun
"""
import urllib2
import cookielib

# ---------------------------------------
# 获取Cookie保存到变量
# ---------------------------------------
# # 申明一个CookieJar对象实例来保存cookie
# cookie = cookielib.CookieJar()
# # 利用urllib2库的HTTPCookieProcessor对象来创建cookie处理器
# handler = urllib2.HTTPCookieProcessor(cookie)
# # 通过handler来构建opener
# opener = urllib2.build_opener(handler)
# # 此处的open方法同urllib2的urlopen方法，也可以传入request
# response = opener.open('http://www.baidu.com')
# for item in cookie:
#     print 'Name = ' + item.name
#     print 'Value = ' + item.value


# ---------------------------------------
# 保存Cookie到文件
# ---------------------------------------
# # 设置保存cookie的文件，同级目录下的cookie.txt
# filename = 'cookie.txt'
# # 声明一个MozillaCookieJar对象实例来保存cookie，之后写入文件
# cookie = cookielib.MozillaCookieJar(filename)
# # 利用urllib2库的HTTPCookieProcessor对象来创建cookie处理器
# handler = urllib2.HTTPCookieProcessor(cookie)
# # 通过handler来构建opener
# opener = urllib2.build_opener(handler)
# #创建一个请求，原理同urllbi2的urlopen
# response = opener.open('http://www.baidu.com')
# # 保存cookie到文件
# cookie.save(ignore_discard=True, ignore_expires=True)


# ---------------------------------------
# 从文件中获取Cookie并访问
# ---------------------------------------
# # 创建MozillaCookieJar实例对象
# cookie = cookielib.MozillaCookieJar()
# # 从文件中读取cookie内容到变量
# cookie.load('cookie.txt', ignore_discard=True, ignore_expires=True)
# # 创建请求的request
# req = urllib2.Request("http://www.baidu.com")
# # 利用urllib2的build_opener方法创建一个opener
# opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
# response = opener.open(req)
# print response.read()