import pprint
def sumeczka(*args):
    print(args)
    print(*args)
    suma = 0
    for i in (args):
        suma = suma + i
    return(suma)


print(sumeczka(5,5,5,5))









i=250
print('cos by tu bylo gdyby %d, wtedy leci ci na twarz %d' % (i,i))


print('{0:0}:!!!!!<{0:0}'.format(2,4))

lista=['ala','ma','kota']
dlugosc = [len(x) for x in lista]
dlugoscbezm = [len(x) for x in lista if 'm' not in x]
print(dlugosc)
print(dlugoscbezm)
from pprint import pprint
def szachownica(dlugosc,wysokosc):

    szach= [['-*'[(x+y)%2] for x in range(0,dlugosc)] for y in range(0,wysokosc)]
    print(szach)


szachownica(30,30)


def ranga(x):
    if x > n:
        return n
    