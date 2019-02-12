# rewrite of ex20.py
#  hopefully shorter.
from sys import argv

script = argv

file ='/tmp/doggie_report.txt'

current_file = open(file,'r+')

current_line = 1
def print_all(f):
    print current_file.read()

print_all(current_file)

def rewind(file):
    file.seek(0)

def print_a_line(line_count, file):
    print line_count, file.readline()
    return line_count + 1


rewind(current_file)
print current_line
current_line = print_a_line(current_line, current_file)
print current_line

print_a_line(current_line, current_file)

