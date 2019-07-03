# encoding=utf-8
import time

'''  吹牛斗地主 

        1. 检测谁能出牌. 记录谁 刚出牌.123452

        Number of rounds of play(出牌轮数): NrPlay
        Playing status(出牌状态):PlayingS

        Note:

            入场, WeChat1, WeChat2, WeChat3(QQ1, QQ2, QQ3),

            用户信息表:
                手机号, 绑定 WeChat
                手机号, 绑定 QQ
                手机号, 绑定, 姓名, 绑定 WeChat(QQ), 绑定身份证, 绑定银行卡. 绑定支付宝号.

                绑定验证, 
                    短信验证, 银行卡验证;


        demo:

        Nstep0:
            userid = {
            WeChat1:[v1, 1263, 124],
            WeChat2:[v2, 1263, 124],
            WeChat3:[v3, 1263, 124]            
            }
            ss11 = {'v':1, 'playCards':['v1所有的牌'], 'NrPlay':1, 'PlayingS':1}
            v:1, 表示出牌人的身份. 
            NrPlay 表示本轮 能否出牌. PlayingS表示本轮, 能够说话 

        Nstep_1:开局, 发牌;
            每人17张, 底牌三张,            
            排序. 分配给 三个人;
            每人17张, 排序. 分配给 三个人;

            初次发牌后, 每个人有 18张牌;
            方块三拥有者, 可以出牌; 本次为 第一轮;
            
            ss11 = {'v': 1, 'playCards': ['3', '3', '3', 'Q', 'Q'], 'NrPlay': 1, 'PlayingS': 1, 'speakError': 5, 'speakTrue': 5}
            ss11:表示出牌人为 v:1, 也就是 vplay1
            PlayingS [0,1,2] ;{0, 表示未说话. 可出牌或['不要', '过', '要不起']}, {1,表示已经说话}
            
'''

ss11 = {'v': 1, 'playCards': ['3', '3', '3', 'Q', 'Q'], 'NrPlay': 1, 'PlayingS': 1, 'speakError': 5, 'speakTrue': 5}
ss12 = {'v': 1, 'playCards': ['5', '6', '7', '8', '9', '10'], 'NrPlay': 1, 'PlayingS': 0, 'speakError': 4, 'speakTrue': 5}
ss13 = {'v': 1, 'playCards': ['6'], 'NrPlay': 1, 'PlayingS': 0}

sss13 = {'v': 1, 'playCards': ['4', '4', '4', '3'], 'NrPlay': 1, 'PlayingS': 0, 'speakError': 4, 'speakTrue': 5}


print(ss11['playCards'])
print(ss11['playCards'].clear())
print(ss11)
print(ss11['playCards'])
print('''ss11['NrPlay']''', ss11['NrPlay'])

print('检测,结束一家后 谁牌多, 谁能出牌')
def checkLen(k1=[], k2=[]):
    slist1 = k1
    slist2 = k2
    len1 = len(list(slist1['playCards']))
    len2 = len(list(slist2['playCards']))
    print('len1', len1)
    print('len2', len2)
    print('1_speakError + speakTrue', slist1['speakError'] + slist1['speakTrue'])
    print('2_speakError + speakTrue', slist2['speakError'] + slist2['speakTrue'] )

    if len1 > len2:
        slist1['NrPlay'] = 1
        print('len1 > len2')
    elif len1 < len2:
        slist2['NrPlay'] = 1
        print('len1 < len2')
    elif len2 == len1:
        print('len1 == len2')
        if slist1['speakError'] + slist1['speakTrue'] > slist2['speakError'] + slist2['speakTrue']:
            print('slist1 NrPlay=1')
        elif slist1['speakError'] + slist1['speakTrue'] < slist2['speakError'] + slist2['speakTrue']:
            print('slist2 NrPlay=1')
        else:
            print(''' print('slist1 NrPlay=1')''')
            pass

    pass

ss112 = {'v': 1, 'playCards': ['3', '3', '3', 'Q', 'Q'], 'NrPlay': 1, 'PlayingS': 1, 'speakError': 5, 'speakTrue': 5}
ss121 = {'v': 1, 'playCards': ['5', '6', '7', '8', '9', '10'], 'NrPlay': 1, 'PlayingS': 0, 'speakError': 4, 'speakTrue': 5}
ss132 = {'v': 1, 'playCards': ['6'], 'NrPlay': 1, 'PlayingS': 0}
sss132 = {'v': 1, 'playCards': ['4', '4', '4', '3', '9', '10'], 'NrPlay': 1, 'PlayingS': 0, 'speakError': 5, 'speakTrue': 5}
checkLen(k1=sss132, k2=ss121)

