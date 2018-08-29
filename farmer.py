import random
zielona = ['wilk','krowa','świnia','owca','owca','owca','krolik','krolik','krolik','krolik','krolik','krolik']
czerwona = ['lis','koń','świnia','świnia','owca','owca','krolik','krolik','krolik','krolik','krolik','krolik']
def rzut_kostka(kostka):

    randomowa = ''
    randomowa2 = ''
    for i in zielona:

        randomowa = random.randint(1,12)

    return randomowa
    print(randomowa)

    for j in czerwona:

        randomowa2 = random.randint(1,12)

    return randomowa2
    print(randomowa2)



print(rzut_kostka(zielona))
print(rzut_kostka(czerwona))