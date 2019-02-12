# accepts commandline arguments
from sys import argv
# argument variables to be saved.
#script, filename = argv

print "Please type the filename."
filename = raw_input()

# assigns txt as a function to open file.
txt = open(filename)
#outputs file name.
print "Here's your file %r:" % filename
#
print txt.readline()
