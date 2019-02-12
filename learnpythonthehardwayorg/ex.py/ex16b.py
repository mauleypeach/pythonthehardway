from sys import argv

script, filename = argv

print "We're going to open the file for reading."
print "Continue??"

raw_input("?")

print "Opening the file for reading."
targetfile = open(filename,'r')

print "Reading the file."
print targetfile.read()

# closing the file and opening in write mode.
#targetfile.close()
#print "Closed the file."

print "Opening the file for writing."
targetfile = open(filename,'w+')

print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."
lines = ('%s \n%s\n%r\n') % (line1, line2, line3)
targetfile.write(lines)
targetfile.close()
targetfile = open(filename, 'r')
print "Reading the file."
print targetfile.read()

print "And finally, we close it."
targetfile.close()
