#!/bin/python
# http://anh.cs.luc.edu/handsonPythonTutorial/ifstatements.html
#
#


#weight = float(input("How many pounds does your suitcase weight?"))
#if weight > 50:
#    print("There is a 25 charge for luggage that heavy.")
#print("Thank you for your business.")

def calcWeeklyWages(totalHours, hourlyWage):
    '''Return the total weekly wages for a worker working totalHours,
    with a give regular hourlyWage .  Include overtime for hours over 40.
    '''
    if totalHours <= 40:
        totalWages = hourlyWage * totalHours
    else:
        overtime = totalHours - 40
        totalWages = hourlyWage*40 + (1.5*hourlyWage)*overtime
    return totalWages

def main():
    hours = float(input('Enter hours worked : '))
    wage = float(input('Enter pounds paid per hour : '))
    total = calcWeeklyWages(hours, wage)
    print('Wages for {hours} hours at ${wage:.2f} per hour are ${total:.2f}.'
            .format(**locals()))

main()

