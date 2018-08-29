#d = {10: 'ala', 15:'ma', 5:'kot'}
#for k,v in d.items():
#    print('klucz {k}, wartosc {v}'.format (k=k, v=v))




ewidencja = []
def add_new(ew, name, age, salary):
    """dodaje nowego pracownika do ewidencji"""


    nowa_osoba = {'imie': name, 'wiek': age, 'zarobki': salary}


    ew.append(nowa_osoba)


print(add_new(ewidencja,'Mateusz',20,3000))
print(add_new(ewidencja,'Lukasz',30,5000))
print(add_new(ewidencja,'Jan',40,4000))

def print_all(ew):
    """drukuje ewidencje"""
    for a in ewidencja:
        print("Pracownik o imieniu", a.get('imie') ,"ktory ma", a.get('wiek') ,"lat i jego zarobki to", a.get('zarobki'))

print(print_all(ewidencja))
def salary_avg(ew):
    """zwraca srednie zarobki"""
    suma=0
    srednie=0
    for a in ew:
        suma = suma + a.get('zarobki')
        srednie = suma/len(ew)
    print(suma)
    print(srednie)

    return srednie
print(salary_avg(ewidencja))
