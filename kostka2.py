import random

class Kostka:

    def __init__(self,opis):
        self.opis_kostki=opis


    def losuj(self):
        lista=[]
        for e in self.opis_kostki:
            for i in range(e[1]):
                    lista.append(e[0])
                    los=random.randint(1,len(lista))

        return(lista[los-1])

zielona = [('wilk', 1), ('krowa', 1), ('świnia', 1), ('owca', 3), ('królik', 6)]
czerwona = [('lis', 1), ('koń', 1), ('świnia', 2), ('owca', 2), ('królik', 6)]

cus = Kostka(zielona)
print(cus.losuj())