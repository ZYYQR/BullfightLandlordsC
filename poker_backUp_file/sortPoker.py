
# -*- coding: UTF-8
import operator
'''
poker 牌 排序备份;扑克牌排序备份
'''
l = [('5', '黑桃', 'cover'), ('A', '红桃', 'cover'), ('2', '梅花', 'cover'), ('8', '方片', 'cover')]
lkey = [('5', '黑桃', 'cover'), ('A', '红桃', 'cover'), ('2', '梅花', 'cover'), ('8', '方片', 'cover'), ('4', '红桃', 'cover'), ('6', '梅花', 'cover'), ('9', '方片', 'cover')]
sortlist = ["3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A", "2"]

def sortTed(keyList= [], sourceList = [], element = str()):
    print('use sortTed')
    '''
    :param key: 排序规则. 需要排序的 list 跟 规则list 比较， 相同的 就记一个someList， 不相同的就 排序相加, 最后， 按照 someList = sourceList， 再排序一次
    :param sourceList: 需要排序的 list
    :param element: sort element , 根据它来排序
    :return: return the sorted list
    '''

    iolist = [] #''' list(sourceList[element]) '''
    pok1 = []
    pok11 = []
    for x in sourceList:
        iolist.append(x[0][0])
    # print('取 需要排列的 list的 值list', iolist)

    i = 1
    x = len(iolist) - 1
    while i >= 0:
        x1 = x - 1
        if keyList.index(iolist[x1]):
            xc = keyList.index(iolist[x1])
            # print('1', xc, iolist[x1])
            pok1.append(xc)
        else:
            pass
        x = x - 1
        i = x
    pok12 = sorted(pok1)
    # print('sort的index-pok12', pok12)
    i = 1
    while i>= 0:
        for k in pok12:
            pok11.append(keyList[k])
            # print( k)
        i = -1
    # print('已经 按照index 排序的 pok11', pok11)
    x = 0
    i = 0
    p = []
    xx = len(pok11)
    while i >= 0 and x < 4 and pok11 != []:
        # print('----sign1---  ', xx, 'i value is ', i)
        for d in range(0, xx):
            if pok11 != None and x < 4:
                # print('x==========', x, ' | d  ', d)
                # print('x', x, ' |d ', d, 'pok11', pok11[d-1], '\n | sourceList ', sourceList)
                if pok11[d] == sourceList[x][0]:
                    p.insert(d, sourceList[x])
                    i = i + 1
                    # print("你大爷还是你大爷", pok11)
                    if pok11 == sourceList:
                        i = -1
                        x = -2
                        # print('00sign30 000')
                        continue
                else:
                    # print('sign4 到此一游')
                    i = i + 1
                    while i == 16:
                        # print(' i value ', i)
                        i = -1
                        break
                    pass
            else:
                break
        if pok11 != []:
            # print(" remove the ", pok11[d])
            # pok11 = pok11.pop(d - 1)
            # print('pok11', pok11)
            bidSortTedlist = pok11
            xx = len(pok11)
            # print('xx is ', xx)
        x = x + 1
    # print('\nis p value ', p)
    return bidSortTedlist
    pass
#
# sortTed(keyList=sortlist, sourceList=lkey, element=l[0][0])
