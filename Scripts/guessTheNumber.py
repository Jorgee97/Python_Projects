import random

print("Welcome to Guess the number, you have 3 tries to guess")
number = random.randrange(1, 10)

count = 3

while count > 0:
    inp = int(input())

    if not isinstance(inp, int):
        print("The input most be a number.")
        break

    if inp < number:
        print("The number is to Low")
    elif inp > number:
        print("The number is to High")
    else:
        print("You find the number")
        break

    count -= 1


if count == 0:
    print("You ran out of tries")

