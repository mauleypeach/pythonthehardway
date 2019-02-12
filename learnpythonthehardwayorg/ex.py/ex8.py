#  %r quotes with single quotes around text only.
#Should I use %s or %r for formatting?
#You should use %s and only use %r for getting debugging information about something.
#The %r will give you the "raw programmer's" version of variable,
#also known as the "representation."

formatter = "%r %r %r %r"

# Prints 1234
print formatter % (1, 2, 3, 4)
# prints one two three four
print formatter % ("one", "two", "three", "four")
# Prints 'True' 'False' 'False' 'True'
print formatter % (True, False, False, True)
# Prints %r
print formatter % (formatter, formatter, formatter, formatter)

# Prints text on one line.
print formatter % (
    "I had this thing.",
    "That you could type up right.",
    "But it didn't sing.",
    "So I said goodnight."
)

#1 2 3 4
#'one' 'two' 'three' 'four'
#True False False True
#'%r %r %r %r' '%r %r %r %r' '%r %r %r %r' '%r %r %r %r'
#'I had this thing.' 'That you could type up right.' "But it didn't sing." 'So I said goodnight.'
