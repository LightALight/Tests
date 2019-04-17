#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2018/10/21 21:13
# @Author  : Administrator
# @File    : locustfile.py

"""
-----------------------------------------------------

-----------------------------------------------------
"""

host = "https://www.baidu.com"


def hook_print(msg):
    print(msg)


def get_login_token():

    print("查询百度")
    return "token"
