# read file
file = open('output_show_user_mem_usage.log', 'r')
lines = file.read().splitlines()
file.close()

_len_lines = len(lines)
print (_len_lines)
# config 
_count = 0
count_mem = 0
count_used = 0
_list_user = []
while (_count < _len_lines):
    # print (lines[_count])
    if lines[_count] == 'MEMORY':
        # print (lines[_count])
        count_mem = _count
        _count += 2
        # print (lines[_count])
        print ('---')
        while lines[_count] != 'USED':
            _element = lines[_count].split(' ')
            print (_element[1])
            if _element[1] not in _list_user:
                _list_user.append(_element[1])
            _count += 1
        print ('---')
        count_used = _count
        # print (lines[_count])
        print ('distance: ')
        print (count_used - count_mem)
    _count += 1
print ('array result: ')
print (_list_user)