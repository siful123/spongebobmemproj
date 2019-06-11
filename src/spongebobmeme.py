from random import randint

def sentence(x):
    y = ""
    letters = []
    for char in x:
        letters.append(str(char))
    for letter in letters:
        z = randint(1, 2)
        if letter == "":
            y += letter
        elif z == 1:
            y += letter.lower()
        elif z ==2:
            y += letter.upper()
    print(y)


sentence("hello mom")
sentence("This is a dog")
sentence("stupendously amazing brother")