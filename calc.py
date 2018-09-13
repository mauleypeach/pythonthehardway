# def add (x, y):
#     return (x + y)
#
# def subtract (x, y):
#     return (x - y)
#
# def multiply (x, y):
#     return (x * y)
#
# def divide (x, y):
#     return (x/y)
#
# print("Select an operation: 1 - Add, 2 - Subtract, 3 - Multiply, 4 - Divide")
#
# choice = raw_input("Please choose an option: ")
# numb1 = int(raw_input("Please input the first number: "))
# numb2 = int(raw_input("Please input the second number: "))
#
# if choice == "1":
#     print (numb1, '+', numb2, '=', add(numb1, numb2))
# elif choice == "2":
#     print (numb1, '-', numb2, '=', subtract(numb1, numb2))
# elif choice == "3":
#     print (numb1, '*', numb2, '=', multiply(numb1, numb2))
# elif choice == "4":
#     print (numb1, '/', numb2, '=', divide(numb1, numb2))
# else:
#     print("Please input a valid choice")

# def recursion(numb):
#     if numb == 1 or numb == 0:
#         return 1
#     return numb * recursion(numb - 1)
#
# print("The factorial equals: ", recursion(int(raw_input("Please input a number: "))))

# import itertools, random
#
# deck = list(itertools.product(range(1,14),['Spade', 'Club', 'Heart', 'Diamond']))
#
# random.shuffle(deck)
#
# print("You got:")
# for i in range(6):
#     print(deck[i][0], 'of', deck[i][1])

# Palindrome = raw_input("Please input a word: ")
# palindrome = Palindrome.lower()
# emordnilap = reversed(palindrome)
# if list(palindrome) == list(emordnilap):
#     print(palindrome, "is a palindrome")
# else:
#     print(Palindrome, "isn't a palindrome")
