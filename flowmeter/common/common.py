# coding=utf-8


def extract_data_in_dict(data, keys):
    """
    从data字典提取keys列表中存在的键和相对应的值
    :param data: 字典
    :param keys: 需要提取的键列表
    :return:
    """
    res = {}
    for key in keys:
        val = data.get(key)
        # 只提取data中存在的值
        if val:
            res[key] = val
    return res


def get_allowed_action_of_role(role):
    """
    获取该角色所有能够执行的action
    :param role:
    :return:
    """
    authorities = role.authorities.all()

    action_list = []
    for auth in authorities:
        actions = auth.permission_action.split(';')
        action_list.extend(actions)
    return action_list


def get_page_data(datas, page, limit):
    """
    用于分页查询，获取某页的数据
    :param datas: 待分页的数据
    :param page: 当前页数
    :param limit: 每页最多显示的数据条数
    :return:
    """

    start_index = limit * (page - 1)
    end_index = limit * page

    return datas[start_index: end_index]
