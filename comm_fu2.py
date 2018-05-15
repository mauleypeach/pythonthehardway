#!/usr/bin/python
# Import the snizzle
import os

# setting result to equal the path.
result = os.getcwd()

# I print the variable result, then print the command.
print result
print os.getcwd()

# Some random file stat's of the file. No idea why.
#http://www.pythonforbeginners.com/os/python-system-administration
print ""
print "Getting the status of: ", os.stat('comm_fu2.py')
print ""

# os.system let's me use my normal os commmands.
result = os.system('ls -l /tmp')
# result becomes the output ls -l and we print it
print result
print ""
print ""
# Great a PID, useful!
print os.getpid()
print ""
print ""

# We'll modify a file.
print os.system('ls -l /tmp/mp*')
print ""
print ""
os.chmod('/tmp/mprak.txt',0777)
os.system('ls -l /tmp/mprak.txt')

# problems with this one, needed to sudo this command.
os.chown("/tmp/mprak.txt", 1001, 1001)
print "Changed ownership successfully!!"
print ""
print ""

# load average on the box
print os.getloadavg()
print ""
print ""

# check if file exists.
if os.path.exists("/tmp/mprak.txt"):
    print "File Exists"
else:
    print "File is Missing"

print ""
print ""

# Check for a directory if missing create it.
# if the directory exists but checking causes the mkdir then it exits with fault.
os.system("ls -l /tmp")
print ""
print ""
os.path.exists("/tmp/test_dir") or os.mkdir("/tmp/test_dir")
# os.path.exists("/tmp/test_dirs") or os.mkdir("/tmp/test_dir")
print ""
print ""
os.system("ls -l /tmp")
print ""
print ""

# File or directory
path = "/tmp"
if os.path.isdir(path): print "That's a directory"
if os.path.isfile(path): print "That's a file"

#print os.mkdir('/tmp/new_directory', 0666)
print ""
print ""


print os.environ['HOME']
print os.chdir("/tmp")
print ""
print ""

print os.system("ls -l")

print ""
print ""
for filename in os.listdir("/tmp"):
    print "This is inside /tmp", filename
    print ""
