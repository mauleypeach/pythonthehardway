from sys import exit

def gold_room():
    print "This room is full of gold. How much do you take?"

    next = raw_input("> ")
    if "0" in next or "1" in next:
        how_much = int(next)
    else:
        dead("Man, learn to type a number.")

    if how_much < 50:
        print "Nice, you're not greedy, you win!"
        exit(0)
    else:
        dead("You greedy monkey!")

def dodgeroom():
    print "The room is full of spikes and a swinging axe."
    print "What will you do? Dodge left, right or flee?"
    next = raw_input("> "),

    if "left" in next:
        print "The axe swings to the right and you find a secret door."
        gold_room()
    elif "right" in next:
        print "You jump to right and the axe takes your arm."
        dead("You fall on the spikes never to be seen again.")
    elif "flee" in next:
        dead("You run straight into the angry bear who eats you.")
    else:
        print "That's not an option!"

def bear_room():
    print "There is a bear here."
    print "The bear has a bunch of honey."
    print "The fat bear is in front of another door."
    print "How are you going to move the bear?"
    bear_moved = False

    while True:
        next = raw_input("> ")

        if "take" in next or "honey" in next:
            dead("The bear looks at you then slaps your face off.")
        elif "taunt" in next and not bear_moved:
            print "The bear has moved from the door. You can go through it now."
            bear_moved = True
        elif "taunt" in next and bear_moved:
            dead("The bear gets pissed off and chews your leg off.")
        elif "open" in next and bear_moved:
            dodgeroom()
        else:
            print "I got no idea what that means."

def cthulhu_room():
    print "Here you see the grreat evil Cthulhu."
    print "He, it, whatever stares at you and you go insane."
    print "Do you flee for your life or eat your head?"

    next = raw_input("> ")

    if "flee" in next:
        start()
    elif "head" in next:
        dead("Well that was tasty!")
    else:
        cthulhu_room()


def dead(why):
    print why, "Good job!"
    exit(0)

def start():
    print "You are in a dark room."
    print "There is a door to your right and left."
    print "Which one do you take?"

    next = raw_input("> ")

    if next == "left":
        bear_room()
    elif next == "right":
        cthulhu_room()
    else:
        dead("You stumble around the room till you starve.")


start()