print(" 判断, 谁家出牌, 谁能出牌")
print('记录, 本轮谁出牌, 出了什么牌, 谁说了什么话')
print('移除 出掉的牌')
print('恢复 出掉的牌')

def checkWho(value=int()):

    pass

def checkStart3(v1=[], v2=[], v3=[]):
    '''
    :param v1: 
    :param v2: 
    :param v3: 
    :return: 检测 谁有 方块3. 有方块3的人, 可以 出牌. 其余两家, 可以说话. 根据顺序, 下家 可以叫牌;
    '''
    print('return 三家的 排好序的, 设置好出牌规则的, 说话人, 出牌人 的三个 字典, 同时 ')
    if ('3', '方片', 'blackCover') in v1:
        print('v1 出牌. 设置 v1 的 出牌机会= 1, 叫牌机会=1, 说话=0')
        print('顺时针, 轮转顺序, 设置 下一家v2 出牌机会= 0, 叫牌机会=1, 说话=1')
        print('顺时针, 轮转顺序, 设置 下下一家v3 出牌机会= 0, 叫牌机会=0, 说话=1')
    elif ('3', '方片', 'blackCover') in v2:
        print('v2 出牌. 设置 v2 的 出牌机会= 1, 叫牌机会=1, 说话=0')
        print('顺时针, 轮转顺序, 设置 下一家v3 出牌机会= 0, 叫牌机会=1, 说话=1')
        print('顺时针, 轮转顺序, 设置 下下一家v1 出牌机会= 0, 叫牌机会=0, 说话=1')
        pass
    elif ('3', '方片', 'blackCover') in v3:
        print('v3 出牌. 设置 v3 的 出牌机会= 1, 叫牌机会=1, 说话=0')
        print('顺时针, 轮转顺序, 设置 下一家v1 出牌机会= 0, 叫牌机会=1, 说话=1')
        print('顺时针, 轮转顺序, 设置 下下一家v2 出牌机会= 0, 叫牌机会=0, 说话=1')
    else:
        print('checkStart3 判断未生效')
        pass

    pass

vlist1 = [('2', '梅花', 'blackCover'), ('3', '方片', 'blackCover'), ('3', '黑桃', 'blackCover'), ('9', '梅花', 'blackCover')]
vlist2 = [('2', '梅花', 'blackCover'), ('4', '方片', 'blackCover'), ('3', '黑桃', 'blackCover'), ('9', '梅花', 'blackCover')]
vlist3 = [('2', '梅花', 'blackCover'), ('5', '方片', 'blackCover'), ('3', '黑桃', 'blackCover'), ('9', '梅花', 'blackCover')]
'''
1. 未完全出牌. 则 循环继续;
2. vplay1 出牌, 信不信或者过; 2.1 都信, 则 下家出牌; 不信,则 开启判断. 惩罚及设置 判断的 出牌人 与 说话人的 出牌情况 以及 说话情况.
3. 判断错误, 就不能出牌. 判断正确, 出牌人 拿回牌, 本局不能再出牌; 

'''
checkStart3(v1=vlist1, v2=vlist2, v3=vlist3)

vplayList = ['vplay1', 'vplay2', 'vplay3']

s = 3
splus = s + 1
print('s表示出牌人的index splus view', vplayList[splus%3])

def NoteWhoSpeak(sp=[], vplay=''):
    '''
    sp=[], 表示 谁说了什么; 输入牌或者 不要, 不信
    vplay='', 表示 谁在说
    :return: 记录是 第几轮, 
    谁说了话. vplay1 说话了sp, 记录下来, 然后根据 vplay 判断下一个 能出牌的人.  
     
    '''
    print('=====================Start=记录到了第几轮的方法')
    s = 1
    x = 0
    while s:
        x = x + 1
        print('到了第 %s 轮' % (x))
        if ss11['playCards'] == [] or ss12['playCards'] == [] or ss13['playCards'] == []:
            print(', 检测 剩余 还有谁有牌')
            s = 0
            if (ss11['playCards'] == [] and ss12['playCards'] == []) or ss13['playCards'] == []:
                print('结束本次斗地主')
            else:
                pass
        elif 1:
            print('扣减出牌人的牌()')
            ss13['playCards'].clear()
            pass
        else:
            print('在这里 else1 ')
            pass
    print('=====================end=记录到了第几轮的方法')
    pass


def end_of_round():

    pass