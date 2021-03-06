# _*_coding:utf-8 _*_
# !/usr/bin/python3
# Reference:********************************
# encoding: utf-8
# @Time: 2019/11/16  14:19
# @Author: 洞洞
# @File: unexpected_win.py
# @Function:
# @Method:
# Reference:********************************
from MyPoco.foundation.information import Information
from MyPoco.game_support.unexpected_win_ss2 import UnexpectedWinSs2
from MyPoco.game_support.unexpected_win_sx import UnexpectedWinSx

class UnexpectedWin:
    def __init__(self, game_name,phone_id):
        self.info = Information()
        self.game_name = game_name
        self.uw = None
        self.phone_id =phone_id
        self.game_list = ["com.youzu.wgame2","com.youzu.test.qa"]
    def unexpected_win(self):
        """
        异常弹窗跳过，区分不同的游戏走不同的逻辑
        :param poco_input: poco对象
        :return:
        """
        if self.uw == None:
            if self.game_name == "com.youzu.wgame2":
                self.uw = UnexpectedWinSx(self.game_name,self.phone_id)

            elif self.game_name == "com.youzu.test.qa":
                self.uw = UnexpectedWinSs2(self.game_name,self.phone_id)
        if self.game_name in self.game_list :
            print("开始查找异常窗口")
            self.uw.unexpected_win()
            print("异常窗口排查完毕")
