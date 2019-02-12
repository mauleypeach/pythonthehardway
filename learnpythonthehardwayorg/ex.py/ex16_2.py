#!/bin/python
from sys import argv
script, weaselfile = argv

print "We're going to erase %r." % weaselfile
print "\n If you don't want that press ctrl-c"
print "\n\n If you do want that, hit enter"

raw_input("?")

print "Opening the file. GoodBye."
target = open(weaselfile, 'w')

print "Truncating the files. Goodbye!"
target.truncate()

print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print("I'm going to writes these to the file.")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print "And finally, we close it."
target.close()
