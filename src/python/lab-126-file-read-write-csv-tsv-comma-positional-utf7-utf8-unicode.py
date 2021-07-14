#
# filename    : lab-126-file-read-write-csv-tsv-comma-positional-utf7-utf8-unicode.py
# Description : File Open
# Docs        :  * https://docs.python.org/3/library/functions.html#open
# Requirements:
#
import json

print('\n#1. File read csv(;)  utf7 - Write tmp without header\n')

file_write = open('file-01-csv-utf7.csv.tmp', 'w+')
with open('file-01-csv-utf7.csv', 'r') as file_read:
    line = file_read.readline()  # skip header from readlines() loop
    for line in file_read.readlines():
        print(line, end='')
        file_write.write(line)
    file_read.close()
file_write.close()


print('\n#2. File read csv(,)  utf7\n')

file_write = open('file-02-csv-comma-utf7.csv.tmp', 'w+')
with open('file-02-csv-comma-utf7.csv', 'r') as file_read:
    line = file_read.readline()  # skip header from readlines() loop
    for line in file_read.readlines():
        a_split_line = line.replace("\n", "").split(',')
        uf = ''
        try:
            uf = a_split_line[0]              # index out of bounds was not checked!
        except:  # not the best way
            pass
        nome_do_estado = ''
        try:
            nome_do_estado = a_split_line[1]  # index out of bounds was not checked!
        except:  # not the best way
            pass
        obs = ''
        try:
            obs = a_split_line[2]           # index out of bounds was not checked!
        except:  # not the best way
            pass
        print(f'uf: "{uf}", nome_do_estado: "{nome_do_estado}", obs: "{obs}"')
        file_write.write(line)
    file_read.close()
file_write.close()


print('\n#3. File read tsv(tab)  utf7\n')

file_write = open('file-03-tsv-utf7.csv.tmp', 'w+')
with open('file-03-tsv-utf7.csv', 'r') as file_read:
    line = file_read.readline()  # skip header from readlines() loop
    for line in file_read.readlines():
        a_split_line = line.replace("\n", "").split('\t')
        # default
        uf = ''
        nome_do_estado = ''
        obs = ''
        # split line and extract values
        if len(a_split_line) >= 1:
            uf = a_split_line[0]
        if len(a_split_line) >= 2:
            nome_do_estado = a_split_line[1]
        if len(a_split_line) >= 3:
            obs = a_split_line[2]
        # print conseole
        print(f'uf: "{uf}", nome_do_estado: "{nome_do_estado}", obs: "{obs}"')
        # write
        file_write.write(line)
    file_read.close()
file_write.close()

print('\n#4. File read pos utf7\n')

file_write = open('file-04-pos-utf7.txt.tmp', 'w+')
with open('file-04-pos-utf7.txt', 'r') as file_read:
    line = file_read.readline()  # skip header from readlines() loop
    for line in file_read.readlines():
        # default
        uf = ''
        nome_do_estado = ''
        obs = ''
        # split line and extract values
        if len(line) >= 2:
            uf = line[0:2]
        if len(line) >= 21:
            nome_do_estado = line[2:21]
        if len(line) >= 31:
            obs = line[21:31]
        # print conseole
        print(f'uf: "{uf}", nome_do_estado: "{nome_do_estado}", obs: "{obs}"')
        # write
        file_write.write(line)
    file_read.close()
file_write.close()

print('\n#5. File read csv utf8 to encoding iso 8859-1\n')

file_write = open('file-05-csv-utf8.csv.tmp', 'w+', encoding="utf8")
file_write_encode_latin = open('file-05-csv-utf8-to-encoding-iso-8859-1.csv.tmp', 'w+', encoding="utf8")
with open('file-05-csv-utf8.csv', 'r', encoding="utf8") as file_read:
    line = file_read.readline()  # skip header from readlines() loop
    for line in file_read.readlines():
        a_split_line = line.replace("\n", "").split(';')
        # default
        uf = ''
        nome_do_estado = ''
        obs = ''
        # split line and extract values
        if len(a_split_line) >= 1:
            uf = a_split_line[0]
        if len(a_split_line) >= 2:
            nome_do_estado = a_split_line[1]
        if len(a_split_line) >= 3:
            obs  = a_split_line[2]
        # print conseole
        print(f'uf: "{uf}", nome_do_estado: "{nome_do_estado}", obs: "{obs}"')
        # write
        file_write.write(line)
        file_write_encode_latin.write(line)
    file_read.close()
file_write.close()


print('\n#5. File read csv utf8 to json\n')

dict_file={}
file_write = open('file-05-csv-utf8-to-json.csv.tmp', 'w+', encoding="utf8")
with open('file-05-csv-utf8.csv', 'r', encoding="utf8") as file_read:
    line = file_read.readline()  # skip header from readlines() loop
    record_num = 0
    for line in file_read.readlines():
        a_split_line = line.replace("\n", "").split(';')
        record_num += 1
        uf = ''
        nome_do_estado = ''
        obs = ''
        # split line and extract values
        if len(a_split_line) >= 1:
            uf = a_split_line[0]
        if len(a_split_line) >= 2:
            nome_do_estado = a_split_line[1]
        if len(a_split_line) >= 3:
            obs  = a_split_line[2]
        # print conseole
        print(f'uf: "{uf}", nome_do_estado: "{nome_do_estado}", obs: "{obs}"')
        # write buffer to json
        dict_record = {'uf': uf, 'nome_do_estado': nome_do_estado, 'obs': obs}
        dict_file['row#' + str(record_num)] = dict_record
    file_read.close()

json_dict_file = json.dumps(dict_file)
file_write.write(json_dict_file)
file_write.close()

