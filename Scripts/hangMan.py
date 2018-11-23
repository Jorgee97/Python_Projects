import random

words = ["house", "car", "creation", "junior", "developer", "glasses", "kitchen"]

word = words[random.randint(0, len(words) - 1)]
print(word)


def find_letters_on_word(letter):
    index = []
    for i, l in enumerate(word):
        if l == letter:
            index.append(i)
    return index


def assign_size():
    string = ""
    for i in range(0, len(word)):
        string += str(i)
    return string


def assign_value_found(my_index, guess):
    l = list(guess)
    for i, v in enumerate(my_index):
        l[v] = word[v]
    return "".join(l)


guessed = assign_size()

maximumTry = 3
while maximumTry > 0:
    maximumTry -= 1
    letter = input("Guess the word, please write one letter: \n")
    indexArray = find_letters_on_word(letter)
    if not len(indexArray) == 0:
        guessed = assign_value_found(indexArray, guessed)

    print(guessed)

if maximumTry == 0:
    guess = input("Please write the completed word: \n")

    if guess == word:
        print("You have won the game, the word was " + word.upper())
    else:
        print("You have failed, the word was " + word.upper())
