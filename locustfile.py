#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2018/10/21 21:13
# @Author  : Administrator
# @File    : locustfile.py

"""
-----------------------------------------------------

-----------------------------------------------------
"""

from locust import HttpLocust, TaskSet, task
from httprunner import utils, runner


class WebPageTasks(TaskSet):

    def on_start(self):
        self.test_runner = runner.Runner(self.client)
        self.testset = self.locust.testset

    @task
    def test_specified_scenario(self):
        self.test_runner.run_testset(self.testset)


class WebPageUser(HttpLocust):
    host = ''
    task_set = WebPageTasks
    min_wait = 1000
    max_wait = 5000

    testcase_file_path = os.path.join(os.getcwd(), 'testcases//skypixel.yml')
    testsets = utils.load_testcases_by_path(testcase_file_path)
    testset = testsets[0]
