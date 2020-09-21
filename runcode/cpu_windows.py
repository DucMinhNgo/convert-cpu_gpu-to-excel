file = open('../windows/cpu.log', 'r')
lines = file.read().splitlines()
file.close()

# write to excel
import xlsxwriter
workbook = xlsxwriter.Workbook('../windows/cpu_windows.xlsx')
worksheet = workbook.add_worksheet()

row = 0
col = 0
_count = 0
_len_lines = len(lines)
_arr_hour = [0, 6, 12, 18]
while (_count < _len_lines):
    col = 0
    _count += 1
    # print (lines[_count])
    _date = lines[_count].split(' ')[1]
    # print (_date.split('/')[1])
    _count += 3
    _time = int(lines[_count].split(':')[0])
    _minute = lines[_count].split(':')[1]
    _real_minite = int(_minute.split(' ')[0])
    if (_time in _arr_hour and _real_minite == 21):
        print ('---')
        print (_time)
        print (_real_minite)
        # print (_date.split('/')[1] + '_' + str(_time))
        worksheet.write(row, 0, _date.split('/')[1] + '_' + str(_time))
    _count += 5
    if (_time in _arr_hour and _real_minite == 21):
        _date_time = lines[_count].split(',')
    # print ('---')
        print (float(_date_time[1][1:5]))
        worksheet.write(row, 1, float(_date_time[1][1:5]))
        row += 1
    _count += 6
workbook.close()