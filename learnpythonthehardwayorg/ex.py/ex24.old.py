print "Let's practice everything."
# escapes sequences.
print 'You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.'
# Tripple quote trick.
poem = """
\t The lovely world
with logic so firmly planted
cannot discern \nthe needs of lovely
nor comprehend passion from intuition
and requires an explanation
\n\twhere there is none.
"""

print "------------"
print poem
print "------------"

# math
five = 10 - 2 + 3 -6
print "This should be five: %s" % five
# function do math with variables.
def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates

# set's multiple return variables from the function.
start_point = 10000
beans, jars, crates, = secret_formula(start_point)
# %d decimal % list variables.
print "With a starting point of: %d" % (start_point)
print "We'd have %d beans, %d jars, and %d crates." % (beans, jars, crates)

start_point = start_point / 10

print "We can also do that this way:"
print "We'd have %d beans, %d jars, and %d crates." % secret_formula(start_point)
