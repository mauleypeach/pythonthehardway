#!/bin/python
#

from sys import argv
import os
import socket

script, weaselfile, = argv


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

target.write(line1 + "\n" + line2 + "\n" + line3 + "\n")

print "And finally, we close it."
target.close()

