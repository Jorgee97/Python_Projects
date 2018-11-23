import random

print("Press R to roll the dice and S to stop the program.")

inp = input()

while inp != "S":
    if inp == "R":
        print(random.randrange(1, 6), end="\n")

    inp = input()
