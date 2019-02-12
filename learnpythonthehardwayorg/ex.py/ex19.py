def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print "You have %d cheeses!" % cheese_count
    print "You have %d boxes of crackers!" % boxes_of_crackers
    print "Man that's enough for a party!"
    print "Get a blanket.\n"

# we print the words and give the values of cheese and crackers as args to the function.
print "We can just give the function numbers directly:"
cheese_and_crackers(20,30)

# We assign variables then pass the variables to the function.
print "OR we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# We assign specific values after applying a calc to them
print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)

# combine varibles and math to give a final value
print "And we can combine the two, varibles and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
