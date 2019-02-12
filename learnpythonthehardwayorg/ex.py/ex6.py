# using / replacing %d with 10
x = "There are %d types of people." %10
# There are 10 types of people.

# sets variables.
binary = "binary"
do_not = "don't"

#  Swaps our variables, note the brackets.
y = "Those who know %s and those who %s." % (binary, do_not)
# Those who know binary and those who don't.


print x
print y

#######################################
#  uses a %r that return a repr().  not sure what but python execute
# note the brackets are added. %r returns raw text
print "I said: %r." %x
# I said: 'There are 10 types of people.'.

#The brackes here are from the txt within the print. None added.
print "I also said: '%s'." % y
#I also said: 'Those who know binary and those who don't.'.

# set a variable to False and %r returns no brackets because a boolean is set.
# %r returns raw text.
hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

print joke_evaluation % hilarious
#Isn't that joke so funny?! False

# As expected adding strings works.
w = "This is the left side of..."
e = "a string with a right side."

print w + e
