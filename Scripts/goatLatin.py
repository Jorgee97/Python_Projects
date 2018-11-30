'''
    A sentence S is given, composed of words separated by spaces. Each word consists of lowercase and uppercase letters only.

    We would like to convert the sentence to "Goat Latin" (a made-up language similar to Pig Latin.)

    The rules of Goat Latin are as follows:

    If a word begins with a vowel (a, e, i, o, or u), append "ma" to the end of the word.
    For example, the word 'apple' becomes 'applema'.

    If a word begins with a consonant (i.e. not a vowel), remove the first letter and append it to the end, then add "ma".
    For example, the word "goat" becomes "oatgma".

    Add one letter 'a' to the end of each word per its word index in the sentence, starting with 1.
    For example, the first word gets "a" added to the end, the second word gets "aa" added to the end and so on.
    Return the final sentence representing the conversion from S to Goat Latin.
'''

vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']


def a_creator(i):
    return "a" * int(i+1)


def to_goat_latin(s):
    s = s.split(" ")

    for i in range(len(s)):
        # Does the string start with a vowel or a constant
        currentWord = s[i]
        if currentWord[0] in vowels:
            currentWord += "ma" + a_creator(i)
            s[i] = currentWord
        else:
            s[i] = currentWord[1:] + currentWord[0] + "ma" + a_creator(i)

    return s


def main():
    s = input()
    result = to_goat_latin(s)

    print(' '.join(result))

if __name__ == "__main__":
    main()
