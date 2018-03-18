#!/usr/bin/python
# -*- coding: utf-8 -*-
#####################################
# File name : paster.py
# Create date : 2014-03-06 10:31
# Modified date : 2016-10-20 14:20
# Author : DARREN
# Describe : not set
# Email : lzygzh@126.com
#####################################

import pybase.pylog
import pynetbase.pyHtml
import pybase.pytime
import pycontent
import etc

def get_url_content(url):
    content = pynetbase.pyHtml.get_html_page(url)
    #content = content.decode("gb2312","ignore").encode("utf8")
    return content

def get_root_urls():
    return etc.ROOT_URLS

def get_content_url_list(root_url):
    content = get_url_content(root_url)
    url_list = []
    url_id_list = pycontent.get_img_art_list(content)
    for num in range(len(url_id_list)):
        url = pycontent.get_spider_url(url_id_list[num])
        url_list.append(url)
    return url_list

def get_all_content_urls_from_root_urls():
    url_list = []
    urls = get_root_urls()
    for url in urls:
        lt = get_content_url_list(url)
        url_list.extend(lt)
    return url_list

def deal_url(url):
    con = get_url_content(url)
    if con:
        return get_insert_dic(con,url)
    else:
        return False

def get_insert_dic(con,url):
    img_dic = pycontent.paster_content_page(con,url)
    if img_dic:
        img_dic["origin_url"] = url
        img_dic["sp"] = 1
        img_dic["level"] = etc.LEVEL
        img_dic["channel"] = etc.CHANNEL
        img_dic["day"] = pybase.pytime.get_day()
        return img_dic
    else:
        return False

##########test code###################################

def test():
    lt = get_all_content_urls_from_root_urls()
    for item in lt:
        print item

    lt = etc.TEST_URL_LIST
    for sp_url in lt:
        dic= deal_url(sp_url)
        if dic:
            for item in dic:
                print "%s:%s" % ( item, dic[item])

def run():
    test()

if __name__ == "__main__":
    run()
