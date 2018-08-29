import random

def dodaj_kilka_razy(lista,wartosci,powtorzenie):
    for i in range(powtorzenie):

        lista.append(wartosci)



def rzut_kostka(nazwa):
    lista = []

    for i in nazwa:
        dodaj_kilka_razy(lista,i[0],i[1])

    losowanie = random.randint(0, len(lista)-1)
    return (lista[losowanie])






zielona = [('wilk', 1), ('krowa', 1), ('świnia', 1), ('owca', 3), ('królik', 6)]
czerwona = [('lis', 1), ('koń', 1), ('świnia', 2), ('owca', 2), ('królik', 6)]



def sprawdzenie(ilosc,nazwa):

    slownik = {}

    for i in range(ilosc):
        w = rzut_kostka(nazwa)
        slownik[w]=slownik.get(w , 0) + 1

    return slownik



#tworzenie stada
def tworzstado():
    stado = {'duży pies': 2, 'mały pies': 4, 'koń': 6, 'krowa': 12, 'świnia': 20, 'owca': 24, 'królik': 60}

    return stado


print(tworzstado())
zagroda = {}
#funkcja przeganiania zwierzat uzyta w transferze
def przeganianie(stado,zagroda,zwierz,ile_na_kostkach):

    ile_w_zagrodzie = zagroda.get(zwierz, 0)
    ile_dodac = (ile_w_zagrodzie + ile_na_kostkach) // 2
    stado[zwierz] = stado[zwierz] - ile_dodac
    zagroda[zwierz] = ile_w_zagrodzie + ile_dodac

#transfer zwierzat
def transfer(kostka1,kostka2,stado,zagroda):
    if kostka1 == kostka2:
        przeganianie(stado,zagroda,kostka1,2)
        print("przeganianie1",stado)
    else:
        przeganianie(stado,zagroda,kostka1,1)
        przeganianie(stado,zagroda,kostka2,1)


    print('na koniec', zagroda)
    print('na koniec',stado)


#test dla pytest
x=tworzstado()
def testujemy_test(kostka1,kostka2,stado,zagroda):

    if kostka1 == kostka2:
        przeganianie(stado,zagroda,kostka1,2)
    else:
        przeganianie(stado,zagroda,kostka1,1)
        przeganianie(stado,zagroda,kostka2,1)





