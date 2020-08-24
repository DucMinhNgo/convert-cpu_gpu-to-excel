file = open('./viralint/output_show_user_gpu_usage.log', 'r')
lines = file.read().splitlines()
file.close()

# write to excel
import xlsxwriter
workbook = xlsxwriter.Workbook('./viralint/viralint_gpu_usage.xlsx')
worksheet = workbook.add_worksheet()
row = 0
col = 0
_arr_title = ['date_hour_of_Aug', 0, 1, 2, 3, 4, 5, 6, 7]

for element_title in _arr_title:
    worksheet.write(row, col, element_title)
    col += 1
row += 1

_count = 0
print (len(lines))
_len_lines = len(lines)
_arr_hour = [0, 6, 12, 18]
while (_count < _len_lines):
    date_line = lines[_count]
    print (date_line)
    if date_line.split(' ')[1] == 'Aug':
        if date_line.split(' ')[2] == '':
            # print (date_line.split(' ')[3])
            _date = date_line.split(' ')[3]
            hour_line = date_line.split(' ')[4]
        else:
            _date = date_line.split(' ')[2]
            hour_line = date_line.split(' ')[3]
        print (_date)
        print (hour_line)
        col = 0
        # if (int(hour_line.split(':')[0]) in _arr_hour and int(hour_line.split(':')[1]) == 0):
        worksheet.write(row, col, _date + "_" + hour_line.split(':')[0])
        _count += 2
        _len_of_gpu = 7
        _sub_count = 0
        while (_sub_count < _len_of_gpu):
            get_name = lines[_count + _sub_count].split('|')[3].strip()
            print (get_name)
            worksheet.write(row, _sub_count + 1, get_name)
            _sub_count += 1
        row += 1
        _count += _len_of_gpu
    else:
        _count += 2
        _count += 7

workbook.close()