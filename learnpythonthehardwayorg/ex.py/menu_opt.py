#!/usr/bin/python

#version 2

import sys, os, paramiko

print (30 * '-' ) 
print ( '  MAIN MENU ' )
print (30 * '-' )
print ( "1.  bc1tcwsi101" )
print ( "2.  User management")
print ( "3.  Reboot server" )
print ( 30 * '-' )


############################
## Robust error handling  ##
## only accept int        ##
###########################
## Wait for vaild input while... not ###
is_vaild=0

while not is_vaild :
    try :
        choice = int (raw_input('Enter your choice [1-3] : '))
        is_vaild = 1  ## set it to 1 to validate input and to terminate.
    except ValueError, e  :
        print ("'%s' is not a vaild integer." % e.args[0].split(": ")[1])

### Take action as per selected menu-option ###
if choice == 1:
    print ("Starting backup...")
    print ('ssh bc1tcwsi101.ppd1.travisperkins.com')
elif choice == 2:
    print ("Starting user management...")
elif  choice == 3:
    print ("Rebooting the server...")
else:
#    print ("Invalid selection... %s" % choice)
    print ("Invalid selection..." )



