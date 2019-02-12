elements = []
for i in range(0,6):
    print "Adding %r to elements list." % i
    elements.append(i)
    for i in elements:
        print "Element list %r." % i

