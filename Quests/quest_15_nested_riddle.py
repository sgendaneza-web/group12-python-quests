choice1 = input("Do you go left or right? ").lower()

if choice1 == "left":
    choice2 = input("Do you swim or wait? ").lower()
    if choice2 == "swim":
        print("You found a treasure!")
    else:
        print("You waited too long and missed the treasure.")
else:
    print("You went right and fell into a trap!")