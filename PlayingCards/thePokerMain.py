# -*- coding: UTF-8

'''  主 类, 发牌 及 计算 目前 金额(用于后续惩罚) 比如 每家 1000金币, 余额 与 所出额度, 入 额度; 一个月 抽成, 卖道具.等级以及 匹配 对手.'''
''' note1{ 
说话, 信还是不信, 过还是等会儿. 
}

'''

'''出牌状态(能出牌, 但是不能吹牛(note1)), 说话状态 '''

'''判断类1, 调用类 : 判断 到哪家说话. 记录, 哪家刚出牌( 记录状态, ).  '''

'''判断类2 : 判断 说 不信的人的话, 是否正确. 正确则 惩罚 出牌人且修改出牌人 出牌状态, '''

''''''

#encoding=utf-8
import time

'''  吹牛斗地主 '''

BiddingListPoker = ['8', '9', '10', 'J', 'Q']

OutToListPoker = ['3', '4', '5', '6', '7']

def OutTheP(OutP=[], fOutP=[], is_EnableO = '', who = []):
    '''    Bidding and bidding,
            检查当前玩家, 能否出牌.
            OutP:手中能出的牌
            fOutP: 叫牌;
            展示叫牌, 牌
    '''
    if is_EnableO:
        print('谁在出牌', who)
        print("出牌", OutP)
        print("叫牌", fOutP)
        print("输出 fOutP, 与 OutP", '\n等待 下面两家说话')
        return OutP, fOutP

    else:
        print(who, '出牌未到你出牌, 请等待')
    pass

def enableSpeak():
    '''    判断当前玩家能否说话
    '''
    pass

def enableOutP():
    pass

CPlist = []
VPlist = []
BPlist = []


speakToE = ['过', '不要', '要不起', '不信']
speakToWait = ['等我半分钟啊'] # 普通玩家, 只能 使用 3次/单局
speakToWaitAminute = ['等我一分钟啊'] # VIP玩家, 使用 3次/单局

def noteWheel(speakWho=str()):
    '''
    记录 谁说话,
    说的是什么,(出牌的话, 出的是什么)
    下一个 预计是谁
    :return:
    '''
    print(speakWho)
    pass

def assertThePoker(is_assert = 'ABC', OutP1=OutToListPoker, fOutP1=BiddingListPoker):
    '''
    验证结果是否正确 信不信
    Verify that the results are correct 
    '''
    s1, s2 = OutTheP(OutP=OutP1, fOutP=fOutP1, is_EnableO='', who=['Xwho'])
    x = 0
    if s1 == s2:
        print("断言错误, 惩罚 说话者")
        x = 1
    else:
        x = 2
        print("断言正确, 惩罚 出牌者, 奖励 说话者")
    pass
