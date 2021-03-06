# _*_coding:utf-8 _*_
# !/usr/bin/python3
# Reference:********************************
# encoding: utf-8
# @Time: 2019/11/7  17:03
# @Author: 洞洞
# @File: message_ss2.py
# @Function:
# @Method:
# Reference:********************************
class MessageSs2:
    """
    3的后半段、10的军团红包、12的名将传道具、13武将变装
    """

    def __init__(self):
        self.resource = {"角色经验": '''"type":1,"value":1''',
                         "贵族经验": '''"type":1,"value":2''',
                         "银币": '''"type":1,"value":3''',
                         "体力值": '''"type":1,"value":4''',
                         "威名": '''"type":1,"value":6''',
                         "声望": '''"type":1,"value":8''',
                         "寻宝次数": '''"type":1,"value":9''',
                         "灵玉": '''"type":1,"value":10''',
                         "军团贡献": '''"type":1,"value":11''',
                         "征讨次数": '''"type":1,"value":12''',
                         "战功": '''"type":1,"value":13''',
                         "军武积分": '''"type":1,"value":14''',
                         "军团副本挑战次数": '''"type":1,"value":15''',
                         "将魂": '''"type":1,"value":16''',
                         "进阶饰品精华": '''"type":1,"value":17''',
                         "成就点数": '''"type":1,"value":19''',
                         "招贤币": '''"type":1,"value":20''',
                         "水": '''"type":1,"value":21''',
                         "勇气值": '''"type":1,"value":22''',
                         "月卡积分": '''"type":1,"value":23''',
                         "疲劳值": '''"type":1,"value":24''',
                         "军功": '''"type":1,"value":25''',
                         "技能点": '''"type":1,"value":26''',
                         "庆典积分": '''"type":1,"value":27''',
                         "神兵精魄": '''"type":1,"value":28''',
                         "列传次数": '''"type":1,"value":33''',
                         "粮草": '''"type":1,"value":34''',
                         "军令": '''"type":1,"value":35''',
                         "烈焰弓碎片": '''"type":2,"value":201''',
                         "烈焰鞋碎片": '''"type":2,"value":202''',
                         "烈焰甲碎片": '''"type":2,"value":203''',
                         "烈焰盔碎片": '''"type":2,"value":204''',
                         "寒光锤碎片": '''"type":2,"value":211''',
                         "寒光鞋碎片": '''"type":2,"value":212''',
                         "寒光甲碎片": '''"type":2,"value":213''',
                         "寒光盔碎片": '''"type":2,"value":214''',
                         "血战利斧碎片": '''"type":2,"value":301''',
                         "血战长靴碎片": '''"type":2,"value":302''',
                         "血战锁甲碎片": '''"type":2,"value":303''',
                         "血战头盔碎片": '''"type":2,"value":304''',
                         "破军战枪碎片": '''"type":2,"value":311''',
                         "破军长靴碎片": '''"type":2,"value":312''',
                         "破军锁甲碎片": '''"type":2,"value":313''',
                         "破军面甲碎片": '''"type":2,"value":314''',
                         "朱雀羽扇碎片": '''"type":2,"value":401''',
                         "朱雀步履碎片": '''"type":2,"value":402''',
                         "朱雀法袍碎片": '''"type":2,"value":403''',
                         "朱雀发冠碎片": '''"type":2,"value":404''',
                         "霸王神剑碎片": '''"type":2,"value":411''',
                         "霸王战靴碎片": '''"type":2,"value":412''',
                         "霸王重甲碎片": '''"type":2,"value":413''',
                         "霸王战盔碎片": '''"type":2,"value":414''',
                         "无双画戟碎片": '''"type":2,"value":421''',
                         "无双战靴碎片": '''"type":2,"value":422''',
                         "无双宝铠碎片": '''"type":2,"value":423''',
                         "无双金冠碎片": '''"type":2,"value":424''',
                         "三略碎片1": '''"type":2,"value":11011''',
                         "三略碎片2": '''"type":2,"value":11012''',
                         "三略碎片3": '''"type":2,"value":11013''',
                         "司马法碎片1": '''"type":2,"value":11021''',
                         "司马法碎片2": '''"type":2,"value":11022''',
                         "司马法碎片3": '''"type":2,"value":11023''',
                         "孙子兵法碎片1": '''"type":2,"value":11111''',
                         "孙子兵法碎片2": '''"type":2,"value":11112''',
                         "孙子兵法碎片3": '''"type":2,"value":11113''',
                         "孙子兵法碎片4": '''"type":2,"value":11114''',
                         "鬼谷子碎片1": '''"type":2,"value":11121''',
                         "鬼谷子碎片2": '''"type":2,"value":11122''',
                         "鬼谷子碎片3": '''"type":2,"value":11123''',
                         "鬼谷子碎片4": '''"type":2,"value":11124''',
                         "太平要术碎片1": '''"type":2,"value":11211''',
                         "太平要术碎片2": '''"type":2,"value":11212''',
                         "太平要术碎片3": '''"type":2,"value":11213''',
                         "太平要术碎片4": '''"type":2,"value":11214''',
                         "太平要术碎片5": '''"type":2,"value":11215''',
                         "孟德新书碎片1": '''"type":2,"value":11321''',
                         "孟德新书碎片2": '''"type":2,"value":11322''',
                         "孟德新书碎片3": '''"type":2,"value":11323''',
                         "孟德新书碎片4": '''"type":2,"value":11324''',
                         "孟德新书碎片5": '''"type":2,"value":11325''',
                         "县令印碎片1": '''"type":2,"value":12011''',
                         "县令印碎片2": '''"type":2,"value":12012''',
                         "县令印碎片3": '''"type":2,"value":12013''',
                         "主薄印碎片1": '''"type":2,"value":12021''',
                         "主薄印碎片2": '''"type":2,"value":12022''',
                         "主薄印碎片3": '''"type":2,"value":12023''',
                         "太尉印碎片1": '''"type":2,"value":12111''',
                         "太尉印碎片2": '''"type":2,"value":12112''',
                         "太尉印碎片3": '''"type":2,"value":12113''',
                         "太尉印碎片4": '''"type":2,"value":12114''',
                         "御史印碎片1": '''"type":2,"value":12121''',
                         "御史印碎片2": '''"type":2,"value":12122''',
                         "御史印碎片3": '''"type":2,"value":12123''',
                         "御史印碎片4": '''"type":2,"value":12124''',
                         "将军印碎片1": '''"type":2,"value":12211''',
                         "将军印碎片2": '''"type":2,"value":12212''',
                         "将军印碎片3": '''"type":2,"value":12213''',
                         "将军印碎片4": '''"type":2,"value":12214''',
                         "将军印碎片5": '''"type":2,"value":12215''',
                         "丞相印碎片1": '''"type":2,"value":12321''',
                         "丞相印碎片2": '''"type":2,"value":12322''',
                         "丞相印碎片3": '''"type":2,"value":12323''',
                         "丞相印碎片4": '''"type":2,"value":12324''',
                         "丞相印碎片5": '''"type":2,"value":12325''',
                         "鱼符碎片1": '''"type":2,"value":13011''',
                         "鱼符碎片2": '''"type":2,"value":13012''',
                         "鱼符碎片3": '''"type":2,"value":13013''',
                         "雀符碎片1": '''"type":2,"value":13021''',
                         "雀符碎片2": '''"type":2,"value":13022''',
                         "雀符碎片3": '''"type":2,"value":13023''',
                         "雀符碎片4": '''"type":2,"value":13024''',
                         "虎符碎片1": '''"type":2,"value":13031''',
                         "虎符碎片2": '''"type":2,"value":13032''',
                         "虎符碎片3": '''"type":2,"value":13033''',
                         "虎符碎片4": '''"type":2,"value":13034''',
                         "虎符碎片5": '''"type":2,"value":13035''',
                         "定军刀碎片": '''"type":2,"value":21010''',
                         "曲燕碎片": '''"type":2,"value":21020''',
                         "霸王手戟碎片": '''"type":2,"value":22010''',
                         "松纹古锭刀碎片": '''"type":2,"value":22020''',
                         "诸葛连弩碎片": '''"type":2,"value":22030''',
                         "雌雄双股剑碎片": '''"type":2,"value":22040''',
                         "墨羽扇碎片": '''"type":2,"value":22050''',
                         "火云剑碎片": '''"type":2,"value":22060''',
                         "丈八蛇矛碎片": '''"type":2,"value":23010''',
                         "龙胆亮银枪碎片": '''"type":2,"value":23020''',
                         "青釭剑碎片": '''"type":2,"value":23030''',
                         "七星宝刀碎片": '''"type":2,"value":23040''',
                         "闭月团扇碎片": '''"type":2,"value":23050''',
                         "苍叶绿绮琴碎片": '''"type":2,"value":23060''',
                         "红颜符碎片": '''"type":2,"value":40010''',
                         "凤鸣符碎片": '''"type":2,"value":40020''',
                         "战象符碎片": '''"type":2,"value":40030''',
                         "撼天符碎片": '''"type":2,"value":40040''',
                         "双枪符碎片": '''"type":2,"value":40050''',
                         "冰封符碎片": '''"type":2,"value":40060''',
                         "截江符碎片": '''"type":2,"value":40070''',
                         "血屠符碎片": '''"type":2,"value":40080''',
                         "狂熊符碎片": '''"type":2,"value":40090''',
                         "地刺符碎片": '''"type":2,"value":40100''',
                         "悍勇符碎片": '''"type":2,"value":40110''',
                         "寒冰裂符碎片": '''"type":2,"value":50010''',
                         "枪剑合符碎片": '''"type":2,"value":50020''',
                         "万箭发符碎片": '''"type":2,"value":50030''',
                         "巨刃斩符碎片": '''"type":2,"value":50040''',
                         "救苍生符碎片": '''"type":2,"value":50050''',
                         "雷龙暴符碎片": '''"type":2,"value":50060''',
                         "豪情志符碎片": '''"type":2,"value":50070''',
                         "铁蹄踏符碎片": '''"type":2,"value":50080''',
                         "皓月名符碎片": '''"type":2,"value":50090''',
                         "荼毒咒符碎片": '''"type":2,"value":50100''',
                         "火蛇舞符碎片": '''"type":2,"value":50110''',
                         "双骄媚符碎片": '''"type":2,"value":50120''',
                         "虎骑冲符碎片": '''"type":2,"value":50130''',
                         "双凤鸣符碎片": '''"type":2,"value":50140''',
                         "山崩地裂符碎片": '''"type":2,"value":50150''',
                         "月影蝶舞符碎片": '''"type":2,"value":50160''',
                         "魔灵咆哮符碎片": '''"type":2,"value":50170''',
                         "神勇无双符碎片": '''"type":2,"value":50180''',
                         "于禁碎片": '''"type":2,"value":400010''',
                         "曹丕碎片": '''"type":2,"value":400020''',
                         "乐进碎片": '''"type":2,"value":400030''',
                         "庞德碎片": '''"type":2,"value":400040''',
                         "步练师碎片": '''"type":2,"value":400050''',
                         "孟获碎片": '''"type":2,"value":400060''',
                         "祝融碎片": '''"type":2,"value":400070''',
                         "法正碎片": '''"type":2,"value":400080''',
                         "程普碎片": '''"type":2,"value":400090''',
                         "周泰碎片": '''"type":2,"value":400100''',
                         "黄盖碎片": '''"type":2,"value":400110''',
                         "徐盛碎片": '''"type":2,"value":400120''',
                         "孙尚香碎片": '''"type":2,"value":400130''',
                         "颜良碎片": '''"type":2,"value":400140''',
                         "文丑碎片": '''"type":2,"value":400150''',
                         "陈宫碎片": '''"type":2,"value":400160''',
                         "甄姬碎片": '''"type":2,"value":500010''',
                         "张辽碎片": '''"type":2,"value":500020''',
                         "许褚碎片": '''"type":2,"value":500030''',
                         "夏侯惇碎片": '''"type":2,"value":500040''',
                         "夏侯渊碎片": '''"type":2,"value":500050''',
                         "张郃碎片": '''"type":2,"value":500060''',
                         "庞统碎片": '''"type":2,"value":500070''',
                         "张飞碎片": '''"type":2,"value":500080''',
                         "黄忠碎片": '''"type":2,"value":500090''',
                         "魏延碎片": '''"type":2,"value":500100''',
                         "马超碎片": '''"type":2,"value":500110''',
                         "姜维碎片": '''"type":2,"value":500120''',
                         "大乔碎片": '''"type":2,"value":500130''',
                         "孙权碎片": '''"type":2,"value":500140''',
                         "孙坚碎片": '''"type":2,"value":500150''',
                         "吕蒙碎片": '''"type":2,"value":500160''',
                         "太史慈碎片": '''"type":2,"value":500170''',
                         "鲁肃碎片": '''"type":2,"value":500180''',
                         "华佗碎片": '''"type":2,"value":500190''',
                         "袁绍碎片": '''"type":2,"value":500200''',
                         "于吉碎片": '''"type":2,"value":500210''',
                         "华雄碎片": '''"type":2,"value":500220''',
                         "董卓碎片": '''"type":2,"value":500230''',
                         "公孙瓒碎片": '''"type":2,"value":500240''',
                         "郭嘉碎片": '''"type":2,"value":510010''',
                         "典韦碎片": '''"type":2,"value":510020''',
                         "刘备碎片": '''"type":2,"value":510030''',
                         "赵云碎片": '''"type":2,"value":510040''',
                         "陆逊碎片": '''"type":2,"value":510050''',
                         "小乔碎片": '''"type":2,"value":510060''',
                         "贾诩碎片": '''"type":2,"value":510070''',
                         "貂蝉碎片": '''"type":2,"value":510080''',
                         "体力丹": '''"type":3,"value":1''',
                         "培养丹": '''"type":3,"value":2''',
                         "普通招将令": '''"type":3,"value":5''',
                         "高级招将令": '''"type":3,"value":6''',
                         "下品经验书": '''"type":3,"value":7''',
                         "中品经验书": '''"type":3,"value":8''',
                         "上品经验书": '''"type":3,"value":9''',
                         "极品经验书": '''"type":3,"value":10''',
                         "进阶石": '''"type":3,"value":11''',
                         "初级精炼石": '''"type":3,"value":12''',
                         "中级精炼石": '''"type":3,"value":13''',
                         "高级精炼石": '''"type":3,"value":14''',
                         "顶级精炼石": '''"type":3,"value":15''',
                         "竞技场挑战令": '''"type":3,"value":16''',
                         "宝物精炼石": '''"type":3,"value":17''',
                         "免战令小": '''"type":3,"value":18''',
                         "免战令大": '''"type":3,"value":19''',
                         "寻宝令": '''"type":3,"value":20''',
                         "橙将万能碎片": '''"type":3,"value":21''',
                         "红将万能碎片": '''"type":3,"value":22''',
                         "金将万能碎片": '''"type":3,"value":23''',
                         "主线残卷": '''"type":3,"value":24''',
                         "巨兽讨伐令": '''"type":3,"value":25''',
                         "时装精华": '''"type":3,"value":26''',
                         "橙兵符万能碎片": '''"type":3,"value":27''',
                         "红兵符万能碎片": '''"type":3,"value":28''',
                         "金兵符万能碎片": '''"type":3,"value":29''',
                         "武将刷新令": '''"type":3,"value":30''',
                         "兵符铸造石": '''"type":3,"value":32''',
                         "银两箱": '''"type":3,"value":33''',
                         "虎符宝物箱": '''"type":3,"value":34''',
                         "兵符精华": '''"type":3,"value":35''',
                         "列传残卷": '''"type":3,"value":36''',
                         "图鉴升级卷轴": '''"type":3,"value":37''',
                         "现世招将令": '''"type":3,"value":38''',
                         "铸像石": '''"type":3,"value":39''',
                         "6元充值额度": '''"type":3,"value":40''',
                         "30元充值额度": '''"type":3,"value":41''',
                         "60元充值额度": '''"type":3,"value":42''',
                         "98元充值额度": '''"type":3,"value":43''',
                         "198元充值额度": '''"type":3,"value":44''',
                         "328元充值额度": '''"type":3,"value":45''',
                         "648元充值额度": '''"type":3,"value":46''',
                         "普通装备纹晶": '''"type":3,"value":47''',
                         "高级装备纹晶": '''"type":3,"value":48''',
                         "普通宝物纹晶": '''"type":3,"value":49''',
                         "高级宝物纹晶": '''"type":3,"value":50''',
                         "神兵令": '''"type":3,"value":51''',
                         "神兵令刷新令": '''"type":3,"value":52''',
                         "千军令": '''"type":3,"value":53''',
                         "金斧子": '''"type":3,"value":54''',
                         "银斧子": '''"type":3,"value":55''',
                         "神兵铸造石": '''"type":3,"value":56''',
                         "金将令": '''"type":3,"value":57''',
                         "霸服头像框": '''"type":3,"value":58''',
                         "化身符纸": '''"type":3,"value":59''',
                         "荣耀头像框": '''"type":3,"value":60''',
                         "星辰符石": '''"type":3,"value":61''',
                         "月辉符石": '''"type":3,"value":62''',
                         "日曜符石": '''"type":3,"value":63''',
                         "神意符石": '''"type":3,"value":64''',
                         "于禁": '''"type":4,"value":400010''',
                         "曹丕": '''"type":4,"value":400020''',
                         "乐进": '''"type":4,"value":400030''',
                         "庞德": '''"type":4,"value":400040''',
                         "步练师": '''"type":4,"value":400050''',
                         "孟获": '''"type":4,"value":400060''',
                         "祝融": '''"type":4,"value":400070''',
                         "法正": '''"type":4,"value":400080''',
                         "程普": '''"type":4,"value":400090''',
                         "周泰": '''"type":4,"value":400100''',
                         "黄盖": '''"type":4,"value":400110''',
                         "徐盛": '''"type":4,"value":400120''',
                         "孙尚香": '''"type":4,"value":400130''',
                         "颜良": '''"type":4,"value":400140''',
                         "文丑": '''"type":4,"value":400150''',
                         "陈宫": '''"type":4,"value":400160''',
                         "甄姬": '''"type":4,"value":500010''',
                         "张辽": '''"type":4,"value":500020''',
                         "许褚": '''"type":4,"value":500030''',
                         "夏侯惇": '''"type":4,"value":500040''',
                         "夏侯渊": '''"type":4,"value":500050''',
                         "张郃": '''"type":4,"value":500060''',
                         "庞统": '''"type":4,"value":500070''',
                         "张飞": '''"type":4,"value":500080''',
                         "黄忠": '''"type":4,"value":500090''',
                         "魏延": '''"type":4,"value":500100''',
                         "马超": '''"type":4,"value":500110''',
                         "姜维": '''"type":4,"value":500120''',
                         "大乔": '''"type":4,"value":500130''',
                         "孙权": '''"type":4,"value":500140''',
                         "孙坚": '''"type":4,"value":500150''',
                         "吕蒙": '''"type":4,"value":500160''',
                         "太史慈": '''"type":4,"value":500170''',
                         "鲁肃": '''"type":4,"value":500180''',
                         "华佗": '''"type":4,"value":500190''',
                         "袁绍": '''"type":4,"value":500200''',
                         "于吉": '''"type":4,"value":500210''',
                         "华雄": '''"type":4,"value":500220''',
                         "董卓": '''"type":4,"value":500230''',
                         "公孙瓒": '''"type":4,"value":500240''',
                         "郭嘉": '''"type":4,"value":510010''',
                         "典韦": '''"type":4,"value":510020''',
                         "刘备": '''"type":4,"value":510030''',
                         "赵云": '''"type":4,"value":510040''',
                         "陆逊": '''"type":4,"value":510050''',
                         "小乔": '''"type":4,"value":510060''',
                         "贾诩": '''"type":4,"value":510070''',
                         "貂蝉": '''"type":4,"value":510080''',
                         "红颜符": '''"type":5,"value":40010''',
                         "凤鸣符": '''"type":5,"value":40020''',
                         "战象符": '''"type":5,"value":40030''',
                         "撼天符": '''"type":5,"value":40040''',
                         "双枪符": '''"type":5,"value":40050''',
                         "冰封符": '''"type":5,"value":40060''',
                         "截江符": '''"type":5,"value":40070''',
                         "雷霆符": '''"type":5,"value":40080''',
                         "狂熊符": '''"type":5,"value":40090''',
                         "地刺符": '''"type":5,"value":40100''',
                         "悍勇符": '''"type":5,"value":40110''',
                         "寒冰裂符": '''"type":5,"value":50010''',
                         "枪剑合符": '''"type":5,"value":50020''',
                         "万箭发符": '''"type":5,"value":50030''',
                         "巨刃斩符": '''"type":5,"value":50040''',
                         "救苍生符": '''"type":5,"value":50050''',
                         "雷龙暴符": '''"type":5,"value":50060''',
                         "豪情志符": '''"type":5,"value":50070''',
                         "铁蹄踏符": '''"type":5,"value":50080''',
                         "皓月明符": '''"type":5,"value":50090''',
                         "荼毒咒符": '''"type":5,"value":50100''',
                         "火蛇舞符": '''"type":5,"value":50110''',
                         "双骄媚符": '''"type":5,"value":50120''',
                         "虎骑冲符": '''"type":5,"value":50130''',
                         "双凤鸣符": '''"type":5,"value":50140''',
                         "山崩地裂符": '''"type":5,"value":50150''',
                         "月影蝶舞符": '''"type":5,"value":50160''',
                         "魔灵咆哮符": '''"type":5,"value":50170''',
                         "神勇无双符": '''"type":5,"value":50180''',
                         "燕辞戒+1": '''"type":6,"value":1''',
                         "燕辞链+1": '''"type":6,"value":2''',
                         "燕辞镯+1": '''"type":6,"value":3''',
                         "燕辞佩+1": '''"type":6,"value":4''',
                         "燕辞戒+2": '''"type":6,"value":5''',
                         "燕辞链+2": '''"type":6,"value":6''',
                         "燕辞镯+2": '''"type":6,"value":7''',
                         "燕辞佩+2": '''"type":6,"value":8''',
                         "燕辞戒+3": '''"type":6,"value":9''',
                         "燕辞链+3": '''"type":6,"value":10''',
                         "燕辞镯+3": '''"type":6,"value":11''',
                         "燕辞佩+3": '''"type":6,"value":12''',
                         "惊雷戒+1": '''"type":6,"value":13''',
                         "惊雷链+1": '''"type":6,"value":14''',
                         "惊雷镯+1": '''"type":6,"value":15''',
                         "惊雷佩+1": '''"type":6,"value":16''',
                         "惊雷戒+2": '''"type":6,"value":17''',
                         "惊雷链+2": '''"type":6,"value":18''',
                         "惊雷镯+2": '''"type":6,"value":19''',
                         "惊雷佩+2": '''"type":6,"value":20''',
                         "惊雷戒+3": '''"type":6,"value":21''',
                         "惊雷链+3": '''"type":6,"value":22''',
                         "惊雷镯+3": '''"type":6,"value":23''',
                         "惊雷佩+3": '''"type":6,"value":24''',
                         "烈焰戒+1": '''"type":6,"value":25''',
                         "烈焰链+1": '''"type":6,"value":26''',
                         "烈焰镯+1": '''"type":6,"value":27''',
                         "烈焰佩+1": '''"type":6,"value":28''',
                         "烈焰戒+2": '''"type":6,"value":29''',
                         "烈焰链+2": '''"type":6,"value":30''',
                         "烈焰镯+2": '''"type":6,"value":31''',
                         "烈焰佩+2": '''"type":6,"value":32''',
                         "烈焰戒+3": '''"type":6,"value":33''',
                         "烈焰链+3": '''"type":6,"value":34''',
                         "烈焰镯+3": '''"type":6,"value":35''',
                         "烈焰佩+3": '''"type":6,"value":36''',
                         "飞龙出云戒+1": '''"type":6,"value":37''',
                         "飞龙出云链+1": '''"type":6,"value":38''',
                         "飞龙出云镯+1": '''"type":6,"value":39''',
                         "飞龙出云佩+1": '''"type":6,"value":40''',
                         "飞龙出云戒+2": '''"type":6,"value":41''',
                         "飞龙出云链+2": '''"type":6,"value":42''',
                         "飞龙出云镯+2": '''"type":6,"value":43''',
                         "飞龙出云佩+2": '''"type":6,"value":44''',
                         "飞龙出云戒+3": '''"type":6,"value":45''',
                         "飞龙出云链+3": '''"type":6,"value":46''',
                         "飞龙出云镯+3": '''"type":6,"value":47''',
                         "飞龙出云佩+3": '''"type":6,"value":48''',
                         "火凤飞星戒+1": '''"type":6,"value":49''',
                         "火凤飞星链+1": '''"type":6,"value":50''',
                         "火凤飞星镯+1": '''"type":6,"value":51''',
                         "火凤飞星佩+1": '''"type":6,"value":52''',
                         "火凤飞星戒+2": '''"type":6,"value":53''',
                         "火凤飞星链+2": '''"type":6,"value":54''',
                         "火凤飞星镯+2": '''"type":6,"value":55''',
                         "火凤飞星佩+2": '''"type":6,"value":56''',
                         "火凤飞星戒+3": '''"type":6,"value":57''',
                         "火凤飞星链+3": '''"type":6,"value":58''',
                         "火凤飞星镯+3": '''"type":6,"value":59''',
                         "火凤飞星佩+3": '''"type":6,"value":60''',
                         "苍龙补天戒+1": '''"type":6,"value":61''',
                         "苍龙补天链+1": '''"type":6,"value":62''',
                         "苍龙补天镯+1": '''"type":6,"value":63''',
                         "苍龙补天佩+1": '''"type":6,"value":64''',
                         "苍龙补天戒+2": '''"type":6,"value":65''',
                         "苍龙补天链+2": '''"type":6,"value":66''',
                         "苍龙补天镯+2": '''"type":6,"value":67''',
                         "苍龙补天佩+2": '''"type":6,"value":68''',
                         "苍龙补天戒+3": '''"type":6,"value":69''',
                         "苍龙补天链+3": '''"type":6,"value":70''',
                         "苍龙补天镯+3": '''"type":6,"value":71''',
                         "苍龙补天佩+3": '''"type":6,"value":72''',
                         "饰品合成卷轴": '''"type":6,"value":73''',
                         "测试战戟": '''"type":7,"value":1''',
                         "测试战靴": '''"type":7,"value":2''',
                         "测试战甲": '''"type":7,"value":3''',
                         "测试头盔": '''"type":7,"value":4''',
                         "百炼刀": '''"type":7,"value":101''',
                         "百炼靴": '''"type":7,"value":102''',
                         "百炼甲": '''"type":7,"value":103''',
                         "百炼盔": '''"type":7,"value":104''',
                         "烈焰弓": '''"type":7,"value":201''',
                         "烈焰鞋": '''"type":7,"value":202''',
                         "烈焰甲": '''"type":7,"value":203''',
                         "烈焰盔": '''"type":7,"value":204''',
                         "寒光锤": '''"type":7,"value":211''',
                         "寒光靴": '''"type":7,"value":212''',
                         "寒光甲": '''"type":7,"value":213''',
                         "寒光盔": '''"type":7,"value":214''',
                         "血战利斧": '''"type":7,"value":301''',
                         "血战长靴": '''"type":7,"value":302''',
                         "血战锁甲": '''"type":7,"value":303''',
                         "血战头盔": '''"type":7,"value":304''',
                         "破军战枪": '''"type":7,"value":311''',
                         "破军长靴": '''"type":7,"value":312''',
                         "破军锁甲": '''"type":7,"value":313''',
                         "破军面甲": '''"type":7,"value":314''',
                         "朱雀羽扇": '''"type":7,"value":401''',
                         "朱雀步履": '''"type":7,"value":402''',
                         "朱雀法袍": '''"type":7,"value":403''',
                         "朱雀发冠": '''"type":7,"value":404''',
                         "霸王神剑": '''"type":7,"value":411''',
                         "霸王战靴": '''"type":7,"value":412''',
                         "霸王重甲": '''"type":7,"value":413''',
                         "霸王战盔": '''"type":7,"value":414''',
                         "无双画戟": '''"type":7,"value":421''',
                         "无双战靴": '''"type":7,"value":422''',
                         "无双宝铠": '''"type":7,"value":423''',
                         "无双金冠": '''"type":7,"value":424''',
                         "三略": '''"type":8,"value":11010''',
                         "司马法": '''"type":8,"value":11020''',
                         "孙子兵法": '''"type":8,"value":11110''',
                         "鬼谷子": '''"type":8,"value":11120''',
                         "太平要术": '''"type":8,"value":11210''',
                         "孟德新书": '''"type":8,"value":11320''',
                         "县令印": '''"type":8,"value":12010''',
                         "主薄印": '''"type":8,"value":12020''',
                         "太尉印": '''"type":8,"value":12110''',
                         "御史印": '''"type":8,"value":12120''',
                         "将军印": '''"type":8,"value":12210''',
                         "丞相印": '''"type":8,"value":12320''',
                         "经验鱼符": '''"type":8,"value":13010''',
                         "经验雀符": '''"type":8,"value":13020''',
                         "经验虎符": '''"type":8,"value":13030''',
                         "世家子弟": '''"type":9,"value":38''',
                         "名门望族": '''"type":9,"value":39''',
                         "皇室贵胄": '''"type":9,"value":40''',
                         "天命之子": '''"type":9,"value":41''',
                         "一掷千金": '''"type":9,"value":42''',
                         "乐善好施": '''"type":9,"value":43''',
                         "博施济众": '''"type":9,"value":44''',
                         "兼济天下": '''"type":9,"value":45''',
                         "少年得志": '''"type":9,"value":46''',
                         "中流砥柱": '''"type":9,"value":47''',
                         "运筹帷幄": '''"type":9,"value":48''',
                         "功成名就": '''"type":9,"value":49''',
                         "骁骑之团": '''"type":9,"value":50''',
                         "虎狼之旅": '''"type":9,"value":51''',
                         "百战之师": '''"type":9,"value":52''',
                         "王者之军": '''"type":9,"value":53''',
                         "剑客": '''"type":11,"value":100''',
                         "狂斧": '''"type":11,"value":200''',
                         "银枪": '''"type":11,"value":300''',
                         "夜叉": '''"type":11,"value":400''',
                         "神射": '''"type":11,"value":500''',
                         "猛将": '''"type":11,"value":600''',
                         "天师": '''"type":11,"value":700''',
                         "定军刀": '''"type":14,"value":1010''',
                         "曲燕": '''"type":14,"value":1020''',
                         "霸王手戟": '''"type":14,"value":2010''',
                         "松纹古定刀": '''"type":14,"value":2020''',
                         "雌雄双股剑": '''"type":14,"value":2030''',
                         "诸葛连弩": '''"type":14,"value":2040''',
                         "墨羽扇": '''"type":14,"value":2050''',
                         "火云剑": '''"type":14,"value":2060''',
                         "丈八蛇矛": '''"type":14,"value":3010''',
                         "龙胆亮银枪": '''"type":14,"value":3020''',
                         "青釭剑": '''"type":14,"value":3030''',
                         "七星宝刀": '''"type":14,"value":3040''',
                         "闭月团扇": '''"type":14,"value":3050''',
                         "苍叶绿绮琴": '''"type":14,"value":3060''',
                         "元宝": '''"type":999,"value":0''',
                         "测试属性": '''"type":1,"value":1001''',
                         "巨猿": '''"type":17,"value":1010''',
                         "猞猁": '''"type":17,"value":2010''',
                         "机关鸟": '''"type":17,"value":3010''',
                         "机关牛": '''"type":17,"value":3020''',
                         "神木青鸾": '''"type":17,"value":4010''',
                         "撼地灵犀": '''"type":17,"value":4020''',

                         }
    def get_resource_value(self,key_str):
        """
        根据传入的key，返回value
        :param key_str: kye
        :return: str value
        """
        return self.resource.get(key_str)