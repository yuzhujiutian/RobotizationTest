# _*_coding:utf-8 _*_
# !/usr/bin/python3
# Reference:********************************
# encoding: utf-8
# @Time: 2019/11/16  15:01
# @Author: 洞洞
# @File: new_account.py
# @Function:
# @Method:
# Reference:********************************
from MyPoco.foundation.information import Information
from MyPoco.game_support.new_account_ss2 import NewAccountSs2


class NewAccount:

    def __init__(self,game_name,phone_id):
        self.info = Information()
        self.game_name =game_name
        if self.game_name == "com.youzu.test.qa":
            self.nas = NewAccountSs2(phone_id)
        else:
            pass

    def new_game_account(self,  resource_dic_input, sever_name_input,play_dic):  # 接口方法，后期拓展游戏使用
        """
        创建一个新账号
        :param dic_input: 账号要求，字典
        :param sever_name_input: 区服名
        :return:
        """
        if self.game_name == "com.youzu.test.qa":  # ss2
            print("开始创建账号")
            self.account,self.role_name=self.nas.new_account_ss2( resource_dic_input, sever_name_input,play_dic)
        else:
            pass
        self.info.set_config(self.game_name, "new_game_account1", self.account)
        account_info = {sever_name_input:self.role_name}
        print(self.info.root_dir_path)
        print("开始存入账号信息"+self.account+str(account_info))
        self.info.set_config(self.game_name,self.account,str(account_info))
        return self.account
