#You are a superhero and have to save the princess.
#The princess is in a locked tower.
# you sneak around and get to two doors(right or left) using a clue.
def start():
    print("You're a superhero whose going to save the princess.\n")
    print("You're in front of the tower she's locked in.\n")
    print("Will you enter the tower or leave?\n")

    choice = input("Type 'tower' or 'leave': ").strip().lower()

    if choice == "tower":
        tower()
    elif choice == "leave":
        leave()
    else:
        print("Invalid choice")
        start()


def tower():
    print("\nYou walk into the scary tower.\n")
    print("You see two different doors on the right and left.\n")
    print("You reach for the scroll between the two doors and read the message.\n")
    print("Rusted hinges creak and groan,\n"
          "In dust and shadow stands alone.\n"
          "Grand designs may charm the eye,\n"
          "Hollow promises often lie.\n"
          "Trust the door that time forgot.\n")

    choice = input("Will you choose the 'right door' or the 'left door': ").strip().lower()

    if choice == "right door":
        print("\nHurray! You've rescued the princess!")
        print("You win!")
    elif choice == "left door":
        print("\nYou've been killed by the dragon!")
        print("You lose!")
    else:
        print("Invalid choice")
        tower()


def leave():
    print("\nBye bye!")


start()






    