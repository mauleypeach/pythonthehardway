# accepts commandline arguments 
from sys import argv
# argument variables to be saved.
script, filename = argv
# assigns txt as a function to open file.
txt = open(filename)
#outputs file name.
print "Here's your file %r:" % filename
#
print txt.read()

print "Type the filename again:"
file_again = raw_input("> ")

txt_again = open(file_again)

print txt_again.read()
