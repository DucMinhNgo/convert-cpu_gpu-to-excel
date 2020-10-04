# read file
file = open('../emagevision/output_cpu.log', 'r')
lines = file.read().splitlines()
file.close()

# write to excel
import xlsxwriter
workbook = xlsxwriter.Workbook('../emagevision/cpu_emagevision.xlsx')
worksheet = workbook.add_worksheet()
row = 0
col = 0
_arr_title = ['date_hour', 'cpu_used']
for element_title in _arr_title:
    worksheet.write(row, col, element_title)
    col += 1
row += 1
# 
_count = 0
_len_lines = len(lines)

_arr_hour = [0, 6, 12, 18]
from  Userlist.array_month import _arr_mouth
# _arr_mouth = ['Aug', 'Sep', 'Oct']
while (_count < _len_lines):
    date_line = lines[_count]
    date_line = " ".join(date_line.split())
    if date_line.split(' ')[1] in _arr_mouth:
        print (date_line)
        if date_line.split(' ')[2] == '':
            _date = date_line.split(' ')[3]
            hour_line = date_line.split(' ')[4]
        else:
            _date = date_line.split(' ')[2]
            hour_line = date_line.split(' ')[3]
        
        # print (hour_line.split(':')[0])
        # print (hour_line)
        col = 0
        if (int(hour_line.split(':')[0]) in _arr_hour and int(hour_line.split(':')[1]) == 0):
            _data = _date + "_" + hour_line.split(':')[0]
            # print (_data)
            worksheet.write(row, col, _data)
            col += 1
        _count += 4
        if (int(hour_line.split(':')[0]) in _arr_hour and int(hour_line.split(':')[1]) == 0):
            if lines[_count].split(' ')[11] == '':
                _data_used = lines[_count].split(' ')[12]
            else:
                _data_used = lines[_count].split(' ')[11]
            # print (_data_used)
            worksheet.write(row, col, float(_data_used))
            col += 1
            row += 1
        _count += 12
    else:
        _count += 16
workbook.close()