i = 0
numbers = []

x = int(raw_input("What is the max number to count too? \n>"))
y = int(raw_input("What is the increment to use? \n>"))

while i < x:
    print "At the top i is %d" % i
    numbers.append(i)

    i = i + y
    print "Numbers now: ", numbers
    print "At the bottom i is %d" % i


print "The Numbers: "

for num in numbers:
    print num

# doing this a for loop using range.
i = 0

print "\n\n\nusing for loop with %r %r %r" % (i, x, y)

for i in range(i,x,y):
    print "My for loop numbers are: %r" % i 

# doing this as a function
print "\n\n\nOutput as a function."
i = 0
maulilist = []

def mauli(i,x,y):
    while i < x:
        print "At the top i is %d" % i
        maulilist.append(i)
        i += y
        print "Numbers are now: ", maulilist
        print "At the bottom i is %d" % i

mauli(i,x,y)
