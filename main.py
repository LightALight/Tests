#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2019/4/17 0:28
# @Author  : Administrator
# @File    : main.py

"""
-----------------------------------------------------

-----------------------------------------------------
"""
import os
from httprunner.api import HttpRunner

runner = HttpRunner()
discover_cases = os.path.join(r'testsuites', 'test_suite_demo.yml')
discover_cases = os.path.abspath(discover_cases)
print(discover_cases)
runner.run(discover_cases)