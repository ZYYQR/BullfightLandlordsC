# -*- coding: UTF-8
import pysnooper
from StudingCoding.PyCharmZyyFiletempo001.BullfightLandlords.file1.pokerSortBase import baseSortThePoker
from StudingCoding.PyCharmZyyFiletempo001.BullfightLandlords.PlayingCards.fightingLandlordsRule import TheRules


def bigMethod(oldList=[], newList=[]):
    '''
    :param oldList: 去除 oldList的 类型 与 数量 
    :param newList: 判断 newL的 类型与 数量; 
    :return: 提前判断, 是否是炸弹呢. 
    '''

    s = TheRules.checkThelist(list_value=newList)
    print('s S.checkThelist 排查了, 炸弹的结果')
    newList = s
    print("bigMethod ")
    oldListLen = len(oldList)
    oldListAttu = oldList[-1]
    newList_Len = len(newList)
    newList_Attu = newList[-1]

    if oldListLen == newList_Len and oldListAttu == newList_Attu:
        print("同长度,同属性,排序比较大小.不能 飞一飞,用elif来飞一飞. ")
        oldList0_index = baseSortThePoker.orderTheNum_index(value_is=str(oldList[0]))
        newList0_index = baseSortThePoker.orderTheNum_index(value_is=str(newList[0]))
        # print('newList0_index', newList0_index)
        if oldList0_index < newList0_index and oldListAttu != 'fly_cards':
            print('newList0_index 大于 上家')
        elif oldList0_index > newList0_index and oldListAttu != 'fly_cards':
            print("叫牌比上家小, 不能出牌")

        elif oldListAttu == 'fly_cards' and oldListLen == newList_Len:
            print("飞一飞比较大小, 姐妹飞一飞 3的元素不唯一.需要处理")

            pass

    elif oldListLen != newList_Len and oldListAttu == newList_Attu:
        print("同类型, 不同数量.不能出牌")

    else:
        print("啥也不是, 不能 出牌")
        return 'False'

    pass


print("================================")
listx0 = ['A', 'single_card']
listx01 = ['K', 'single_card']
listxx0 = ['A', '3']
listxx102 = ['A', 'A', 'a_pair']
listxx10 = ['3', '3', 'a_pair']
listxxx0 = ['3', '3', '3']
listxxx04 = ['3', '3', '3', '3']

listxxx02 = ['3', '3', '3', '4', 'fly_cards']
listxxx0212 = ['4', '4', '4', '3', 'fly_cards']
listxxx021 = ['3', '3', '3', '4', '4', 'fly_cards']

listxxxx0 = ['3', '3', '4', '4', '5', '5', 'sister_cards']
listxxxx01 = ['3', '3', '4', '4', '5', '5', '7', '7', '8', '8', 'sister_cards']
list1 = ['3', '4', '5', '6', '7', '8', '9', '8']
list112 = ['3', '4', '5', '6', '7', '8', '9', '10', 'shunzi']
list1121 = ['4', '5', '6', '7', '8', '9', '10', 'J', 'shunzi']
theQueenBombName1 = ['Kid', 'Big ghost']


ruls = bigMethod(oldList=listxxx02, newList=listxxx0212)
print('ben叫牌', ruls)
