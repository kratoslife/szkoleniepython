import kostka2

zielona = [('wilk', 1), ('krowa', 1), ('świnia', 1), ('owca', 3), ('królik', 6)]
czerwona = [('lis', 1), ('koń', 1), ('świnia', 2), ('owca', 2), ('królik', 6)]

#sprawdzenie
def sprawdzenie(ilosc,nazwa):

    slownik = {}

    for i in range(ilosc):
        w = kostka2.Kostka()
        slownik[w]=slownik.get(w , 0) + 1

    return slownik



#tworzenie stada
def tworzstado():
    stado = {'duży pies': 2, 'mały pies': 4, 'koń': 6, 'krowa': 12, 'świnia': 20, 'owca': 24, 'królik': 60}

    return stado

#zagroda = {}
#funkcja przeganiania zwierzat uzyta w transferze
def przeganianie(stado,zagroda,zwierz,ile_na_kostkach):

    if zwierz == 'wilk' or zwierz == 'lis':
        return
    else:
        ile_w_zagrodzie = zagroda.get(zwierz, 0)
        ile_dodac = (ile_w_zagrodzie + ile_na_kostkach) // 2
        stado[zwierz] = stado[zwierz] - ile_dodac
        zagroda[zwierz] = ile_w_zagrodzie + ile_dodac


#transfer zwierzat
def transfer(kostka1,kostka2,stado,zagroda):
    if kostka1 == kostka2:
        przeganianie(stado,zagroda,kostka1,2)
    else:
        przeganianie(stado,zagroda,kostka1,1)
        przeganianie(stado,zagroda,kostka2,1)




def rzez(masakrator, zagroda,stado):
    if masakrator == 'wilk':
        if zagroda.get('duży pies',0) > 0:
            zagroda['duży pies']=zagroda.get('duży pies')-1
            stado['duży pies'] = stado.get('duży pies') + 1
        else:
            for i in zagroda.keys():
                if i != 'koń':
                    stado[i]=stado.get(i,0)+zagroda.get(i,0)
                    zagroda[i]=0


    elif masakrator == 'lis':

        if zagroda.get('mały pies',0) > 0:
            zagroda['mały pies']=zagroda.get('mały pies')-1
            stado['mały pies']=stado.get('mały pies')+1
        else:
            zagroda['królik'] = 0