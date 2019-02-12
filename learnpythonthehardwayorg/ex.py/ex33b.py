#number = int(raw_input("Enter a number: "))
#i = 0
#numbers = []
def countto(number,inc):
    i = 0
    numbers = []
    while i < number:
        print "At the top i is %d" % i
        numbers.append(i)

        i = i + inc
        print "Numbers now: ", numbers
        print "At the bottom i is %d" % i


    print "The numbers: "


    for num in numbers:
        print num

#while_loop(int(raw_input("Enter a number: ")), int(raw_input("Enter increment: ")))
countto(int(raw_input("Enter a number:> ")),int(raw_input("Enter an incrament:> ")))
