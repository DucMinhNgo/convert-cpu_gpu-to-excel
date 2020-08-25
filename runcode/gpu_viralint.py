file = open('../viralint/output_gpu.log', 'r')
lines = file.read().splitlines()
file.close()
# write to excel
import xlsxwriter
workbook = xlsxwriter.Workbook('../viralint/gpu_viralint.xlsx')
worksheet = workbook.add_worksheet()
row = 0
col = 0
_arr_title = ['date_hour_of_Aug', 0, 1, 2, 3, 4, 5, 6, 7]
for element_title in _arr_title:
    worksheet.write(row, col, element_title)
    col += 1
row += 1   
# 
_count = 0
print (len(lines))
_len_lines = len(lines)
_arr_hour = [0, 6, 12, 18]
while (_count < _len_lines):
    # if _count == 0:
    # print (lines[_count])
    date_line = lines[_count]
    # print (date_line)
    if date_line.split(' ')[1] == 'Aug':
        # print (lines[_count])
        # print (date_line.split(' ')[1])
        # print ('---')
        # print (int(hour_line.split(':')[0]))
        # print (date_line.split(' ')[2])
        # print day
        if date_line.split(' ')[2] == '':
            # print (date_line.split(' ')[3])
            _date = date_line.split(' ')[3]
            hour_line = date_line.split(' ')[4]
        else:
            _date = date_line.split(' ')[2]
            hour_line = date_line.split(' ')[3]
        # print (hour_line)
        # hour
        # print (hour_line.split(':')[0])
        # minutes
        # print (hour_line.split(':'))[1]
        col = 0
        if (int(hour_line.split(':')[0]) in _arr_hour and int(hour_line.split(':')[1]) == 0):
            worksheet.write(row, col, _date + "_" + hour_line.split(':')[0])
            # print ('---')
            # print (_date)
            col += 1
            # print (hour_line.split(':')[0])
        _count += 1
        # drop line
        _count += 1
        # print ('---')
        if (int(hour_line.split(':')[0]) in _arr_hour and int(hour_line.split(':')[1]) == 0):
            _len_of_gpu = 8
            _sub_count = 0
            print (_count)
            # use for viralint
            if (_count > 900 and _count < 1153):
                _len_of_gpu = 7
            print ('---')
            while (_sub_count < _len_of_gpu):
                # print (lines[_count + _sub_count].split(',')[0])
                get_percentage = lines[_count + _sub_count].split(',')[0]
                # print (int(get_percentage.split(' ')[0]))
                # print (_count)
                data_gpu = int(get_percentage.split(' ')[0])
                # print (data_gpu)
                worksheet.write(row, col, data_gpu)
                col += 1
                _sub_count += 1
            print ('---')
            row += 1
        # use for viralint
        if (_count > 900 and _count < 11153):
            _count += 7
        else:
            _count += 8
    else:
        _count += 1
        # drop line
        _count += 1
        _count += 8
workbook.close()
