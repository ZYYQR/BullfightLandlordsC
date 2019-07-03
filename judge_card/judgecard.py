def judgeCardCategory():
    '''
    牌种类:
    1 单
    2 双
    3 三个
    31 三带1
    32 三带1对
    4 炸弹 或者 3带1
    5 顺子
     牌: [3,3,3,1,4,4,4,2]
    :return:  31,2,3 三带1, 2连, 3为 最小的主数据
    牌: [1,2,3,4,5,6]
    :return 5,6,1 顺子,6连,1为最小的主数据
    '''

    pass
    return


def SurePutCard(old_card_list,new_card_list):
    '''

    :param old_card_list: 对方出牌
    :param new_card_list: 我方出牌
    :return: 1: 可以出大上, 0 不可以出 牌型不符合,或者太小
    '''
    card_category, card_connect_count,main_min_card = judgeCardCategory(old_card_list)
    card_category_new, card_connect_count_new,main_min_card_new = judgeCardCategory(old_card_list)
    if card_connect_count_new != 4 or (card_connect_count_new==4 and card_category==4):
        if card_category_new == card_category and card_connect_count == card_connect_count_new and main_min_card < main_min_card_new:
            print("压死")
            return 1
        elif card_category_new == card_category and card_connect_count == card_connect_count_new and main_min_card >= main_min_card_new:
            print("牌太小,出牌失败")
            return 0
        elif card_category_new != card_category or card_connect_count != card_connect_count_new :
            print("牌型不符,出牌失败")
            return 0
    elif card_connect_count_new == 4 and card_category !=4:
        print("压死")
        return 1


