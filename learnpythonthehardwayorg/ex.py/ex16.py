# allows for variables to be added.
from sys import argv
import os
import subprocess

# ------------------------------------------------
# Screen setup
os.system('clear')
# The os.system command is now defunt and subprocess is now used.
# Use this with any shell command.
subprocess.call('clear', shell=True)
print '\n' * 5
print "-" * 50
print '\n'
# -----------------------------------------------

# info
print "The name of the script is ", argv[0]
print "There are %r variables." %len(argv)
print "The arguments are : ", argv
# ----------------------------------------------
# variables setup.

script, filename = argv
#-------------------------------------------------
# PROGRAM
# In this program we open a file for writing and append new text to it.
# Creating a text editor.
# .close() .read() .readline() .truncate() .write()
print "" * 2
print script
print filename

print "" * 2
print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL- C (^C)."
print "If you do want that, hit RETURN."
raw_input(">")

# open target file for writing.
target = open(filename, 'w')
print "Opening file %r " %filename

print "Truncating file, Goodbye!"
open(filename, 'w').truncate

print "Enter 3 lines for addition to the file."

line1 = raw_input("The 1st line to append \n> ")
print line1
line2 = raw_input("The 2nd line to append \n> ")
print line2
line3 = raw_input("The 3rd line to \
append \n> ")
print line3

print "I\'m going to write these lines!"

# writing the lines to a file. /tmp/mprak.txt
open(filename,'w+').write('test write\n')
#target.close()
print(line1,"\n", line2,"\n",line3,"\n")
#target.writelines("line1","\n", "line2","\n","line3","\n")
lines = [line1, '\n', line2,'\n', line3]
print lines
target.writelines(lines)
print("") * 2
target.close()
print open(filename).read()
target.close()

# end screen setup
print "" * 2
print "-" * 50
print '\n' * 5
