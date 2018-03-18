#!/usr/bin/python
# -*- coding: utf-8 -*-
#####################################
# File name : views.py
# Create date : 2017-03-30 13:35
# Modified date : 2017-09-10 05:02
# Author : DARREN
# Describe : not set
# Email : lzygzh@126.com
#####################################
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.core.mail import send_mail

import pybase.pypost
import pybase.pyjson
import pyHtml
import pybase.pytime
import pybase.pyre
import pybase.pyfile

import pycontent
import urllib2
import urllib
import math
import time
import hashlib
import time
import pycontent
import os

def write_git_file(con="mytest"):
    path= "/home/liuzy/github/iri8/iri8/"
    name="test.json"
    full_path = "%s/%s" % (path,name)
    file_content = con
    file_object = pybase.pyfile.create_file(path,name)
    file_object.write(file_content)
    file_object.close()
    run_sh(path,name)

def run_sh(path,name):
    os.popen("./git_sh.sh %s %s >> ./gitlog.log" % (path,name))

def getASCP():
    t = int(math.floor(time.time()))
    e = hex(t).upper()[2:]
    m = hashlib.md5()
    m.update(str(t).encode(encoding='utf-8'))
    i = m.hexdigest().upper()

    if len(e) != 8:
        AS = '479BB4B7254C150'
        CP = '7E0AC8874BB0985'
        return AS,CP
    n = i[0:5]
    a = i[-5:]
    s = ''
    r = ''
    for o in range(5):
        s += n[o] + e[o]
        r += e[o + 3] + a[o]

    AS = 'A1' + s + e[-3:]
    CP = e[0:3] + r + 'E1'
    return AS,CP

def open_url(url):    
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}

    null_proxy_handler = urllib2.ProxyHandler({})
    opener = urllib2.build_opener(null_proxy_handler)
    urllib2.install_opener(opener)

    req = urllib2.Request(url) 
    req.add_header('User-Agent', "Mozilla/5.0")
    response = urllib2.urlopen(req)
    data = response.read().decode('utf-8')
    return data

def _check_request_argc(request,key_name):
    arg_dic = request.GET
    #arg_dic = request.arguments
    method = "get"
    if (request.method == pybase.pyjson.get_request_post()):
        dic  = pybase.pyjson.json_to_dict(request.body)
        info_dic = dic["info"]
        dic = dic["data"]
        arg_dic = info_dic
        method = "post"

    if arg_dic:
        try:
            if arg_dic.has_key(key_name):
                if method == "get":
                    v = arg_dic.get(key_name,"")[0]
                elif method == "post":
                    v = arg_dic.get(key_name,"")
                else:
                    ret = "do not know request method: %s" % method
                    return (False,pybase.pyjson.json_fail(ret, request.method))
                return (True,v)
            else:
                ret = "do not have argument %s" % key_name
                return (False,pybase.pyjson.json_fail(ret, request.method))
        except Exception, e:
            ret = "%s" % e
            pybase.pylog.warning(ret)
            return (False,pybase.pyjson.json_fail(ret, request.method))
    else:
        ret = "do not have arguments"
        return (False,pybase.pyjson.json_fail(ret, request.method))


#def get_json_data():
def get_json_data(st,ttas,ttcp):
    #st = int(time.time())
    #ttas,ttcp = getASCP()
    #print ttas,ttcp
    #url = "http://www.toutiao.com/api/pc/feed/?max_behot_time=1504097711&category=__all__&utm_source=toutiao&widen=1&tadrequire=false&as=A135A91A164A479&cp=59A68A54B779DE1" 
    url = "http://www.toutiao.com/api/pc/feed/?max_behot_time=%s&category=__all__&utm_source=toutiao&widen=1&tadrequire=false&as=%s&cp=%s" % (st,ttas,ttcp)
    #isSuc, ret = pybase.pypost.http_get(url)
    ret = open_url(url)
    #global gcon = ret
    return ret

def home(request):
    pybase.pylog.info(request.path)
    pybase.pylog.info(request.META['SERVER_NAME'])
    server_name = request.META['SERVER_NAME']
    subname = server_name.split('.')[0]
    lt = read_sub_webs()
    if subname  in lt:
        return render(request, 'tttt/home.html',{'subweb':subname})
    else:
        return render(request, 'tttt/lt.html',{"subweb":subname})

def read_sub_webs():
    fo = pybase.pyfile.open_file('./','subwebname',type='r')
    con = fo.read()
    lt = con.split('\n')
    return lt[:-1]

def mytest(request):
    user_name = request.user
    return render(request, 'tttt/h.html')
    #return render(request, 'furni/h.html',{"username":user_name})
    #return HttpResponse("Hello world ! ")

def myfeed(request):
    key_name = "max_behot_time"
    is_have, st = _check_request_argc(request,key_name)
    key_name = "as"
    is_have, ttas = _check_request_argc(request,key_name)
    key_name = "cp"
    is_have, ttcp = _check_request_argc(request,key_name)
    ret = get_json_data(st,ttas,ttcp)
    #ret = get_json_data()
    return HttpResponse(ret)

def deelconi(request):
    url = request.path
    url = "http://www.toutiao.com%s" % url
    ret = get_url_content(url)
    return render(request, 'tttt/con.html',{"con_content":ret})

