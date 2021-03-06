#!/usr/bin/python
# -*- coding: utf-8 -*-
# author:liahu
# datetime:2019/9/11 10:56
# software: PyCharm

from locust import TaskSequence, Locust, seq_task, task
from locust.exception import StopLocust
from protocol_file.func import *
from protocol_file.rclient import getuserid
from socket import create_connection


class WorkTaskSet(TaskSequence):
    def __init__(self, parent):
        super(WorkTaskSet, self).__init__(parent)
        self.username = getuserid()

    def judge(self, flag):
        if not flag:
            self.over()

    # 登录
    @seq_task(1)
    def Login(self):
        flag, data = MSG_C2G_Login(self)
        self.judge(flag)
        G2C_Login = cg_pb2.G2C_Login()
        G2C_Login.ParseFromString(data)
        print(G2C_Login)
        print(G2C_Login.uid, G2C_Login.sid)
        self.uid = G2C_Login.uid
        self.sid = G2C_Login.sid
        print("====================",G2C_Login.ret)
        # 如果ret等于3则需要创角协议
        if G2C_Login.ret == 3:
            flag, data = MSG_C2G_Create(self)
            self.judge(flag)
            G2C_Create = cg_pb2.G2C_Create()
            G2C_Create.ParseFromString(data)
            print(G2C_Create)
        else:
            pass


    @seq_task(2)
    @task(200)
    def stormcity_info(self):
        #print("1111111111111111111")
        flag, data = MSG_C2S_StormCity_Info(self)
        self.judge(flag)
        S2C_StormCity_Info = cs_pb2.S2C_StormCity_Info()
        S2C_StormCity_Info.ParseFromString(data)
        print(S2C_StormCity_Info.ret)
        for key in S2C_StormCity_Info.units:
            print(key)
            if key.can_challenge:
                self.battle_rank = key.rank
                #print("=================================",key.rank, key.id, key.can_challenge)
                break;

        print("222222222222222222")
        flag, data = MSG_C2S_StormCity_ChallengeBegin(self)
        self.judge(flag)
        S2C_StormCity_ChallengeFinish = cs_pb2.S2C_StormCity_ChallengeFinish()
        S2C_StormCity_ChallengeFinish.ParseFromString(data)
        print(S2C_StormCity_ChallengeFinish)

        # print("333333333333333333")
        flag, data = MSG_C2S_StormCity_ChallengeBegin_Bar(self)
        self.judge(flag)
        S2C_StormCity_ChallengeBegin = cs_pb2.S2C_StormCity_ChallengeBegin()
        S2C_StormCity_ChallengeBegin.ParseFromString(data)
        print(S2C_StormCity_ChallengeBegin)
        print(S2C_StormCity_ChallengeBegin.ret, S2C_StormCity_ChallengeBegin.rank)

    """
    #攻城掠地-城主抢夺信息
    @seq_task(2)
    def stormcity_info(self):
        #print("1111111111111111111")
        flag, data = MSG_C2S_StormCity_Info(self)
        S2C_StormCity_Info = cs_pb2.S2C_StormCity_Info()
        S2C_StormCity_Info.ParseFromString(data)
        print(S2C_StormCity_Info.ret)
        for key in S2C_StormCity_Info.units:
            print(key)
            if key.can_challenge:
                self.battle_rank = key.rank
                #print("=================================",key.rank, key.id, key.can_challenge)
                break;

    
    #攻城掠地-城池抢夺挑战12404
    @seq_task(3)
    def stormcity_challengebegin(self):
        print("222222222222222222")
        flag, data = MSG_C2S_StormCity_ChallengeBegin(self)
        S2C_StormCity_ChallengeFinish = cs_pb2.S2C_StormCity_ChallengeFinish()
        S2C_StormCity_ChallengeFinish.ParseFromString(data)
        print(S2C_StormCity_ChallengeFinish)


    #攻城掠地-城池抢夺挑战 在接受一个协议 12403
    @seq_task(4)
    def stormcity_challengebegin_bar(self):
        #print("333333333333333333")
        flag, data = MSG_C2S_StormCity_ChallengeBegin_Bar(self)
        S2C_StormCity_ChallengeBegin = cs_pb2.S2C_StormCity_ChallengeBegin()
        S2C_StormCity_ChallengeBegin.ParseFromString(data)
        print(S2C_StormCity_ChallengeBegin)
        print(S2C_StormCity_ChallengeBegin.ret, S2C_StormCity_ChallengeBegin.rank)

    
    #攻城掠地-城池抢夺官职奖励
    @seq_task(5)
    def stormcity_getlordaward(self):
        print("444444444444444444444")
        flag, data = MSG_C2S_StormCity_GetLordAward(self)
        S2C_StormCity_GetLordAward = cs_pb2.S2C_StormCity_GetLordAward()
        S2C_StormCity_GetLordAward.ParseFromString(data)
        print(S2C_StormCity_GetLordAward)


    #攻城掠地-城池抢夺获取排行榜
    @seq_task(6)
    def C2S_StormCity_GetRanklist(self):
        print("5555555555555555555555555")
        flag, data = MSG_C2S_StormCity_GetRanklist(self)
        S2C_StormCity_GetRanklist = cs_pb2.S2C_StormCity_GetRanklist()
        S2C_StormCity_GetRanklist.ParseFromString(data)
        print(S2C_StormCity_GetRanklist)
    """

    @seq_task(99)
    def over(self):
        print("over")
        raise StopLocust("task over")

        """
    # 商店
    @seq_task(2)
    def shopping(self):
        flag, data = MSG_C2S_Shop_Shopping(self)
        # S2C_Shop_Shopping = cs_pb2.S2C_Shop_Shopping()
        # S2C_Shop_Shopping.ParseFromString(data)
        # print(S2C_Shop_Shopping)

    # 招募
    @seq_task(3)
    def recruit_recruit(self):
        flag, data = MSG_C2S_Recruit_Recruit(self)
        # S2C_Recruit_Recruit = cs_pb2.S2C_Recruit_Recruit()
        # S2C_Recruit_Recruit.ParseFromString(data)
        # print(S2C_Recruit_Recruit)

    # 取背包数据
    @seq_task(4)
    def Flush(self):
        flag, data = MSG_C2S_Flush(self)
        # S2C_Flush = cs_pb2.S2C_Flush()
        # S2C_Flush.ParseFromString(data)
        # print(S2C_Flush)

    # 武器升级
    @seq_task(5)
    def Upgrade(self):
        flag, data = MSG_C2S_Knight_Upgrade(self)
        # S2C_Knight_Upgrade = cs_pb2.S2C_Knight_Upgrade()
        # S2C_Knight_Upgrade.ParseFromString(data)
        # print(S2C_Knight_Upgrade)

    # 获取副本数据
    @seq_task(6)
    def getchapterlist(self):
        flag, data = MSG_C2S_Dungeon_GetChapterList(self)
        # S2C_Dungeon_GetChapterList = cs_pb2.S2C_Dungeon_GetChapterList()
        # S2C_Dungeon_GetChapterList.ParseFromString(data)
        # print(S2C_Dungeon_GetChapterList)

    # 副本战斗
    @seq_task(7)
    def Dungeon_ChallengeStageBegin(self):
        flag, data = MSG_C2S_Dungeon_ChallengeStageBegin(self)
        # S2C_Dungeon_ChallengeStageBegin = cs_pb2.S2C_Dungeon_ChallengeStageBegin()
        # S2C_Dungeon_ChallengeStageBegin.ParseFromString(data)
        # print(S2C_Dungeon_ChallengeStageBegin)

    # 获取排行榜
    @seq_task(8)
    def getrank(self):
        flag, data = MSG_C2S_GetCommonRankList(self)
        # S2C_GetCommonRankList = cs_pb2.S2C_GetCommonRankList()
        # S2C_GetCommonRankList.ParseFromString(data)
        # print(S2C_GetCommonRankList)

    # 名人堂
    @seq_task(9)
    def famerank(self):
        flag, data = MSG_C2S_HallOfFame_Rank(self)
        # S2C_HallOfFame_Rank = cs_pb2.S2C_HallOfFame_Rank()
        # S2C_HallOfFame_Rank.ParseFromString(data)
        # print(S2C_HallOfFame_Rank)
    """



class WorkLocust(Locust):
    task_set = WorkTaskSet
    min_wait = 1000
    max_wait = 2000

    def __init__(self):
        super(WorkLocust, self).__init__()
        host = "10.3.128.5"
        port = 16865
        self.client = create_connection((host, port))


if __name__ == '__main__':
    work = WorkLocust()
    work.run()
