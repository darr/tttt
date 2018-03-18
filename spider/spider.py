#!/usr/bin/python
# -*- coding: utf-8 -*-
#####################################
# File name : spider.py
# Create date : 2017-08-30 21:44
# Modified date : 2017-08-30 22:20
# Author : DARREN
# Describe : not set
# Email : lzygzh@126.com
#####################################

import pybase.pypost
import pybase.pyjson
import pybase.pytime
import math
import time
import hashlib

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


def get_json_data():
    st = pybase.pytime.get_timestamp()
    ttas,ttcp = getASCP()
    print ttas,ttcp
    url = "http://www.toutiao.com/api/pc/feed/?max_behot_time=1504097711&category=__all__&utm_source=toutiao&widen=1&tadrequire=false&as=A135A91A164A479&cp=59A68A54B779DE1" 
    #url = "http://www.toutiao.com/api/pc/feed/?max_behot_time=%s&category=__all__&utm_source=toutiao&widen=1&tadrequire=false&as=%s&cp=%s" % (st,ttas,ttcp)
    print url
    isSuc, ret = pybase.pypost.http_get(url)
    con = pybase.pyjson.json_to_dict(ret)
    for i in con:
        print i
    mess = con["message"]
    if mess ==  "success":
        dt = con["data"]
        for i in range(len(dt)):
            item = dt[i]
            for key in item:
                if key == "group_id":
                    print "%s:%s" % (key,item[key])
                elif key == "image_list":
                    print "%s:%s" % (key,item[key])
                else:
                    print key
    print mess


if __name__ == "__main__":
    get_json_data()
