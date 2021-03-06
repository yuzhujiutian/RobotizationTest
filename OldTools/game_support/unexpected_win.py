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
from airtest.core.api import *

using("Tools")
from get_info.information import Information
from game_support.unexpected_win_sx import UnexpectedWinSx
from game_support.unexpected_win_ss2 import UnexpectedWinSs2


# from Tools.get_info.information import Information
# from Tools.game_support.unexpected_win_sx import UnexpectedWinSx
# from Tools.game_support.unexpected_win_ss2 import UnexpectedWinSs2

class UnexpectedWin:
    def __init__(self):
        self.info = Information()
        self.game_name = self.info.get_config("App_Name", "game_name")

    def set_poco(self, poco_input):
        """
        :param poco_input: 用于设置和切换不同的poco对象
        :return:
        """
        self.poco = poco_input

    def unexpected_win(self):
        """
        异常弹窗跳过，区分不同的游戏走不同的逻辑
        :param poco_input: poco对象
        :return:
        """

        if self.game_name == "com.youzu.wgame2":
            sxuw = UnexpectedWinSx()
            sxuw.sx_unexpected_win()
        elif self.game_name == "com.youzu.test.qa":
            ss2uw = UnexpectedWinSs2()
            ss2uw.set_poco(self.poco)
            ss2uw.ss2_unexpected_win()
        else:
            pass
