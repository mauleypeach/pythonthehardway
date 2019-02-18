#!/bin/python
i = 0
numbers = []

while i < 10:
    print (" i is at the value %r") %i
    numbers.append(i)
    i = i + 1
    print (" i is now at value %r") %i

print "The numbers are :"

for num in numbers:
    print ("%r") %num



# rewrite as function
countto = input("Enter the number to count to : ")
numbers = []
def count(countto):
   """This is a rebuild using functions"""
   i = 0 
   while i < countto:
       print("At the top i is %r") %i
       numbers.append(i)
       i = i + 1
       print ("At the bottom i is %r") %i

count(countto)
print ("The numbers are : -")

for num in numbers:
    print num
