#wiek = 15
#if wiek < 18:
#    print('dozwolone od lat 18')
#print(wiek)


#imie = 'Alin'
#if imie[-1] == 'a':
#    print('Pani ' + imie)
#if imie[-1] != 'a':
#    print('Pan ' + imie)

#imie = 'Bodzio'
#if imie[-1] == 'a':
#    print ('Pani ' + imie)
#elif imie[-1] == 'o':
#    print ("Panio " + imie)
#else:
#    print ('Pan ' + imie)


#a = 'labas'
#pierw = False
#for zmienna in a:
#    if zmienna == 'a' and not pierw:
#        print('X')
#        pierw = True
#    else:
#        print(zmienna)


#1
#def zmienia (napis):
#    pierw = False
#    for a in napis:
#            if a == 'a' and not pierw:
#                print('X')
#               pierw = True
#            else:
#                print(a)

#zmienia('aa')

##2
#def lista(a):
#    b = []
#    b.append(a[0])
#    b.append(a[-1])
#    return b

#print(lista([7,2,3,4]))

#3
#def funkcja(napis,znak):
#    wystepuje=0
#    for znak in napis:
#        wystepuje += 1
#    return wystepuje

#print(funkcja('1111','1'))



#4
#def cus(napis):
#    zwrot = ''
#    for lista in napis:
#        zwrot = lista + zwrot
#    return zwrot

#print(cus('ala ma kota'))

#5
def rev(napis):
    wyraz = ''
    ret = ''

    for c in napis:
        if c != ' ':
            wyraz = wyraz + c
        else:
            ret = wyraz + ' ' + ret
            wyraz = ''

    ret = wyraz + ' ' + ret
    return ret[:-1]

print(rev('ala ma kota'))

#6
def rev(napis):
    ret = ''
    l=len(napis)
    for i in range(l):
        ret = ret + napis[l-i-1]
    return ret
print(rev('kot'))


#def rev(rozmiar,start):
#    ret = ''
#    for i in range(rozmiar):
#        if (i+start) % 2:
#            ret += '*'
#        else:
#            ret += '.'
#
#    return ret


#def rev2(rozmiar):
#    ret = ''
#    for i in range(rozmiar):
#        ret.append(rozmiar, i%2)
#
#    return ret
#
#print(rev2(2))
