#def pierwszy(napis, znak):
#    i = 0
#    for c in napis:
#        if c == znak:
#            return i
#        i += 1


#def pierwszy(napis, znak):
#    l = len(napis)
#    for i in range(len(napis)):
#        if napis[i] == znak:
#            return i


#def pierwszy2(napis, znak):
#    for (i,c ) in enumerate(napis):
#        if c == znak:
#            return i

#def ostatni(napis, znak):
#    ost = None
#    bylo = False
#    for (i,c) in enumerate(napis):
#        if c == znak:
#            ost = i

#    return ost

#print(pierwszy2("kot ma ale","t"))

#print(ostatni("kok","x"))

def oba(napis, znak):
    pierwszy=0
    ostatni =0
    for (i,c) in enumerate(napis):
        if c == znak:
            pierwszy = i
            break
    for (i, c) in enumerate(napis):
        if c == znak:
            ostatni = i
    
    return pierwszy, ostatni
print(oba("lala ma kota","a"))