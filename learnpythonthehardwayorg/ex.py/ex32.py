the_count = [1,2,3,4,5]
fruits = ['apples','oranges','pears','apricots']
change = [1,'pennies',2,'dimes',3,'quarters']

# this first kind of for-loop goes through a list
for number in the_count:
    print "This is the count %d" % number

# same as above for fruits
for fruit in fruits :
    print "A fruit of type: %s" % fruit

# also we can go through mixed lists too
# notice we use %r (meaning raw_data) because we don't know what's in the list.
for i in change :
    print "I got %r" % i

# we can also build list, first start with an empty list. 
elements = []

print "count using range function" # then user the range function to do 0 to 5 counts. 
for i in range(0,6):
    print "Adding %d to the list." % i
    # append is a function that lists understand. 
    elements.append(i)

# now we can print them out too
for i in elements:
    print "Element was %d" %i
