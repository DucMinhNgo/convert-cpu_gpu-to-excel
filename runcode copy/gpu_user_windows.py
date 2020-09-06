file = open('../windows/output_show_gpu_usage.log', 'r')
lines = file.read().splitlines()
file.close()
# write to excel
import xlsxwriter
workbook = xlsxwriter.Workbook('../windows/gpu_user_windows.xlsx')
worksheet = workbook.add_worksheet()
_arr_title = ['date_hour_of_Aug', 0, 1, 2, 3, 4, 5, 6, 7]
row = 0
col = 0
for element_title in _arr_title:
    worksheet.write(row, col, element_title)
    col += 1
row += 1
_count = 0
_len_lines = len(lines)
_arr_hour = [0, 6, 12, 18]
while (_count < _len_lines):
    print ("---")
    print ("line: ", str(_count))
    # print (lines[_count])
    _count += 1
    _date = lines[_count].split(' ')[1]
    # print (_date)
    print (_date.split('/')[1])
    _count += 3
    _time = int(lines[_count].split(':')[0])
    print (_time)
    # _minute = lines[_count].split(':')[1]
    # _real_minite = int(_minute.split(' ')[0])
    worksheet.write(row, 0, _date.split('/')[1] + '_' + str(_time))
    # print (lines[_count])
    _count += 5
    # print (lines[_count])
    _len_of_gpu = 8
    _sub_count = 0
    col = 0
    print ('---')
    while (col < _len_of_gpu):
        # print (lines[_count + _sub_count].split('|')[3].strip())
        _result = lines[_count + _sub_count].split('|')[3].strip()
        _get_percent = int(lines[_count + _sub_count].split('|')[1].strip().split(',')[1].strip().split(' ')[0])
        print (_get_percent)
        _result = _result.split(' ')
        # print('---')
        _name_arr = []
        _data_arr = []
        _sum = 0
        # _get_percent = _result = lines[_count + _sub_count].split('|')[1].strip()
        # print (_get_percent)
        for _element_name in _result:
            if _element_name == "NT" or _element_name == "Window":
                pass
            else:
                # print ('---')
                # print (_element_name)
                # print (_element_name.split('\\')[1])
                split_name = _element_name.split('\\')[1]
                split_name = split_name.split('(')[0]
                split_name = split_name.split('/')
                _sum += int(split_name[1])
                if split_name[0] not in _name_arr:
                    # split_name.split('(')[0]
                    _name_arr.append(split_name[0])
                    _data_arr.append(int(split_name[1]))
                else:
                    _index_element = _name_arr.index(split_name[0])
                    _data_arr[_index_element] += int(split_name[1])
            # print (int(split_name.split('/')[1]))
        # print (_name_arr)
        print (_data_arr)
        print (_sum)
        _len_data_arr = len(_data_arr)
        _count_data = 0
        while (_count_data < _len_data_arr):
            # print (str(round(((_data_arr[_count_data]/_sum *100)*_get_percent)/100, 2)) + "%")
            _name_arr[_count_data] += "(" + str(round(((_data_arr[_count_data]/_sum *100)*_get_percent)/100, 2)) + "%)"
            _count_data += 1
        print (_name_arr)
        _str_name_arr = ""
        for _element in _name_arr:
            _str_name_arr += _element + " "
        worksheet.write(row, col + 1, _str_name_arr.strip())
        col += 1
        _sub_count += 1*2
    row += 1
    print ('count: ', str(_count))
    _count += 17
    row += 1
workbook.close()