#!/usr/bin/python
from sys import argv
# we are setting the variables of script name and file to use as input_file.
script, input_file = argv
# Here we define a function with 1 argument f will be the filename. we assign f and read f.
def print_all(f):
    print f.read()
# we create function rewind. we set the file pointer to position 0. meaning it prints from the first char.
def rewind(f):
    f.seek(0)
# we created a function to read a whole line based on the line count. Added a comma at then to prevent newline from the file being printed.
def print_a_line(line_count, f):
    print line_count, f.readline(),
# we here set current_file to open the file for reading.
current_file = open(input_file)

print "First let's print the whole file: \n"
# using functions
print_all(current_file)

print "Now let's rewind, kind of like a tape."
# function rewind. passing in the input_file.
rewind(current_file)

print "Let's print three lines:"
# We set variable current line and increase it by 1 as lines are read.
current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)
