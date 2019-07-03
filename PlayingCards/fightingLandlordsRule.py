# -*- coding: UTF-8
import pysnooper
from StudingCoding.PyCharmZyyFiletempo001.BullfightLandlords.file1.pokerSortBase import baseSortThePoker as S

class TheRules():
    '''
    Python3.7.3
    1. 叫牌 规则: 1.1小于三张牌的规则(一张, 两张, 王炸判断) And 大于3张牌的规则(姐妹拱北, 飞一飞, 四张炸弹, 顺子)
    
    2. 大牌判断, 两个 叫牌人的牌的大小 判断;
    
    Noun_definition = {
    'single_card':"单牌",
    'a_pair':"对子",
    'fly_cards':"飞一飞",
    'sister_cards':"姐妹拱背",
    'the_Bomb':"炸弹",
    'shunzi':"顺子",
    'wang Fry':"王炸"
    }
    '''

    def __init__(self):
        self.__doc__ = ''
        self.count_list()
        self.sisterJudgment()
        self.checkSimplyOneSort()
        self.outPutRules_innerThree()
        self.checkThelist()

    def checkSimplyOneSort(sls= str(), source_list=[]):
        print("去重checkSimplyOneSort ", set(source_list))
        setlist = set(source_list)
        settolist = list(setlist)
        sortList = sorted(settolist)
        print('sortList_checkSimplyOneSort', sortList)
        return sortList

    def checkThelist(sls=str(), list_value=[]):
        print("checkThelist 是炸弹就弄它, 不是炸弹就 原样出入")
        ls = []
        if (len(list_value) == 4 and len(set(list_value)) == 1) or list_value == ['Kid', 'Big ghost']:
            ls = list_value
            print('The boom', list_value, '炸弹 , 还需要判断 更近 炸弹的大小 用 orderTheNum 查看是啥炸弹')

            pass
        else:
            ls = list_value
            print("原样出入")
            pass
        return ls

    def count_list(sls=str(), slist=[]):
        '''
        :param slist: 输入list, 输出 长度, 输出 相同元素个数.  
        :return: 
        '''
        print("count_list ")
        hNum = []
        hdict = {}
        slistLen = len(slist)
        for x in slist:
            xnum = slist.count(x)
            # print(x, xnum)
            hdict['%s' % (x)] = xnum
            hNum.append(xnum)
        # print('hNum 相同元素最多的那个元素的个数', hNum, '\n', 'hdict', hdict, '\n', 'slistLen', slistLen, '\n', 'source slist', slist)
        return hNum, hdict, slistLen, slist

    def sisterJudgment(self, k1=1, k2=2, source_list=[]):
        print("调用 第2个方法 sisterJudgment")
        '''
        method_function_2 , 判断 能否叫牌;
        本方法, 判断 长度 大于 4的 叫牌数量
        判断, 是否是姊妹拱背
        len 大于5[6, 8, 10, 12, 14, 16] 且不是 拱北
        k1(slistLen) 表示 list长度, 
        k2(len(hdict)) 表示 统计元素个数list长度
        '''
        print("源list==", source_list, '\nsource_list[0]', source_list[0])
        ospokerlist =S.checkSimplyOneSort(source_list)
        ospokerlistlen = len(ospokerlist)
        shunzi01 = ['3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        indexNum = shunzi01.index('%s' % (source_list[0]))
        print('indexNum sisterJudgment', indexNum)
        Hlen = [6, 8, 10, 12, 14, 16]
        hNum, hdict, slistLen, slist1 =self.count_list(slist=source_list)
        bidList = []
        print('shunzi01[indexNum:indexNum+k1]', shunzi01[indexNum:indexNum + k1], '\nsource_list', source_list)
        if k2 == k1 / 2 and k1 in Hlen and shunzi01[indexNum:indexNum + ospokerlistlen]:
            print(' 是 姊妹, 可以叫牌/叫牌')
            bidList = source_list + ['sister_cards']

        elif max(hNum) == 3 and len(hdict) == 2:
            print('这个是 飞一飞, 可以叫牌/叫牌')
            bidList = source_list + ['fly_cards']

        elif shunzi01[indexNum:indexNum + k1] == source_list:
            print('是 顺子, 可以叫牌/叫牌')
            bidList = source_list + ['shunzi']
            ''' 排除 飞一飞'''

        elif len(source_list) == 4 and len(set(source_list)) == 1:
            print("sisterJudgment 这个是炸弹")
            bidList = source_list + ['the_Bomb']

        else:
            print('不neng')
            bidList = 'False'

        return bidList
        pass

    def outPutRules_innerThree(self, source_list=[]):
        '''
        :param source_list: 输入 源list, 判断 是什么牌, 并且, 获取属性 
        :return: 
        '''
        print("调用 第一个方法 outPutRules_innerThree, source_list", source_list)
        sliLen = len(source_list)
        theQueenBombName1 = ['Kid', 'Big ghost']
        theQueenBombName2 = ['Xiao Wang', 'king']
        theQueenBombName3 = ['Kid', 'king']
        theQueenBombSet = theQueenBombName3 + theQueenBombName2 + theQueenBombName1
        bidList = []
        if sliLen > 3:
            # print("调用方法二, 然后 继续执行")
            hNum, hdict, slistLen, slist1 = self.count_list(slist=source_list)
            print('hNum, hdict, slistLen, slist1', hNum, hdict, slistLen, slist1)
            bidList =self.sisterJudgment(k1=slistLen, k2=len(hdict), source_list=slist1)
            print('bidList sisterJudgment bidList', bidList)
            pass
        elif sliLen == 2 and (source_list[0] in theQueenBombSet) and (source_list[1] in theQueenBombSet):
            print(" 这是王炸")
            bidList = source_list + ['wang Fry']
            pass
        elif sliLen == 3:
            print("三张牌 不符合叫牌规则, 请重选")
        elif sliLen == 2 and len(set(source_list)) == 1:
            print(" 这个是 对子")
            bidList = source_list + ['a_pair']
        elif sliLen == 2 and len(set(source_list)) == 2:
            print(" 这个是 飞一飞")
            bidList = source_list + ['fly_cards']
        elif sliLen == 1:
            print(" 这个是 , 单牌")
            bidList = source_list + ['single_card']

        else:
            print("无法叫牌, 出错了")
            bidList = 'False'

        return bidList
        pass

print("================================")
listx0 = ['A']
listxx0 = ['A', '3']
listxx002 = ['A', 'A']
listxx10 = ['3', '3']
listxxx0 = ['3', '3', '3']
listxxx04 = ['3', '3', '3', '3']
listxxx02 = ['3', '3', '3', '4']
listxxx021 = ['3', '3', '3', '4', '4']
listxxxx0 = ['3', '3', '4', '4', '5', '5']
listxxxx01 = ['3', '3', '4', '4', '5', '5', '7', '7', '8', '8']
list1 = ['3', '4', '5', '6', '7', '8', '9', '8']
list112 = ['3', '4', '5', '6', '7', '8', '9', '10', 'shunzi']
list1121 = ['4', '5', '6', '7', '8', '9', '10', 'J']
theQueenBombName1 = ['Kid', 'Big ghost']


# ruls = outPutRules_innerThree(source_list=listxxx04)
# print('上家叫牌', ruls, ruls[-1])


# num = orderTheNum(value_is=listx0[0])
'''
备用代码
# print('转化h 为 str', h)
# print(set(listxxx0))
#
# print(h.count('6'))

# print(max(hNum))
shunzi01 = ['3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
shunzi01Q = ['10', 'J', 'Q', 'K', 'A']
# print(shunzi01 + shunzi01Q)

opath = shunzi01.index('6')
# print('x.index', shunzi01.index('6'))
# print(shunzi01[opath:opath+7])
'''

list112 = {'playCards':['3', '4', '5', '6', '7', '8', '9', '10'], 'SType':'shunzi'}

inlist = {'v':1, 'playCards':['3', '4', '5', '6', '7', '8', '9', '10']}
print('inlist', inlist)
inplaycards = input(' 到v1出牌:')
print('inplaycards ', inplaycards)
list112 = {'v':1,'playCards':['3', '4', '5', '6', '7', '8', '9', '10'], 'SType':'shunzi', 'Snum': 8}