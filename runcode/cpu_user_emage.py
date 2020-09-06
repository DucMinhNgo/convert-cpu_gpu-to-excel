# read file
file = open('../emage/output_show_user_mem_usage.log', 'r')
lines = file.read().splitlines()
file.close()

# write to excel
import xlsxwriter
workbook = xlsxwriter.Workbook('../emage/cpu_each_user_emage.xlsx')
worksheet = workbook.add_worksheet()
row = 0
col = 0
_len_lines = len(lines)
print (_len_lines)
# config 
_count = 0
count_mem = 0
count_used = 0
_list_user = ['andy', 'cindy', 'dustin', 'jay', 'klein1', 'mateo', 'root', 'scott', 'turing', 'wayne', 'thinh', 'duy', 'Neil', 'shinre', 'klein', 'Darius', 'dao']
_count_user = 0
_len_user = len(_list_user)
worksheet.write(0, 0, 'date_cpu')
while (_count_user < _len_user):
    worksheet.write(row, _count_user + 1, _list_user[_count_user])
    _count_user += 1
row += 1

while (_count < _len_lines):
    # print (lines[_count])
    if lines[_count] == 'MEMORY':
        print (lines[_count - 1])
        # remove duplicated space
        lines[_count - 1] = " ".join(lines[_count - 1].split())
        _date = lines[_count - 1].split(' ')
        print (_date[1] + "_" + _date[2] + "_" + str(int(_date[3].split(":")[0])))
        print ("error: ")
        print (_date[1])
        print ('end')
        _check_true_time = int(_date[3].split(":")[0]) in [6, 12, 18, 0] and int(_date[3].split(":")[1]) == 0
        # print ('_check_true_time:')
        print (_check_true_time)
        # if int(_date[3].split(":")[0]) in [6, 12, 18, 0]:
        if _check_true_time == True:
            worksheet.write(row, 0, _date[1] + "_" + _date[2] + "_" + str(int(_date[3].split(":")[0])))
        count_mem = _count
        _count += 2
        # print (lines[_count])
        print ('---')
        _complete_data = []
        while lines[_count] != 'USED':
            _element = lines[_count].split(' ')
            if _element[1] in _list_user:
                _index = _list_user.index(_element[1])
                _complete_data.append(_index)
                # col
                print ('index', str(_index))
                if _check_true_time == True:
                    worksheet.write(row, _index + 1, float(_element[0]))
            _count += 1
        _complete_count = 0
        while (_complete_count < _len_user):
            if (_complete_count not in _complete_data):
                if _check_true_time == True:
                    worksheet.write(row, _complete_count + 1, 0)
            _complete_count += 1
        print ('---')
        if _check_true_time == True:
            row += 1
        count_used = _count
        # print (lines[_count])
        print ('distance: ')
        print (count_used - count_mem)
    _count += 1
print ('array result: ')
print (_list_user)
workbook.close()