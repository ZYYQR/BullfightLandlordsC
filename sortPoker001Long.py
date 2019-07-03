# -*- coding: UTF-8
import operator
import random
import pysnooper
l = [('5', '黑桃', 'cover'), ('A', '红桃', 'cover'), ('2', '梅花', 'cover'), ('8', '方片', 'cover')]

lkey = [('5', '黑桃', 'cover'), ('A', '红桃', 'cover'), ('2', '梅花', 'cover'), ('8', '方片', 'cover'), ('4', '红桃', 'cover'),
        ('9', '梅花', 'cover'), ('9', '方片', 'cover'), ('3', '方片', 'cover')]

colorThePoker = {'e': '黑桃', 'r': '红桃', 't': '梅花', 'y': '方片'}
'''
还未配置好， 3， 以及 10 没拍好序
'''

sortlist = ["", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A", "2"]

# print(l[0][0])

@pysnooper.snoop('/home/qz/PycharmProjects/mycfile/StudingCoding/PyCharmZyyFiletempo001/BullfightLandlordsC/sortTedLog.logs')
def sortTed(keyList = [], sourceList = [], element = str()):
    '''
    :param key: 排序规则. 需要排序的 list 跟 规则list 比较， 相同的 就记一个someList， 不相同的就 排序相加, 最后， 按照 someList = sourceList， 再排序一次
    :param sourceList: 需要排序的 list
    :param element: sort element , 根据它来排序
    :return: return the sorted list
    '''
    # print("sortTed is method ")
    iolist = [] #''' list(sourceList[element]) '''
    pok1 = []
    pok11 = []
    for x in sourceList:
        iolist.append(x[0][0])
    # print('取 需要排列的 iolist 值list', iolist)
    x = len(iolist) - 1
    # print('this is x Initial value', x)
    '''  取出 需要 排序的， list中的index的 list; element 暂时先 没用到。 之后 替换成， 按照 这个index 来筛选。'''
    i = 0
    while x > len(pok1):
        for x11 in range(0, x):
            x1 = x11
            while len(iolist) !=0 and i < 100:
                #             while len(iolist) != 0 and i < 100:

                # print('====ios', x1, '\niolistwhile', iolist)
                #
                # print('===io', iolist[x1])

                if keyList.index(iolist[x1]):
                    # print('x1->', x1)
                    xc = keyList.index(iolist[x1])
                    # print('xc value', xc, iolist[x1], 'len iolist', len(iolist))
                    pok1.append(xc)
                    # print('要删除 这个print(iolist[xc])', iolist[x1])

                    del iolist[x1]
                    x2 = len(iolist) - 1
                    x = x2
                elif iolist is []:
                    continue
                else:
                    # print('see you later')
                    pass
                i = i + 1
    # print("pok1pok1pok1pok1pok1", pok1)
    pok12 = sorted(pok1)
    print('sort的index-pok12', pok12)
    i = 1
    while i>= 0:
        for k in pok12:
            pok11.append(keyList[k])
            # print( k)
        i = -1
    print('已经按照index 排序的 pok11', pok11)
    print('\n pok11', pok11)
    pass

'''
适配 sourceList 长度
以 element=l[0][0] 为提取，排序值
'''

sortTed(keyList=sortlist, sourceList=lkey, element=l[0][0])
