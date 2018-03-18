#!/usr/bin/python
# -*- coding: utf-8 -*-
#####################################
# File name : pycontent.py
# Create date : 2016-09-24 05:56
# Modified date : 2017-09-02 08:26
# Author : DARREN
# Describe : not set
# Email : lzygzh@126.com
#####################################

import pybase.pyre
import pybase.pylog
import urllib2
import cStringIO
#import Image
import pyHtml
#import etc

def get_center_content(front,behind,content,re_str=".*?"):
    ret = ""
    try:
        ret = pybase.pyre.get_center_content(front=front,behind=behind,content=content,re_str=re_str)
    except Exception , e:
        pybase.pylog.error("error:%s" % e)

    if ret:
        return ret.strip()
    return ""

def get_all_center_content(front,behind,content,re_str=".*?"):
    ret = ""
    try:
        ret = pybase.pyre.get_all_center_content(front=front,behind=behind,content=content,re_str=re_str)
    except Exception , e:
        pybase.pylog.error("error:%s" % e)

    if ret:
        return ret
    return ""


def get_content(page):
    front = 'content: \''
    behind = '\''
    content = page
    re_str = '.*?'
    con = get_center_content(front=front,behind=behind,content=content,re_str=re_str)
    return con

def get_a_content_dict_str(page):
    front = 'BASE_DATA.galleryInfo = {'
    behind = '}<'
    content = page
    re_str = '.*?'
    con = get_center_content(front=front,behind=behind,content=content,re_str=re_str)
    #con = "%s}" % con
    return con

def get_base_data_str(page):
    front = '<script>var BASE_DATA'
    behind = '</script>'
    content = page
    re_str = '.*?'
    con = get_center_content(front=front,behind=behind,content=content,re_str=re_str)
    con = "%s;" % con

    front = '= {'
    behind = '};'
    content =con
    re_str = '.*?'
    con = get_center_content(front=front,behind=behind,content=content,re_str=re_str)
    con = "{%s}" % con
    print con
    return con

def get_a_content(page):
    front = 'gallery: \{'
    behind = ']\},'
    content = page
    re_str = '.*?'
    con = get_center_content(front=front,behind=behind,content=content,re_str=re_str)
    con = "{%s]}" % con
    return con

def get_content_title(page):
    front = 'title: \''
    behind = '\','
    content = page
    re_str = '.*?'
    con = get_center_content(front=front,behind=behind,content=content,re_str=re_str)
    return con

def get_article_info(page):
    front = 'articleInfo'
    behind = '},'
    content = page
    re_str = '.*?'
    con = get_center_content(front=front,behind=behind,content=content,re_str=re_str)
    return con

def get_item_content(page):
    front = 'content: \''
    behind = '\''
    content = page
    re_str = '.*?'
    con = get_center_content(front=front,behind=behind,content=content,re_str=re_str)

    return con

def get_content_dict_str(page):
    front = 'var BASE_DATA = '
    behind = '};'
    content = page
    re_str = '.*?'
    con = get_center_content(front=front,behind=behind,content=content,re_str=re_str)
    con = "%s};" % con
    return con

def get_img_lt(page):
    front = '<img src='
    behind = '<'
    content = page
    re_str = '.*?'
    con = get_all_center_content(front=front,behind=behind,content=content,re_str=re_str)
    return con

def get_title(page):
    front = '<div class="j-r-list-c-desc">'
    behind = '</div>'
    content = page
    re_str = '.*?'
    con = get_center_content(front=front,behind=behind,content=content,re_str=re_str)
    con = pybase.pyre.delete_html_tag(con)
    return con

##########test code###################################

def run():
    pass

if __name__ == "__main__":
    run()
