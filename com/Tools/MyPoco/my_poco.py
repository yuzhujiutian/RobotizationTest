# _*_coding:utf-8 _*_
# !/usr/bin/python3
# Reference:********************************
# encoding: utf-8
# @Time: 2020/1/9  17:06
# @Author: 洞洞
# @File: my_poco.py
# @Function:
# @Method:作为编写脚本时使用的类，所有方法集中在这里供脚本调用
#         辅助脚本使用MyPocoObject类编写
# Reference:********************************
import os
from MyPoco.foundation.MyException import *
from MyPoco.foundation.information import Information
from MyPoco.game_support.entry_game import EntryGame
from MyPoco.game_support.first_function_go_run import FirstFunctionGoRun
from MyPoco.game_support.new_account import NewAccount
from MyPoco.game_support.resource_gm import ResourceGm
from MyPoco.poco.xn_test_tools import XnTest
from MyPoco.protocol.gm_method import GmMethod
from MyPoco.poco.my_poco_object import MyPocoObject
from MyPoco.protocol.protocol_function import ProtocolFunction  # 暂时不接入协议


class MyPoco:
    def __init__(self, game_name, phone_id):
        """
        :param game_name: 游戏名字，见ini文件App_Name项
        :param phone_id: 设备号，如果为None，表示不链接设备
        """
        self.info = Information()
        my_poco_path = os.path.abspath(os.path.dirname(__file__))
        self.info.set_config("MyPocoPath", "MyPocoPath", my_poco_path)
        self.game_name = self.info.get_config("App_Name", game_name)
        self.my_poco_obj = MyPocoObject(self.game_name, phone_id)
        self.gm = GmMethod(self.game_name)
        self.rg = ResourceGm(self.game_name, phone_id)
        self.newaccount = NewAccount(self.game_name, phone_id)
        self.phone_id = phone_id

    def make_new_role(self, server_name, username, protocol_name=""):
        """
        设置协议基本信息
        目前只用于创建角色用，其他协议暂不使用
        :param server_name: 服务器名
        :param username: 账号
        :param protocol_name: 协议名
        :return:
        """
        self.protocol = ProtocolFunction(self.game_name, server_name, protocol_name, username)

    def get_ss2_role_id(self):
        """
        再次调用登录方法获得角色id
        :return:
        """
        return self.protocol.get_role_id()

    def swipe(self, pos1, pos2, duration=3):

        """
        根据传入的坐标进行滑动，调用的airtest自带的滑动方法
        :param pos1: 开始
        :param pos2: 结束
        :param duration: 滑动持续时间
        :return:
        """
        self.my_poco_obj.swipe(pos1, pos2, duration=duration)

    # def set_poco(self):
    #     """
    #     编写脚本时使用
    #     :param poco_path:
    #     :return:
    #     """
    #     return self.my_poco_obj.new_poco_obj()

    def set_account_information_gm(self, account, server_name, role_id=""):
        """
        使用GM方法前需要调用该方法,来确定对哪个账号的哪个区下面的角色进行操作
        :param account:str  账号
        :param server_name:str 如果不传，说明该账号只有一个区有角色
        :param role_id: int 如果不传，则通过api获取
        :return:
        """
        self.gm.set_account_information(account, server_name_input=server_name, role_id=role_id)

    def get_poco_dic(self):
        """
        刷新并获取当前界面UI信息
        :return: ui dic
        """
        return self.my_poco_obj.get_poco_dic()

    def my_touch_in_dic(self, poco_path, poco_dic, click_list=None):
        """
        传入缓存的poco节点字典，直接去点击字典里面缓存的节点
        :param poco_path: poco name
        :param poco_dic: 缓存的字典
        :param click_list: 点击节点偏移量
        :return:
        """
        if self.is_in_dic(poco_path, poco_dic):
            self.my_touch(poco_path, click_list=click_list)
        else:
            raise NoneException(poco_path)

    def is_this_text(self, poco_path, text, is_in=False):
        """
        判断节点的文字
        :param poco_path: 节点的绝对路径
        :param text: 需要判断的文字
        :param text: 是否包含
        :return: bool
        """
        return self.my_poco_obj.is_this_text(poco_path, text, is_in=is_in)

    def set_xn_test(self):
        """
        进行性能测试时需要先启动该方法
        """
        self.xt = XnTest()

    # todo err_close_game
    def first_function_go_run(self):
        """
        用来跳过一些功能初次进入的引导动画
        :return:
        """
        ffgr = FirstFunctionGoRun(self.game_name)
        ffgr.first_function_go_run(self.phone_id)

    # @err_close_game
    def open_game(self, sever_name_input, game_account_input):
        """
        功能向,启动游戏并到游戏主界面
        :param sever_name_input: 区服,读配置或新建账号
        :param game_account_input: 账号,读配置或新建账号
        :param red_info: 是否读取表中的账号
        :return:返回StdPoco().poco对象，可使用原生框架
        """
        entry = EntryGame(self.game_name, self.phone_id)
        entry.entry_game(sever_name_input, game_account_input)
        # poco = self.my_poco_obj.new_poco_obj()
        # return poco

    def close_game(self):
        """
        关闭游戏，不区分功能或者性能
        :return:
        """
        self.my_poco_obj.close_game()

    def get_account_info(self, game_account_input):
        return self.get_config(self.game_name, game_account_input)

    # @err_close_game
    def my_swipe(self, start_path, end_path, timein=3):
        """
        两个对象中心点之间的滑动
        :param start_path:开始路径
        :param end_path:结束路径
        :param timein:不传的话默认2秒
        :return:两个对象的坐标
        """
        return self.my_poco_obj.my_swipe(start_path, end_path, timein)

    # def renovate_and_get_poco_dic(self):
    #     """
    #     刷新UI信息并保存本地
    #     :return: ui dic
    #     """
    #     return self.my_poco_obj.renovate_and_get_poco_dic()

    def my_swipe_pos(self, start_pos_list, end_pos_list, timein=3):
        """
        默认滑动时长3秒
        :param pos_list_int:控件的pos属性
        :return:
        """
        self.my_poco_obj.swipe_pos(start_pos_list, end_pos_list, timein)

    # @err_close_game
    def my_touch(self, poco_path, click_list=None):
        """
        :param poco_path:控件路径
        :param click_list:控件点击偏移点[0,0]-[1,1]范围
        :return:Exception
        """

        self.my_poco_obj.touch_poco(poco_path, click_list=click_list)

    def my_touch_pos(self, pos_list_int,is_sleep = True):
        """
        :param pos_list_int:控件的pos属性
        :return:Exception
        """
        self.my_poco_obj.touch_pos(pos_list_int,is_sleep = is_sleep)

    def xn_touch(self, pos_list_int):
        """
        横屏
        直接调用底层Android框架，只需要执行点击操作，不需要截图添加日志
        根据控件位置在屏幕的百分比进行点击操作
        :param pos_list_int:控件的pos属性
        :return:
        """
        self.xt.xn_touch(pos_list_int)

    def xn_swipe(self, start, end):
        """
        直接调用底层Android框架，只需要执行滑动操作，不需要截图添加日志
        根据控件位置在屏幕的百分比进行点击操作
        :param start: 开始控件pos
        :param end: 结束控件pos
        :return:
        """
        self.xt.xn_swipe(start, end)

    def get_config(self, list_name, key):
        """
        获取配置文件信息
        :param list_name:模块名
        :param key:键
        :return:value
        """
        return self.info.get_config(list_name, key)

    def add_section(self, section_name):
        '''
        在配置文件中添加项
        :param section_name:项名称
        :return:
        '''
        self.info.add_section(section_name)

    def remove_section(self, section_name):
        '''
        删除配置文件中的项
        :param section_name:项名称
        :return:
        '''
        self.info.remove_section(section_name)

    def set_config(self, list_name, key, value):
        """
        设置配置文件信息
        :param list_name:模块名
        :param key:键
        :param value:值
        :return:
        """
        self.info.set_config(list_name, key, value)

    def get_time_str(self, str_time_input):
        """
        根据时间戳字符串换算日期和星期
        :param poco_time_input:包含时间戳text的poco对象
        :return: [int(ymd),int(hms),int(week)]
        """
        return self.info.get_time_str(str_time_input)

    def get_game_number_l(self, poco_path, subscript):
        """
        不同游戏不同实现，获取游戏text属性中的数字 one/two
        :param poco_path:poco对象
        :param subscript:0/1
        :return:int
        """
        return self.my_poco_obj.get_game_number_l(poco_path, subscript)

    def get_game_text_l(self, poco_path, subscript):
        """
        不同游戏不同实现，获取poco对象中text属性中的文字 one/two
        :param poco_path:poco对象
        :param subscript:0/1
        :return:str
        """
        return self.my_poco_obj.get_game_text_l(poco_path, subscript)

    def get_game_number_c(self, poco_path):
        """
        不同游戏不同实现，获取游戏text属性中的数字 ]int[
        :param find_number_poco:poco对象
        :return:int
        """
        return self.my_poco_obj.get_game_number_c(poco_path)

    def get_game_number_cc(self, poco_path):
        """
        不同游戏不同实现，获取游戏text属性中的str数字,]int)
        :param find_number_poco:poco对象
        :return:int
        """
        return self.my_poco_obj.get_game_number_cc(poco_path)

    def get_game_number(self, poco_path):
        """
        获取游戏poco_path-text属性中的str数字
        :param poco_path:poco对象
        :return:int
        """
        return self.my_poco_obj.get_game_number(poco_path)

    def get_game_text(self, poco_path):
        """
        获取游戏poco_path-text属性中的str数字
        :param poco_path:poco对象
        :return:int
        """
        return self.my_poco_obj.get_game_text(poco_path)

    def get_poco_position(self, poco_path):
        """
        获取节点的绝对坐标，经过手机分辨率换算
        :param poco_path: poco_name
        :return:
        """
        return self.my_poco_obj.get_poco_position(poco_path)

    def get_game_number_instr(self, poco_path):
        """
        只获取poco对象中text属性中的数字
        :param poco_path:poco路径
        :return:int
        """
        return self.my_poco_obj.get_game_number_instr(poco_path)

    def get_poco_any_value(self, find_poco_path, value_name_str):
        """
        获取游戏poco对象value_name_str属性中的值，需要自行判断类型
        :param find_poco_path:poco对象的路径
        :param value_name_str:属性的key
        :return:value
        """
        return self.my_poco_obj.get_poco_any_value(find_poco_path, value_name_str)

    def get_phone_name(self):
        """
        获取当前手机的名字，区分三挡机使用
        :return:str
        """
        return self.info.get_phone_name()

    def get_phone_size(self):
        """
        获取当前手机的分辨率
        :return:list_int[宽，高]
        """
        return self.info.get_phone_size()

    def contrast_first_second(self, first, second, msg):
        """
        对比结果值，并在报告连接中添加日志信息，比如资源变化前后的对比
        :param first:对比值one
        :param second:对比值two
        :param msg:日志的描述，==/！=、正常/异常
        :return:
        """
        self.my_poco_obj.contrast_first_second(first, second, msg)

    def first_open_yztest(self):
        """
        启动性能工具，在开始测试步骤前结束
        :return:
        """

    def start_test_xn(self, ):
        """
        性能，点击开始测试按钮，启动游戏并在游戏界面停止
        :return:poco对象
        """
        # todo

        return

    def touch_tab_xn(self):
        """
        点击标记按钮
        :return:
        """

    def end_tab_xn(self):
        """
        在这里添加截图，来判断性能测试操作步骤是否正确
        结束测试并上传报告，在开始测试界面结束
        :return:
        """

    def close_test_xn(self):
        """
        停止性能测试，关闭性能软件和游戏
        :return:
        """

    def text_str(self, input_str):
        """
        输入文本，没有回车键
        :param input_str:需要输入的文本
        :return:
        """
        self.my_poco_obj.text_str(input_str)

    # @err_close_game
    # def new_account(self, resource_dic_input, sever_name_input, play_dic):
    # self.newaccount.new_game_account(resource_dic_input, sever_name_input, play_dic)
    def new_account(self, sever_name_input, resource_dic, play_dic):
        """
        根据输入的要求在sever_name区创建一个账号,需要添加创建账号必备的资源
        :param sever_name_input: 区服名和配置一致
        :param resource_dic: 字典，需要添加的各种资源
        :param play_dic: 字典，需要添加的各种资源
        :return:
        """
        self.set_config(self.game_name, "new_game_account1", "")  # 进入之后重置账号
        account = self.get_random_account()
        self.make_new_role(sever_name_input, account)
        role_id = self.get_ss2_role_id()
        self.set_account_information_gm(account, sever_name_input, role_id)  # 设置GM需要的信息
        self.add_resource(resource_dic)
        if "副本" in play_dic.keys() or "列传" in play_dic.keys():
            self.set_checkpoint(account, sever_name_input, play_dic)
        self.set_config(self.game_name, "new_game_account1", account)
        return account

    def is_exist_poco_log(self, poco_path, is_exist_str):
        """
        判断传入的控件是否处于显示状态,在报告中体现，用来验证按钮点击后的状态
        :param poco_path: 控件路径
        :param is_exist_str:"显示"or"隐藏"
        :return: bool  True or False
        """
        return self.my_poco_obj.is_exist_poco_log(poco_path, is_exist_str)

    def is_exist_poco(self, poco_path):
        """
        判断传入的控件是否处于显示状态 ，用来判断按钮是否可以点击
        :param poco_path: 控件路径
        :return: True/False
        """
        return self.my_poco_obj.is_exist_poco(poco_path)

    def add_msg_in_log(self, msg, is_pass=True):
        """
        将打印信息添加到报告中
        :param msg: 日志描述
        :param is_pass: 改变该条打印的是否通过状态
        :return:
        """
        self.my_poco_obj.add_msg_in_log(msg, is_pass=is_pass)

    def is_in_dic(self, poco_path, poco_dic_input=None):
        """
        判断节点是否在当前屏幕
        :param poco_path: 节点名字
        :return: Ture/False
        """
        return self.my_poco_obj.is_in_dic(poco_path, poco_dic_input=poco_dic_input)

    def is_visible(self, poco_path):
        """
        判断节点能不能点击,一般用作点击之后的状态判断
        :param poco_path: 节点名字
        :return: Ture/False
        """
        return self.my_poco_obj.is_visible(poco_path)

    def add_resource(self, dic_input):
        """
        添加各种资源，协议向
        :param dic_input:dic {"资源名称":资源数量,"资源名称":资源数量,...}
        :return:
        """
        # if self.game_name == "com.youzu.wgame2":
        #     self.gm.add_resources(dic_input)
        # elif self.game_name == "com.youzu.test.qa":
        #     self.rg.add_resource(dic_input)
        self.gm.add_resources(dic_input)

    def get_resource_quantity(self, list_input):
        """
        根据传入的道具列表查询道具数量
        :param resource_name_list:["道具名","道具名2"，"道具名3"]
        :return:{"道具名":道具数量,"道具名2":道具数量，"道具名3":道具数量}
        """
        return self.gm.select_resources(list_input)

    def delete_resource(self, dic_input):
        """
        删除各种资源，协议向
        :param dic_input:dic {"资源名称":资源数量,"资源名称":资源数量,...}
        :return:
        """
        # self.gm.delete_resources(dic_input)
        self.rg.delete_resource(dic_input)

    def get_sever_time(self):
        """
        查询服务器时间
        :param server_name:str 服务器名
        :return:[int(ymd),int(hms),int(week)]
        """
        # return self.gm.select_server_time(server_name)
        return self.rg.get_sever_time()

    def set_sever_time(self, dic_input):
        """
        修改服务器时间
        :param server_time_dic:{"服务器名":时间戳}
        :return:
        """
        self.gm.set_server_time(dic_input)

    # def set_checkpoint(self, checkpoint):
    def set_checkpoint(self, account, sever_name_input, checkpoint):
        """
        设置通关关卡数，目前仅限于少三2
        :param checkpoint:str 玩法名-章节数-小关卡数
        :return:
        """
        if "副本" in checkpoint.keys():
            self.gm.set_checkpoint(checkpoint["副本"])
        if "列传" in checkpoint.keys():
            self.open_game(sever_name_input=sever_name_input, game_account_input=account)
            self.rg.set_play_liezhuan_num(checkpoint["列传"])
        # self.gm.set_checkpoint(checkpoint)

    def set_level(self, level):
        """
        设置玩家等级,目前仅限于少西
        :param level:int 玩家等级
        :return:
        """
        self.gm.set_level(level)

    def recharge_supplement(self, resource_name):
        """
        充值补单
        :param resource_name:"道具名"
        :return:
        """
        self.gm.recharge_supplement(resource_name)

    def game_is_die(self):
        return self.my_poco_obj.game_is_die()

    def get_random_account(self):
        """
        根据时间戳生成一个8位的纯数字字符串，可用于生成账号
        :return: str 8位数字
        """
        return self.my_poco_obj.make_random_account()

    # def start_protocol(self, server_name, protocol_name):#暂时不接入协议
    #     """
    #     传入服务器名和协议名
    #     :param server_name: 服务器名
    #     :param protocol_name:
    #     :return:
    #     """
    #     self.pf = ProtocolFunction(self.game_name, server_name, protocol_name)
