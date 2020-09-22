# read file
def _get_list_user_func(_path):
    _user_list = []
    file = open(_path, 'r')
    lines = file.read().splitlines()
    file.close()
    _len = len(lines)
    # print (_len)
    for _i in range(_len):
        _user_list.append(lines[_i])
    _user_list.append('root')
    # print (_user_list)
    return _user_list
# _get_list_user_func('EAI-Linux.log')