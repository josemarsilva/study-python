#
# filename    : lab-124-file-open-write-read-seek-with-close.py
# Description : File Open
# Docs        :  * https://docs.python.org/3/library/functions.html#open
# Requirements:
#

print('\n#1. File manipulation - open \n')


print('\n#2. File manipulation - open and write some lines to file\n')

file = open('file-01.txt', 'w+')  # w+: read and write
file.write('row: 1\n')
file.write('row: 2\n')
file.write('row: 3\n')


print('\n#3. File manipulation - read file stream from top\n')

file.seek(0,0)      # point top of file first row and first char
print(file.read())  # row: 1
                    # row: 2
                    # row: 3


print('\n#4. File manipulation - readline(): read line-by-line from file since top\n')

file.seek(0,0)      # point top of file first row and first char
print(file.readline(), end='')  # row: 1
print(file.readline(), end='')  # row: 2
print(file.readline(), end='')  # row: 3


print('\n#5. File manipulation - readlines(): read all lines from file into a list\n')

file.seek(0,0)      # point top of file first row and first char
print(file.readlines()) # ['row: 1\n', 'row: 2\n', 'row: 3\n']


print('\n#6. File manipulation - readlines(): read all lines from file into a list\n')

print('')
file.seek(0,0)      # point top of file first row and first char
for line in file.readlines():
    print(line, end='')     # row: 1
                            # row: 2
                            # row: 3


file.close()


print('\n#7. File manipulation - with write lines (pythonic way of manipulation)\n')

with open('file-02.txt', 'w+') as file:
    file.write('row: 1\n')
    file.write('row: 2\n')
    file.write('row: 3\n')
    file.close()


print('\n#8. File manipulation - with read lines\n')

with open('file-02.txt', 'r') as file:
    print(file.read())
    file.close()    # row: 1
                    # row: 2
                    # row: 3


print('\n#9. File manipulation - append to end-of-file\n')

with open('file-02.txt', 'a+') as file:
    file.write('row: 4\n')
    file.close()
with open('file-02.txt', 'r') as file:
    print(file.read())
    file.close()    # row: 1
                    # row: 2
                    # row: 3
                    # row: 4

print('\n#10. File manipulation - os.remove(): removing file\n')

import os

os.remove('file-01.txt')
os.remove('file-02.txt')
