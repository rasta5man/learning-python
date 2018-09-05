'''
1. projekt - 5 bodov

Napíšte program (skript v Pythone), ktorý bude vyrábať vizitky pre vašu firmu, napr. v takomto tvare

    +--------------------------------+
    |  _ _                           |
    | ( # )                          |
    |  \ /     Ing. Janko Hraško     |
    |   ^      Mňamky a Chrumky, sro |
    |          Pytliakovo 1121       |
    +--------------------------------+

Orámovanie, logo aj meno firmy podľa vlastnej fantázie - meno musí byť vaše. Využite najrôznejšie znaky, napr. ~~~~~ ***** /\/\/\/ ooooo

Vnútro vizitky mimo rámika má aspoň 5 riadkov a aspoň 30 znakov.

Program najprv prečíta zo vstupu požadovaný počet vizitiek a šírku tlače (počet znakov na riadok) - vizitiek budete tlačiť maximálny počet krát
vedľa seba. Posledný tlačený rad vizitiek tak môže byť kratší. Napr. pre šírku 120 a počet 10 vizitiek program vedľa seba vypíše 3 vizitky
(šírka našej je 34 znakov), takýchto radov vizitiek bude 4, pričom v štvrtom rade bude už len jedna vizitka. Medzi vizitkami v riadku
musí byť medzera a tiež medzi radmi vizitiek musí byť 1 riadok voľný.
'''
# 1. projekt: vizitky pre firmu Jablka a Hrusky s.r.o.
# autor: Rastislav Kovac
# dátum: 25.9.2013







pocetVizitiek = int(input('zadaj pocet vizitiek: '))
sirkaTlace = int(input('zadaj sirku tlace: '))
pocetVizitiekNaRiadok = sirkaTlace // 34 #dlzka vizitky + medzera

while pocetVizitiek > pocetVizitiekNaRiadok:
    for i in range(pocetVizitiekNaRiadok):
        print('+-------------------------------+', end = ' ')
    print()
    for i in range(pocetVizitiekNaRiadok):
        print('|   _____                       |', end = ' ')
    print()
    for i in range(pocetVizitiekNaRiadok):
        print('|  (  #  )                      |', end = ' ')
    print()
    for i in range(pocetVizitiekNaRiadok):
        print('|   \ @ /  Ing. Rastislav Kovac |', end = ' ')
    print()
    for i in range(pocetVizitiekNaRiadok):
        print('|    \ /   Owex Plus            |' ,end = ' ')
    print()
    for i in range(pocetVizitiekNaRiadok):
        print('|     *    Topolcany, Slovensko |' ,end = ' ')
    print()
    for i in range(pocetVizitiekNaRiadok):
        print('+-------------------------------+' ,end = ' ')
    print()
    pocetVizitiek = pocetVizitiek - pocetVizitiekNaRiadok

for i in range(pocetVizitiek):
    print('+-------------------------------+', end = ' ')
print()
for i in range(pocetVizitiek):
    print('|   _____                       |', end = ' ')
print()
for i in range(pocetVizitiek):
    print('|  (  #  )                      |', end = ' ')
print()
for i in range(pocetVizitiek):
    print('|   \ @ /  Ing. Rastislav Kovac |', end = ' ')
print()
for i in range(pocetVizitiek):
    print('|    \ /   Owex Plus            |' ,end = ' ')
print()
for i in range(pocetVizitiek):
    print('|     *    Topolcany, Slovensko |' ,end = ' ')
print()
for i in range(pocetVizitiek):
    print('+-------------------------------+' ,end = ' ')
print()
input()
