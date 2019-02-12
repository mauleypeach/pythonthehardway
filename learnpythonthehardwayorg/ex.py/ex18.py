# this is like you scripts with argv. 
def print_two(*args):
    arg1, arg2, = args
    print "args1: %r, arg2: %r" %(arg1, arg2)

# ok, that *args is actually pointless, we can actually just do this.
def print_two_again(arg1, arg2):
    print "args1: %r, args2: %r" %(arg1, arg2)

# this one takes one argument.
def print_one(arg1):
    print "args1: %r" % arg1
    
# this one takes no arguments.
def print_none():
    print "I got nothing."


print_two("Mauli", "Prakash")
print_two_again("Zed","shaw")
print_one("one_arg")
print_none()

