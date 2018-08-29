#def suma(lista):

#    ret = 0
#    for i in lista:
#        ret = ret + i
#    return ret

#print(suma(lista=[2,3,4,5]))

#def iloczyn(lista):
#
#    ret = 1
#    for i in lista:
#        ret = ret * i
#    return ret
#
#print(iloczyn(lista=[2,3,4,5]))

def duplikat(lista):

    nowalista=[]
    for i in lista:
        if i in nowalista:
            print(i)
        else:
            nowalista.append(i)
    print(nowalista)
    return nowalista



print(duplikat(lista=[3,2,3,4,5]))

