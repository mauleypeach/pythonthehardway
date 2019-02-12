from sys import argv
import os
import subprocess




os.system('clear')
# The os.system command is now defunt and subprocess is now used.
# Use this with any shell command.
subprocess.call('clear', shell=True)
print '\n' * 5
print "-" * 50
print '\n'

print "This is the name of the script, - ", argv[0]
print "This is the number of arguments, - ", len(argv)
print "The arguments are : ", str(argv), '\n'

# Attempting the labelling of the variables
script, filename, name = argv

print script, "Saved as variable script"
print filename, "Saved as variable filename"
print name, "Saved as variable name", '\n'

# I'm going to open a file for reading.
# doin this with a variable.


print "I have opened the file %r "  %filename, '\n'
print open(filename).read()

# variable version
print "Which file to read? ", '\n'
filename_again = raw_input('> ')
txt = open(filename_again)
print '\n',txt.read()

# note that the shell=True is needed.
subprocess.call('ls -l /tmp/mprak.txt', shell=True)


txt.close()

print "-" * 50
print '\n' * 5
