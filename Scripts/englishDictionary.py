import json
from difflib import get_close_matches


data = json.load(open("/home/coreman/Downloads/dictionary.json"))


def retrieve_def(word):
    word = word.lower()

    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word, data.keys())) > 0:
        action = input("Did you mean %s instead? [y or n]: " % get_close_matches(word, data.keys())[0])
        if action == 'y':
            return data[get_close_matches(word, data.keys())[0]]
        elif action == 'n':
            return "The word doesn't exist."
        else:
            return "We don't understand your entry. sorry"


s = input()

result = retrieve_def(s)

if type(result) == list:
    for item in result:
        print("-", item)
else:
    print("-", result)
