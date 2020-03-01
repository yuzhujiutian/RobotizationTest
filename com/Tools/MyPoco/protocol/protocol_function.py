# _*_coding:utf-8 _*_
# !/usr/bin/python3
# Reference:********************************
# encoding: utf-8
# @Time:
# @Author: 洞洞
# @File:
# @Function:开局指定测试哪个游戏的哪条协议，每个脚本只测试一条协议
# @Method:
# Reference:********************************

from socket import create_connection
from MyPoco.protocol_file import cs_pb2, cg_pb2, out_base_pb2
from MyPoco.protocol.login_game import LoginGame
from MyPoco.protocol.protocol_tools import ProtocolTools
from MyPoco.foundation.information import Information


class ProtocolFunction:
    def __init__(self, game_name,server_name,protocol_name):
        """
        用于协议测试使用，创建账号的协议方法单独实现
        开局指定测试哪个游戏的哪条协议
        通过server_name获取对应服务器的IP、端口和服务器ID。设置连接后直接启动登陆协议
        :param server_name: 区服名
        :param game_name:
        """
        self.info = Information()
        self.pt = ProtocolTools(game_name)
        self.username = self.info.get_config("Account_Number","new_game_account")
        self.protocol_name = protocol_name
        # self.protocol_ages_list= self.pt.get_args_list(protocol_name)  #  todo 可能有报错
        #开始连接
        socket_ages_dic = eval(self.info.get_config(game_name,server_name))
        host =socket_ages_dic["host"]   # host = "10.3.128.5"
        port =int(socket_ages_dic["port"])  # port = 16865
        self.server_id = int(socket_ages_dic["server_id"])
        self.socket = create_connection((host, port))
        # 启动登陆
        self.Login()#可以考虑单独启动

    def Login(self):
        lg = LoginGame(self.socket,self.server_id,self.username)
        flag, data = lg.MSG_C2G_Login()
        G2C_Login = cg_pb2.G2C_Login()
        G2C_Login.ParseFromString(data)
        print(G2C_Login)
        # self.uid = G2C_Login.uid
        # self.sid = G2C_Login.sid
        self.info.set_config("com.youzu.test.qa","uid",str(G2C_Login.uid))
        self.info.set_config("com.youzu.test.qa","sid",str(G2C_Login.sid))
        # 如果ret等于3则需要创角协议
        print(G2C_Login.ret)
        if G2C_Login.ret == 3:
            flag, data = lg.MSG_C2G_Create()

    def send_protocol(self, arg_dic):
        """
        传入参数组，发送协议，并获取返回值
        :param arg_dic: {} 参数集
        :return: 返回值
        """
        flag, data = self.pt.make_def(self.socket, self.protocol_name, arg_dic)
        return flag, data