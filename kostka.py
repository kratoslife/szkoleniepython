import random
#dodanie powtarzania
def dodaj_kilka_razy(lista,wartosci,powtorzenie):
    for i in range(powtorzenie):

        lista.append(wartosci)


#rzut kostka
def rzut_kostka(nazwa):
    lista = []

    for i in nazwa:
        dodaj_kilka_razy(lista,i[0],i[1])

    losowanie = random.randint(0, len(lista)-1)
    return (lista[losowanie])