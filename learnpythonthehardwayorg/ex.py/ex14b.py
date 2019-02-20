from sys import argv

script, user_name = argv
prompt = '> '

print "Hi %s" %user_name
print "I'd like to ask you some questions."
print "Do you like me?"
likes = raw_input(prompt)

print "Where do you live %s?" %(user_name)
lives = raw_input(prompt)

print "What kind of computer do you have %s?" %(user_name)
computer = raw_input(prompt)

print """\n\nHi %s so you said you %s like me.
You live in %s.  I have no idea where that is.
And you have a %s computer.""" %(user_name, likes, lives, computer)
