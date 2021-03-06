# _*_coding:utf-8 _*_
# !/usr/bin/python3
# Reference:********************************
# encoding: utf-8
# @Time: 2019/11/20  12:08
# @Author: 洞洞
# @File: protocol_dic_test_ss2.py
# @Function:
# @Method:
# Reference:********************************

class ProtocolDicTestSs2:
    def __init__(self):
        self.protocol_ss2 = {
            2: ['{"message":10452', ',"recruit_type":', ',"consume_type":', ',"num":', '}'],
            3: ['{"message":10650', ',"mail_type":', '}'],
            4: ['{"message":10652', ',"mail_type":', ',"id":', '}'],
            5: ['{"message":10656', ',"mail_type":', ',"id":', '}'],
            6: ['{"message":10142', ',"channel":', ',"content":', ',"name":', '}'],
            7: ['{"message":12204', ',"share_type":', ',"own_id":', ',"id":', '}'],
            8: ['{"message":10655', ',"content":', ',"uid":', ',"name":', '}'],
            9: ['{"message":10908', ',"name":', '}'],
            10: ['{"message":10910', '}'],
            11: ['{"message":10912', ',"id":', '}'],
            12: ['{"message":10914', ',"id":', '}'],
            13: ['{"message":10916', ',"id":', ',"accept":', '}'],
            14: ['{"message":10918', ',"id":', '}'],
            15: ['{"message":10920', ',"id":', '}'],
            16: ['{"message":10924', ',"player_name":', '}'],
            17: ['{"message":10931', ',"id":', '}'],
            18: ['{"message":10200', ',"id":', '}'],
            19: ['{"message":10202', ',"id":', '}'],
            20: ['{"message":10206', ',"id":', '}'],
            21: ['{"message":10250', ',"id":', ',"item_id":', ',"item_num":', '}'],
            22: ['{"message":10252', ',"id":', ',"all_purpose_frag_num":', '}'],
            23: ['{"message":10254', ',"id":', ',"num":', '}'],
            24: ['{"message":10256', ',"id":', ',"confirm":', '}'],
            25: ['{"message":10258', ',"id":', '}'],
            26: ['{"message":10260', ',"id":', ',"pos":', '}'],
            27: ['{"message":10262', ',"id":', '}'],
            28: ['{"message":10264', ',"id":', ',"num":', ',"path_id":', '}'],
            29: ['{"message":10552', ',"id":', '}'],
            30: ['{"message":12100', ',"book_id":', '}'],
            31: ['{"message":12102', ',"advance_id":', '}'],
            32: ['{"message":10482', ',"rank":', '}'],
            33: ['{"message":10485', ',"num":', ',"rank":', '}'],
            35: ['{"message":10493', ',"type":', '}'],
            36: ['{"message":10512', ',"id":', '}'],
            37: ['{"message":10517', ',"shop_id":', ',"item_id":', '}'],
            38: ['{"message":10519', ',"index":', '}'],
            39: ['{"message":10572', ',"id":', '}'],
            40: ['{"message":10574', ',"id":', '}'],
            41: ['{"message":11250', ',"shop_id":', '}'],
            42: ['{"message":11252', ',"shop_id":', ',"flush_type":', '}'],
            43: ['{"message":11254', ',"shop_id":', ',"goods_type":', ',"index":', ',"num":', '}'],
            44: ['{"message":11282', ',"id":', '}'],
            45: ['{"message":11284', ',"id":', '}'],
            46: ['{"message":11300', ',"sys_type":', ',"op_type":', ',"ids":', '}'],
            47: ['{"message":11302', ',"sys_type":', ',"op_type":', ',"ids":', '}'],
            48: ['{"message":11502', ',"id":', '}'],
            49: ['{"message":11505', ',"id":', '}'],
            50: ['{"message":11425', ',"type":', '}'],
            51: ['{"message":11427', ',"type":', ',"like_id":', ',"like_num":', '}'],
            52: ['{"message":11404', ',"id":', '}'],
            53: ['{"message":11202', ',"id":', '}'],
            54: ['{"message":11205', ',"id":', '}'],
            55: ['{"message":11152', ',"uid":', ',"id":', ',"attack_type":', '}'],
            56: ['{"message":11155', ',"id":', '}'],
            57: ['{"message":11157', ',"id":', '}'],
            58: ['{"message":10972', ',"id":', '}'],
            59: ['{"message":10974', ',"id":', '}'],
            60: ['{"message":10952', ',"title_id":', '}'],
            61: ['{"message":10852', ',"id":', ',"knight_id":', ',"model_id":', '}'],
            62: ['{"message":10854', ',"id":', '}'],
            63: ['{"message":10858', ',"friend_id":', '}'],
            64: ['{"message":10860', ',"friend_id":', ',"city_id":', ',"truble_id":', ',"start_time":',
                 '}'],
            65: ['{"message":10800', ',"base_id":', '}'],
            66: ['{"message":10802', ',"id":', ',"base_id":', ',"skip_battle":', '}'],
            67: ['{"message":10805', ',"num":', ',"id":', ',"base_id":', '}'],
            68: ['{"message":10809', ',"id":', ',"buff":', '}'],
            69: ['{"message":10750', ',"id":', ',"consume_list":', '}'],
            71: ['{"message":10752', ',"id":', ',"consume_list":', '}'],
            72: ['{"message":10692', ',"id":', '}'],
            73: ['{"message":10696', ',"id":', ',"type":', '}'],
            74: ['{"message":10600', ',"id":', ',"times":', '}'],
            76: ['{"message":10266', ',"compose":', ',"equip":', '}'],
            77: ['{"message":10602', ',"id":', ',"item_id":', ',"num":', '}'],
            78: ['{"message":11000', ',"idex":', '}'],
            79: ['{"message":11002', ',"key":', '}'],
            80: ['{"message":11006', ',"name":', ',"icon":', ',"confirm":', ',"level":', '}'],
            81: ['{"message":11008', ',"guild_id":', '}'],
            82: ['{"message":11010', ',"apply_id":', ',"accept":', '}'],
            83: ['{"message":11012', ',"kick_id":', '}'],
            84: ['{"message":11018', ',"member_id":', ',"position":', '}'],
            85: ['{"message":11022', ',"start":', '}'],
            86: ['{"message":11024', ',"type":', ',"name":', ',"icon":', ',"frame":',
                 ',"apply_level":', ',"declaration":', ',"announcement":', ',"confirm":', '}'],
            87: ['{"message":11028', ',"message":', '}'],
            88: ['{"message":11030', ',"id":', ',"type":', '}'],
            89: ['{"message":11036', ',"guild_id":', '}'],
            90: ['{"message":11062', ',"id":', ',"num":', '}'],
            91: ['{"message":11064', ',"index":', '}'],
            92: ['{"message":11048', ',"member_id":', '}'],
            93: ['{"message":11052', ',"id":', '}'],
            94: ['{"message":11054', ',"id":', '}'],
            95: ['{"message":11056', ',"id":', '}'],
            96: ['{"message":11072', ',"chapter_id":', '}'],
            97: ['{"message":11074', ',"stage_id":', '}'],
            98: ['{"message":11079', ',"type":', ',"score":', '}'],
            99: ['{"message":11081', ',"chapter_id":', '}'],
            100: ['{"message":11083', ',"position":', ',"stage_id":', '}'],
            101: ['{"message":11085', ',"stage_id":', '}'],
            102: ['{"message":11088', ',"stage_id":', '}'],
            103: ['{"message":12152', ',"type":', ',"value":', ',"stone":', '}'],
            104: ['{"message":12154', ',"type":', '}'],
            105: ['{"message":12156', ',"pos":', '}'],
            106: ['{"message":10702', ',"id":', '}'],
            107: ['{"message":10705', ',"id":', ',"num":', '}'],
            108: ['{"message":10707', ',"id":', ',"tp":', '}'],
            109: ['{"message":10711', ',"id":', '}'],
            110: ['{"message":10713', ',"id":', '}'],
            111: ['{"message":10715', ',"id":', ',"teamId":', '}'],
            112: ['{"message":10717', ',"id":', ',"kick_id":', '}'],
            113: ['{"message":10719', ',"id":', '}'],
            114: ['{"message":10721', ',"id":', ',"prepare":', '}'],
            115: ['{"message":10723', ',"id":', '}'],
            116: ['{"message":10727', ',"id":', '}'],
            117: ['{"message":10729', ',"position_a":', ',"position_b":', '}'],
            118: ['{"message":10731', ',"id":', '}'],
            119: ['{"message":10733', ',"id":', ',"npc":', '}'],
            120: ['{"message":10735', ',"invitee_id":', ',"campaign_id":', '}'],
            121: ['{"message":10739', ',"team_id":', ',"join":', ',"campaign_id":', '}'],
            122: ['{"message":107341', ',"shield":', '}'],
            123: ['{"message":10743', ',"lock":', '}'],
            124: ['{"message":10477', ',"id":', '}'],
            125: ['{"message":10760', ',"id":', '}'],
            126: ['{"message":10749', ',"id":', '}'],
            127: ['{"message":10170', ',"id":', ',"size":', '}'],
            128: ['{"message":10174', ',"id":', ',"num":', '}'],
            129: ['{"message":11602', ',"id":', '}'],
            130: ['{"message":11802', ',"id":', '}'],
            131: ['{"message":11804', ',"ids":', '}'],
            132: ['{"message":11806', ',"id":', '}'],
            133: ['{"message":11808', ',"id":', ',"break_ids":', '}'],
            134: ['{"message":11822', ',"id":', '}'],
            136: ['{"message":11952', ',"id":', '}'],
            137: ['{"message":12002', ',"id":', '}'],
            138: ['{"message":11560', ',"id":', ',"index":', '}'],
            139: ['{"message":12202', ',"id":', '}'],
            140: ['{"message":12228', ',"activity_id":', ',"id":', '}'],
            141: ['{"message":12233', ',"activity_id":', ',"id":', '}'],
            142: ['{"message":12246', ',"activity_id":', ',"id":', '}'],
            143: ['{"message":12226', ',"id":', '}'],
            144: ['{"message":12304', ',"storm_id":', ',"cell_id":', '}'],
            145: ['{"message":12307', ',"storm_id":', ',"cell_id":', '}'],
            146: ['{"message":12309', ',"storm_id":', ',"cell_id":', '}'],
            147: ['{"message":12311', ',"storm_id":', '}'],
            148: ['{"message":12313', ',"storm_id":', '}'],
            149: ['{"message":12315', ',"storm_id":', ',"cell_ids":', '}'],
            150: ['{"message":12325', ',"id":', ',"tg_lv":', '}'],
            157: ['{"message":10422', ',"id":', ',"num":','}'],
            161: ['{"message":10162', ',"tp":', ',"pos":', ',"id":', '}'],
            163: ['{"message":10145', ',"client_time":', '}'], }

    def get_protocol_value(self, key_str):
        """
        根据传入的key，返回value
        :param key_str: kye
        :return: str value
        """
        return self.protocol_ss2.get(key_str)
