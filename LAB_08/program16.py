import random

my_hidden_int = random.randint(1, 100)

user_int = 0

while user_int != my_hidden_int:
    user_int = int(input("Give me your magic number:"))
    if user_int > my_hidden_int:
        print("Too high, try again.")
    elif user_int < my_hidden_int:
        print("Too low, try again")
    else:
        print("Congrulations !")
