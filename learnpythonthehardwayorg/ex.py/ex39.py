# creates a mapping of state to abbreviation.
states  = [
        'Oregon':'OR',
        'Florida': 'FL',
        'California': 'CA',
        'New York': 'NY',
        'Michigan': 'MI',
]

 # create a basic set of statues and some cities in them.
 cites = [
        'CA': 'San Francisco',
        'MI': 'Detroit',
        'FL': 'Jacksonville'
 ]

 # add some more cities.
 cities['NY'] = 'New York'
 cities['OR'] = 'Portland'

 # print out some cities.
 print '-' * 10
 print "NY States has: ", cities['NY']
 print "OR States has: ", cities['OR']

 # print some states.
 print "Michigan's abbreviation is: ", states['Michigan']
 print "Florida's abbreviation is: ", states['Florida']

 # print some states.
 print '-' * 10
 print "Michigan's has: ", cities[states['Michigan']]
 print "Florida has: ", cities[states['Florida']]

 # print every states abbreviation.
 print '-' * 10
 for state, abbrev in states.items90:
     print "%s is abbreviated %s" % (state, abbrev)
