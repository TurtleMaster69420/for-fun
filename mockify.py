from random import randint
while True:
    string = input("I want to mockify the following: ")
    newstring = []
    for letter in string:
        thing = randint(1,2)
        if thing == 1:
            newstring.append(letter.lower())
        else:
            newstring.append(letter.upper())

    print("".join(newstring))
