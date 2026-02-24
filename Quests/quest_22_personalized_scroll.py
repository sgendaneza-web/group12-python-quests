# Quest 22: The Personalized Scroll

def personalized_greeting(name, quest):
    print(f"Hello {name}!")
    print(f"May you succeed in your quest to {quest}!")

user_name = input("Enter your name: ")
user_quest = input("Enter your quest: ")

personalized_greeting(user_name, user_quest)