def deelcon64604(request):
    url = request.path
    url = "http://www.toutiao.com%s" % url
    print url
    ret = get_a_url_content(url)
    return render(request, 'tttt/cona.html',{"con_content":ret})

def deelcon64607(request):
    url = request.path
    url = "http://www.toutiao.com%s" % url
    print url
    ret = get_a_url_content64607(url)
    return render(request, 'tttt/conb.html',{"con_content":ret})

def get_a_url_content(url):
    content = pyHtml.get_html_page(url)
    #content = content.decode("gb2312","ignore").encode("utf8")
    con_dic_str = pycontent.get_a_content_dict_str(content)
    print con_dic_str
    con_content = pycontent.get_a_content(con_dic_str)
    #print con_content
    dic = pybase.pyjson.json_to_dict(con_content)
    print dic
    ndic = dic.copy()
    for key in dic:
        print key
        if key=="sub_abstracts":
            lt = dic[key]
            nlt = []
            for i in range(len(lt)):
                c = lt[i]
                tc = get_trans(c)
                nlt.append(tc)
            ndic[key] = nlt
        elif key == "sub_titles":
            lt = dic[key]
            nlt = []
            for i in range(len(lt)):
                c = lt[i]
                tc = get_trans(c)
                nlt.append(tc)
            ndic[key] = nlt
    print ndic

    return ndic

def get_a_url_content64607(url):
    content = pyHtml.get_html_page(url)
    base_data_str = pycontent.get_base_data_str(content)
    art_str = pycontent.get_article_info(base_data_str)
    print art_str
    title_str = pycontent.get_content_title(art_str).decode('utf-8')
    con_str = pycontent.get_item_content(art_str).decode('utf-8')
    dic = {}

    dic["title"] = title_str
    dic["title_trans"] = get_trans(title_str)

    dic["con"] =con_str

    con_trans = con_str.replace("&amp;","&");
    con_trans = con_trans.replace("&lt;","<");
    con_trans = con_trans.replace("&gt;",">");
    con_trans = con_trans.replace("&quot;","\"");
    img_lt = pycontent.get_img_lt(con_trans)
    print img_lt
    con_trans = pybase.pyre.delete_html_label(con_trans)
    con_trans = con_trans.replace(" ","");
    con_lt = con_trans.split("\n")
    con_trans = con_trans.replace("\n","");
    trans_ret = ""
    
    y = 0
    for i in range(len(con_lt)):
        if con_lt[i] != '':
            trans_item = get_trans(con_lt[i])
            if y < len(img_lt):
                trans_ret = "%s<p>%s</p><img src=%s" %  (trans_ret,trans_item,img_lt[y])
                y = y + 1
            else:
                trans_ret = "%s<p>%s</p>" %  (trans_ret,trans_item)
    if y < len(img_lt):
        for i in range(y+1,len(img_lt)):
            trans_ret = "%s<img src=%s" %  (trans_ret,trans_item,img_lt[y])

    dic["con_trans"] = trans_ret
    #con_trans = con_trans.replace("&nbsp","");
    #print con_trans
    #   if len(con_trans) < 4000:
    #       trans_str= get_trans(con_trans)
    #       dic["con_trans"] = trans_str
    #   else:
    #       print "too long"
    for i in range(len(img_lt)):
        print img_lt[i]
    return dic


def get_trans(con):
    con = con.replace(" ","&nbsp;")
    url = "http://trans.aidaling.com/dltran/query"
    infoDic= {
    #"tl":"ja",
    "sl":"zh-CN",
#    "tl":"en",
    "tl":"ko_KR",
    "q":u"%s" % con
    }

    dataDic = {}
    sendDic = {
    "info":infoDic,
    "data":dataDic
    }
    isSuc,ret = pybase.pypost.send(url,sendDic)

    if isSuc == True:
        dic = pybase.pyjson.json_to_dict(ret)
        t = dic["data"]["t"]
        print t
        return t
    else:
        return ""

def gettoutiao(url):
    ret = open_url(url)

def deelconp(request):
    url = request.path
    url = "http://www.toutiao.com%s" % url
    ret = get_url_content(url)
    return render(request, 'tttt/con.html',{"con_content":ret})

def get_url_content(url):
    content = pyHtml.get_html_page(url)
    #content = content.decode("gb2312","ignore").encode("utf8")
    con_dic_str = pycontent.get_content_dict_str(content)
    print con_dic_str
    con_content = pycontent.get_content(con_dic_str)
    print con_content
    return con_content

def test_i_url():
    url = "http://www.toutiao.com/i6459592468387070478/"
    get_url_content(url)

def test_a_url():
    #url = "http://www.toutiao.com/a6460452639602639374"
    #get_a_url_content(url)
    #url = "http://www.toutiao.com/a6460732777703670286"
    #url = "http://www.toutiao.com/a6461006673346560525"
    #url = "http://www.toutiao.com/i6459592468387070478/"
    url = "http://www.toutiao.com/a6460702142796661262/"
    ret = get_a_url_content64607(url)
    #dic = pybase.pyjson.json_to_dict(ret)
    #print dic

def test_git_file():
    con ='''
{
    "title": "这个是标题",
    "content": "这个是内容内容"
}
'''
    write_git_file(con)

if __name__ == "__main__":
    #test_a_url()
    server_name = 'en.iri8.com'

#def send_email():
#    send_mail('send email test','this is conetnt','lzygzh@126.com',['279357271@qq.com',],fail_silently=False)
