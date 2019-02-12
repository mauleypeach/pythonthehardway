# write a python function and run that 10 different ways.
#
#
# My function will calulate a total for how good 
# charlie and hudson have been today.

# take a number for charlie and one for hudson and add them,

from datetime import date

good_report= '/tmp/doggie_report.txt'

def goodness(sc_char, sc_hud):
    total = (sc_char + sc_hud) / 2
    today = date.today()
    print("\nThey scored an average of %r points today : %r/%r/%r." ) % (total, today.day, today.month, today.year)
    line = ("Charlie " + str(charlie_score),"Hudson " + str(hudson_score)+", " + "Average: " + str(total) + " " + str(today))
    good_rep = open(good_report,'a')
    good_rep.write(str(line)+ "\n")
    good_rep.close()



# How good has Charlie been
charlie_score = int(raw_input("Please rate Charlies' goodness. "))
print ("""You said Charlie scored %r.""") % charlie_score

# How good has Hudson been
hudson_score = int(raw_input("Please rate Hudson's goodness. "))
print ("You said Hudson scored %r.") % hudson_score


# Function to average scores
goodness(charlie_score, hudson_score)

# Get last score
good_rep = open(good_report,'r')
line = good_rep.read().splitlines()
last = line[-2]
print ("\nTheir last score was : %r ") % last

# Write results to a file
print( "\nWritng this info to %r." ) % good_report




