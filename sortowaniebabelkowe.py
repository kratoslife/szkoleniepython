#!/usr/bin/python
# -*- coding: utf-8 -*-
import random


def losuj(rozmiar, od, do):  # zwraca tablicę o podanym rozmiarze
    tab = []  # z wylosowanymi wartościami


while rozmiar > 0:  # dopóki jakieś musi dodać
    tab.append(random.randint(od, do))
rozmiar -= 1  # zmniejsza ilość pozostałych komórek do wylosowania
return tab


# wersja algorytmu w ktorej za kazdym obiegiem glownej petli
# przetwarzany jest jeden element mniej (z poczatku listy
# bo tam juz nic nie ma prawa sie zmienic - przy jednym obiegu
# na poczatek wyplywa element o najmniejszej wartosci)
def sort(tab):  # zwraca posortowaną tablicę
    for i in range(len(tab)):
        j = len(tab) - 1  # od ostatniej komórki


        while j > i:  # do aktualnie szukanej jako najmniejsza
            if tab[j] < tab[j - 1]:  # jeśli komórka wcześniej jest mniejsza, zamienia
                tmp = tab[j]
                tab[j] = tab[j - 1]
                tab[j - 1] = tmp
            j -= 1
    return tab

tab = losuj(10, 1, 10)
print "przed: " + str(tab)
tab = sort(tab)
print "   po: " + str(tab)