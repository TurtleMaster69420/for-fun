# Now you can mock people... without having to manually making each letter lowercase or uppercase! How revolutionary (I bet no one has ever done this)
# And it's free! That's a great price!


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
