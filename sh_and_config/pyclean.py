#!/usr/bin/python
# -*- coding: utf-8 -*-
#####################################
# File name : pyclean.py
# Create date : 2016-08-14 03:00
# Modified date : 2017-08-29 15:52
# Author : DARREN
# Describe : not set
# Email : lzygzh@126.com
#####################################

import os
#import etc
#import table_etc
#import pybase.etc
import pybase.pyprogress

#   def close_self_proc():
#       pybase.pyprogress.close_progress("%s.py" % etc.PROC_NAME)

def delete_log_dir():
    os.popen("rm -rf ./log")

#   def delete_log_db():
#       log_db_name = pybase.etc.DATABASE_NAME
#       os.popen("rm ./%s.db" % log_db_name)

#   def delete_sqltest_db():
#       os.popen("rm ./sqltest.db")

#   def delete_nohup():
#       os.popen("rm ./nohup.out")

#   def delete_pyc():
#       os.popen("rm ./*.pyc")

def delete_ini():
    os.popen("rm ./*.ini")

def delete_log():
    os.popen("rm ./*.log")

def delete_nginx_conf():
    os.popen("rm ./*.conf")

def delete_root_config_sh():
    os.popen("rm ./root_config.sh")

def close_uwsgi_proc():
    pybase.pyprogress.close_progress("%s%s_uwsgi.ini" % ("tttt","9648"))

#   def delete_tmp_file():
#       tmp_file_name = table_etc.TMP_FILE_PATH = "./tmp_file/"
#       os.popen("rm -rf %s" % tmp_file_name)

if __name__ == "__main__":
    delete_ini()
    delete_log()
    delete_nginx_conf()
    delete_root_config_sh()
    close_uwsgi_proc()
    delete_log_dir()
