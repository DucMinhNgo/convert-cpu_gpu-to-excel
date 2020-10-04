# read file
file = open('../viralint/output_cpu.log', 'r')
lines = file.read().splitlines()
file.close()

# write to excel
import xlsxwriter
workbook = xlsxwriter.Workbook('../viralint/cpu_viralint.xlsx')
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
# add new 
from  Userlist.array_month import _arr_mouth
while (_count < _len_lines):
    print ('---')
    date_line = lines[_count]
    print (date_line)
    date_line = " ".join(date_line.split())
    print (date_line)
    print (_count)
    print (date_line.split(' '))
    # print (date_line.split(' '))
    if date_line.split(' ')[1] in _arr_mouth:
        # print ('date_line')
        # print (_count)
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
        print (_count)
        _count += 10
        print (_count)
    else:
        _count += 16
workbook.close()