#!/usr/bin/python
# -*- coding: utf-8 -*-
#####################################
# File name : pyHtml.py
# Create date : 2016-10-01 04:16
# Modified date : 2017-09-01 07:54
# Author : DARREN
# Describe : not set
# Email : lzygzh@126.com
#####################################

import pybase.pylog
import urllib2
import pybase.pytime
import socket
##import Image
#from PIL import Image
import cStringIO

def get_html_page(url):
    try:
        refer = "http://www.baidu.com"
        req = None
        i_headers = {"User-Agent":"Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9.1) Gecko/20090624 Firefox/3.5", "Referer":refer}
        socket.setdefaulttimeout(10)
        req = urllib2.Request(url, headers=i_headers)
        response = urllib2.urlopen(req)
        the_page = response.read()
        return the_page
    except Exception , e:
        pybase.pylog.error("url:%s error:%s" % (url,e))
        return False

def get_html_page_with_proxy(lt,url):
    proxy_ip = lt[1]
    proxy_port = lt[2]
    ret = ''
    socket.setdefaulttimeout(5)
    try:
        ret = urllib.urlopen(url,proxies = {'http':'http://%s:%s' % (proxy_ip, proxy_port)})
    except Exception,e:
        print 'get web html %s' % e
        return False
    if ret:
        return True
    return False

#   def get_img_size(url):
#       hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
#       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
#       'Accept-Encoding': 'none',
#       'Accept-Language': 'en-US,en;q=0.8',
#       'Connection': 'keep-alive'}
#       req= urllib2.Request(url, headers=hdr)

#       file = urllib2.urlopen(req)
#       tmpIm = cStringIO.StringIO(file.read())
#       im = Image.open(tmpIm)
#       return im.format, im.size, im.mode

def get_request_arguments(request,argu_name):
    v = False
    try:
        v = request.arguments.get(argu_name,False)[0]
    except Exception, e:
        ret = "do not have arguments %s or %s get fail" % (argu_name,argu_name)
        pybase.pylog.warning(ret)
    return v
