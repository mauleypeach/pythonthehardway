from sys import argv

# open a file and print it out.
script, filename = argv
txt = open(filename)

print txt.read()

print "Your file is called %s." % filename
