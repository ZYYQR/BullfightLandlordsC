import uuid


def judgeCardCategory():
    '''
    ������:
    1 ��
    2 ˫
    3 ����
    31 ����1
    32 ����1��
    4 ը�� ���� 3��1
    5 ˳��
     ��: [3,3,3,1,4,4,4,2]
    :return:  31,2,3 ����1, 2��, 3Ϊ ��С��������
    ��: [1,2,3,4,5,6]
    :return 5,6,1 ˳��,6��,1Ϊ��С��������
    '''

    pass
    return


def SurePutCard(old_card_list,new_card_list):
    '''

    :param old_card_list: �Է�����
    :param new_card_list: �ҷ�����
    :return: 1: ���Գ�����, 0 �����Գ� ���Ͳ�����,����̫С
    '''
    card_dict = {
        "J":"11","Q":"12","K":"13","A":"14","2":"15","XW":"16","DW":"17"
    }
    card_category, card_connect_count,main_min_card = judgeCardCategory(old_card_list)
    card_category_new, card_connect_count_new,main_min_card_new = judgeCardCategory(old_card_list)
    if main_min_card_new in card_dict.keys():
        main_min_card_new = card_dict[main_min_card_new]
    if main_min_card in card_dict.keys():
        main_min_card = card_dict[main_min_card]
    if card_connect_count_new != 4 or (card_connect_count_new==4 and card_category==4):
        if card_category_new == card_category and card_connect_count == card_connect_count_new and int(main_min_card) < int(main_min_card_new):
            print("ѹ��")
            return 1
        elif card_category_new == card_category and card_connect_count == card_connect_count_new and int(main_min_card) >= int(main_min_card_new):
            print("��̫С,����ʧ��")
            return 0
        elif card_category_new != card_category or card_connect_count != card_connect_count_new :
            print("���Ͳ���,����ʧ��")
            return 0
    elif card_connect_count_new == 4 and card_category !=4:
        print("ѹ��")
        return 1

def playUuid():
    return uuid.uuid4()
