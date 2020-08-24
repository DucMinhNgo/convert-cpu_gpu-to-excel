file = open('gpu.log', 'r')
lines = file.read().splitlines()
file.close()
# write to excel
import xlsxwriter
workbook = xlsxwriter.Workbook('gpu_windows.xlsx')
worksheet = workbook.add_worksheet()

row = 0
col = 0
_arr_title = ['date_hour_of_Aug', 0, 1, 2, 3, 4, 5, 6, 7]

for element_title in _arr_title:
    worksheet.write(row, col, element_title)
    col += 1
row += 1
_count = 0
_len_lines = len(lines)
_arr_hour = [0, 6, 12, 18]
while (_count < _len_lines):
    # print (lines[_count])
    _count += 2
    # print (lines[_count])
    _date = lines[_count].split(' ')[1]
    print (_date.split('/')[1])
    _count += 3
    # print (lines[_count])
    _time = int(lines[_count].split(':')[0])
    _minute = lines[_count].split(':')[1]
    _real_minite = int(_minute.split(' ')[0])
    if (_time in _arr_hour and _real_minite == 14):
        print (_time)
        print (_real_minite)
        worksheet.write(row, 0, _date.split('/')[1] + '_' + str(_time))
    _count += 4
    _len_of_gpu = 8
    _sub_count = 0
    print ('---')
    col = 1
    while (_sub_count < _len_of_gpu):
        get_percentage = lines[_count + _sub_count].split(',')[0]
        data_gpu = int(get_percentage.split(' ')[0])
        print (data_gpu)
        if (_time in _arr_hour and _real_minite == 14):
            worksheet.write(row, col, data_gpu)
            col += 1
        _sub_count += 1
    # _count += 7
    print ('---')
    if (_time in _arr_hour and _real_minite == 14):
        row += 1
    _count += 1
    _count += 7
workbook.close()