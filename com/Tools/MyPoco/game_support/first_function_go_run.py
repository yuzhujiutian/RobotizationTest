# _*_coding:utf-8 _*_
#!/usr/bin/python3
#Reference:********************************
# encoding: utf-8
#@Time: 2019/12/13  17:57
#@Author: 洞洞
#@File: first_function_go_run.py
#@Function:
#@Method:
#Reference:********************************
from MyPoco.game_support.first_function_go_run_ss2 import FirstFunctionGoRunSs2


class FirstFunctionGoRun:
    def __init__(self,game_name):

        self.game_name = game_name

    def first_function_go_run(self,phone_id):
        """
        用来跳过一些功能初次进入的引导动画
        :return:
        """
        if self.game_name == "com.youzu.test.qa":
            ffgrs2 = FirstFunctionGoRunSs2()
            ffgrs2.first_function_go_run_ss2(phone_id)
        else:
            pass