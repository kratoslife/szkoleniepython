import random
import kostka2
import logikagry
#dodanie powtarzania

zielona = [('wilk', 1), ('krowa', 1), ('świnia', 1), ('owca', 3), ('królik', 6)]
czerwona = [('lis', 1), ('koń', 1), ('świnia', 2), ('owca', 2), ('królik', 6)]


def rozgrywka():
    wartosckostki1 = kostka2.Kostka(zielona)
    wartosckostki2 = kostka2.Kostka(czerwona)
    zagrody_graczy=[]
    stadograczy=logikagry.tworzstado()
    gracze=input('Podaj liczbe graczy: ')
    ruch=input('Podaj ilosc rzutow: ')
    gracze=int(gracze)
    ruch=int(ruch)
    if gracze < 2:
        print("Podales za mala ilosc graczy, chcesz grac sam?!")
        return
    elif gracze > 6:
        print("Podales za duza ilosc graczy!")
        return
    else:
        for i in range(gracze):
            zagrody_graczy.append({})
        while ruch > 0:
            for j in range(gracze):

                rzut = wartosckostki1.losuj()
                rzut2 = wartosckostki2.losuj()
                logikagry.transfer(rzut,rzut2,stadograczy,zagrody_graczy[j])
                #print(wywolanie)
                print(ruch)
                print("gracz: ",j)
                print('rzut 1',rzut)
                print('rzut 2',rzut2)
                print("stado",stadograczy)
                print("pokaz zagrode",zagrody_graczy[j])
                #for e in zagrody_graczy[j].values():
                    #if e == 0:
                        #print("przegrales")
                    #else:
                        #print('wygrales')
            ruch -= 1

print(rozgrywka())
#x=tworzstado()
#y=transfer('mały pies','mały pies',x,zagroda)
#y=transfer('królik','królik',x,zagroda)
#y=transfer('koń','koń',x,zagroda)
#print(rzez('lis',zagroda,x))
#print(zagroda)
#print(x)


#test# dla pytest

#def testujemy_test(kostka1,kostka2,stado,zagroda):
#
#    if kostka1 == kostka2:
#        przeganianie(stado,zagroda,kostka1,2)
#    else:
#        przeganianie(stado,zagroda,kostka1,1)
#        przeganianie(stado,zagroda,kostka2,1)