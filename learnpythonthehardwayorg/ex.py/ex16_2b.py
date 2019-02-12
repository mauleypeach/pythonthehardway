#!/bin/python
#

from sys import argv
import os
import socket

script, filename, = argv

myhost =  os.getenv('HOSTNAME')
print ("Getting disk infomation for ") + (socket.gethostname()) '+' ("Recording to %r") % filename


