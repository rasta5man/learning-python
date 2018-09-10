'''3. projekt - 5 bodov

Napíšte program, ktorý v textovom režime

1 v prvých troch parametroch funkcie kalendar dostáva nejaký dátum (deň, mesiac, rok)

2 skontroluje, či je to korektný dátum v intervale <1.1.1901, 31.12.2100>, ak nie, vypíše o tom správu (deň. mesiac. rok je zle zadaný dátum) a pokračuje v kroku 6
3 vypíše, koľko dní uplynulo k tomuto dátumu od 1.1.1901
4 vypíše aký deň v týždni je zadaný dátum
5 vypíše kalendár na celý mesiac, v ktorom sa nachádza zadaný dátum
    kalendár je vypísaný tak, že čísla v prvom stĺpci zodpovedajú pondelkom, v druhom stĺpci utorkom, ... v poslednom 7 stĺpci nedeliam
     dajte si záležať na správnom formátovaní, aby boli všetky stĺpce zarovnané vpravo 
6 v ďalších troch parametroch funkcie kalendar dostáva ďalší dátum (deň, mesiac, rok)
7 robí to isté ako s prvým dátumom: skontroluje správnosť, vypočíta počet dní od 1.1.1901 a deň v týždni
8 vypíše kalendár pre daný mesiac, ale len vtedy, keď sa líši od už vypisovaného kalendára pre prvý dátum 

Priebeh by mal vyzerať takto

    >>> kalendár(15, 5, 2002, 7, 1, 2003)
    počet dní od 1.1.1901 do 15.5.2002 = ????
    15.5.2002 = streda
    Kalendár pre máj 2002
            1  2  3  4  5
      6  7  8  9 10 11 12
     13 14 15 16 17 18 19
     20 21 22 23 24 25 26
     27 28 29 30 31
    ---
    počet dní od 1.1.1901 do 7.1.2003 = ????
    7.1.2003 = utorok
    Kalendár pre január 2003
    Použi ten istý kalendár ako pre máj 2002
    >>>

Zadefinujte a v programe využite minimálne tieto funkcie (parametre si zvoľte podľa potreby):

    kalendar(...)             # štart celého programu
    dobry_datum(...)          # zistí, či je dátum korektný
    pocet_dni(...)            # zistí počet dní od 1.1.1901 k zadanému dátumu
    pocet_dni_v_mesiaci(...)  # vypočíta počet dní v danom mesiaci a roku (pre zistenie priestupnosti roku)
    meno_mesiaca(...)         # vráti meno príslušného mesiaca, napr. 'január', 'február', ...
    meno_dna(...)             # meno dna v týždni, napr. 'pondelok', 'utorok', ...
    vypis_kalendar(...)       # vypíše kalendár pre daný mesiac vo špecifikovanom formáte

Môžete predpokladať, že 1.1.1901 bol utorok. Preto deň, ktorý je od tohto dátumu vzdialený násobok 7 je tiež utorok. Kontrolovať výpočty dátumov môžete napr. na stránke pracovný kalenár.

Váš odovzdaný program musí začínať tromi riadkami komentárov:

    # 3. projekt: kalendar
    # autor: Janko Hraško
    # dátum: 10.10.2013

Používajte len také konštrukcie jazyka Python, ktoré sme sa zatiaľ učili. Nepoužívajte napr. zoznamy a ani iné štruktúry.
'''





# spustacia funkcia 
def kalendar(den, mesiac, rok, inyDen, inyMesiac, inyRok):
    dobryDatum(den, mesiac, rok, inyDen, inyMesiac, inyRok)
    menoDna1(den, mesiac, rok, inyDen, inyMesiac, inyRok)
    menoDna2(den, mesiac, rok, inyDen, inyMesiac, inyRok)
    print('Pocet dni od 1.1.1901 po ', den,'.',mesiac,'.',rok,' = ', pocetDni1(den, mesiac, rok, inyDen, inyMesiac, inyRok))
    print('Pocet dni od 1.1.1901 po ', inyDen,'.',inyMesiac,'.',inyRok,' = ', pocetDni2(den, mesiac, rok, inyDen, inyMesiac, inyRok))
    pocet = abs(pocetDni1(den, mesiac, rok, inyDen, inyMesiac, inyRok) - pocetDni2(den, mesiac, rok, inyDen, inyMesiac, inyRok))
    print('Pocet dni od', den,'.',mesiac,'.',rok,' po', inyDen,'.',inyMesiac,'.',inyRok,' = ', pocet)
    vypisKalendara(den, mesiac, rok, inyDen, inyMesiac, inyRok)


# funkcia skontroluje, ci je datum spravne zadany a ak nie, vypise o tom spravu    
def dobryDatum(den, mesiac, rok, inyDen, inyMesiac, inyRok):
    if rok in range(1901,2101):
        if mesiac == 1 or mesiac==3 or mesiac ==5 or mesiac ==7 or mesiac ==8 or mesiac==10 or mesiac==12:
            if den not in range(1,32):
                print ('deň je zle zadaný dátum')
            else:
                print('zadali ste datum: ', den,'.',mesiac,'.',rok)
        if mesiac == 4 or mesiac==6 or mesiac ==9 or mesiac ==11:
            if den not in range(1,31):
                print ('deň je zle zadaný dátum')
            else:
                print('zadali ste datum: ', den,'.',mesiac,'.',rok)
        if mesiac == 2 and rok%4 == 0:
            if den not in range(1,30):
                print ('deň je zle zadaný dátum')
            else:
                print('zadali ste datum: ', den,'.',mesiac,'.',rok)
        if mesiac == 2 and rok%4 != 0:
            if den not in range(1,29):
                print ('deň je zle zadaný dátum')
            else:
                print('zadali ste datum: ', den,'.',mesiac,'.',rok)
    else:
        print('rok je zle zadaný dátum')
    if mesiac not in range(1,13):
        print('mesiac je zle zadaný dátum')
    if den not in range(1,32):
        print ('deň je zle zadaný dátum')
        
    #kontrola zadania pre iny rok
    if inyRok in range(1901,2101):
        if inyMesiac == 1 or inyMesiac==3 or inyMesiac ==5 or inyMesiac ==7 or inyMesiac ==8 or inyMesiac==10 or inyMesiac==12:
            if inyDen not in range(1,32):
                print ('deň je zle zadaný dátum')
            else:
                print('zadali ste datum: ', inyDen,'.',inyMesiac,'.',inyRok)
        if inyMesiac == 4 or inyMesiac==6 or inyMesiac ==9 or inyMesiac ==11:
            if inyDen not in range(1,31):
                print ('deň je zle zadaný dátum')
            else:
                print('zadali ste datum: ', inyDen,'.',inyMesiac,'.',inyRok)
        if inyMesiac == 2 and inyRok%4 == 0:
            if inyDen not in range(1,30):
                print ('deň je zle zadaný dátum')
            else:
                print('zadali ste datum: ', inyDen,'.',inyMesiac,'.',inyRok)
        if inyMesiac == 2 and inyRok%4 != 0:
            if inyDen not in range(1,29):
                print ('deň je zle zadaný dátum')
            else:
                print('zadali ste datum: ', inyDen,'.',inyMesiac,'.',inyRok)
    else:
        print('rok je zle zadaný dátum')
    if inyMesiac not in range(1,13):
        print('mesiac je zle zadaný dátum')
    if inyDen not in range(1,32):
        print ('deň je zle zadaný dátum')


# funkcia vypocita pocet dni od 1.1.1901 az po prvy zadany datum      
def pocetDni1(den, mesiac, rok, inyDen, inyMesiac, inyRok):
    # nasledujuci for cyklus prida pocet dni podla poctu prestupnych rokov k zadanemu roku
    pridaj1 = 0
    for i in range(1904, 2104, 4):
            if rok >= i:
                pridaj1 += 1

    if mesiac == 1:
        if  rok in range(1904,2104,4):
            pocetDni = 365*(rok - 1901) + den + pridaj1 - 1
        else:
            pocetDni = 365*(rok - 1901) + den + pridaj1
    elif mesiac == 2:
        if  rok in range(1904,2104,4):
            pocetDni = 365*(rok - 1901) + den + 31 + pridaj1 - 1
        else:
            pocetDni = 365*(rok - 1901) + 31 + den + pridaj1
    elif mesiac == 3:
        pocetDni = 365*(rok - 1901) + 31 + 28 + den+ pridaj1
    elif mesiac == 4:
        pocetDni = 365*(rok - 1901) + 31 + 28 + 31 + den+ pridaj1
    elif mesiac == 5:
        pocetDni = 365*(rok - 1901) + 31 + 28 + 31 + 30 + den+ pridaj1
    elif mesiac == 6:
        pocetDni = 365*(rok - 1901) + 31 + 28 + 31 + 30 + 31 + den+ pridaj1
    elif mesiac == 7:
        pocetDni = 365*(rok - 1901) + 31 + 28 + 31 + 30 + 31 + 30 + den+ pridaj1
    elif mesiac == 8:
        pocetDni = 365*(rok - 1901) + 31 + 28 + 31 + 30 + 31 + 30 + 31 + den+ pridaj1
    elif mesiac == 9:
        pocetDni = 365*(rok - 1901) + 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + den+ pridaj1
    elif mesiac == 10:
        pocetDni = 365*(rok - 1901) + 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + den+ pridaj1
    elif mesiac == 11:
        pocetDni = 365*(rok - 1901) + 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31 + den+ pridaj1
    elif mesiac == 12:
        pocetDni = 365*(rok - 1901) + 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31 + 30 + den+ pridaj1
    
    return pocetDni


#funkcia vypocita pocet dni od 1.1.1901 az po druhy zadany datum
def pocetDni2(den, mesiac, rok, inyDen, inyMesiac, inyRok):    
    # priestupne roky
    pridaj2 = 0
    for i in range(1904, 2104, 4):
            if inyRok >= i:
                pridaj2 += 1
        
    if inyMesiac == 1:
        if  inyRok in range(1904,2104,4):
            inyPocetDni = 365*(inyRok - 1901) + inyDen + pridaj2 - 1
        else:
            inyPocetDni = 365*(inyRok - 1901) + inyDen + pridaj2
    elif inyMesiac == 2:
        if  inyRok in range(1904,2104,4):
            inyPocetDni = 365*(inyRok - 1901) + inyDen + 31 + pridaj2 - 1
        else:
            inyPocetDni = 365*(inyRok - 1901) + 31 + inyDen + pridaj2
    elif inyMesiac == 3:
        inyPocetDni = 365*(inyRok - 1901) + 31 + 28 + inyDen+ pridaj2
    elif inyMesiac == 4:
        inyPocetDni = 365*(inyRok - 1901) + 31 + 28 + 31 + inyDen+ pridaj2
    elif inyMesiac == 5:
        inyPocetDni = 365*(inyRok - 1901) + 31 + 28 + 31 + 30 + inyDen+ pridaj2
    elif inyMesiac == 6:
        inyPocetDni = 365*(inyRok - 1901) + 31 + 28 + 31 + 30 + 31 + inyDen+ pridaj2
    elif inyMesiac == 7:
        inyPocetDni = 365*(inyRok - 1901) + 31 + 28 + 31 + 30 + 31 + 30 + inyDen+ pridaj2
    elif inyMesiac == 8:
        inyPocetDni = 365*(inyRok - 1901) + 31 + 28 + 31 + 30 + 31 + 30 + 31 + inyDen+ pridaj2
    elif inyMesiac == 9:
        inyPocetDni = 365*(inyRok - 1901) + 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + inyDen+ pridaj2
    elif inyMesiac == 10:
        inyPocetDni = 365*(inyRok - 1901) + 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + inyDen+ pridaj2
    elif inyMesiac == 11:
        inyPocetDni = 365*(inyRok - 1901) + 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31 + inyDen+ pridaj2
    elif inyMesiac == 12:
        inyPocetDni = 365*(inyRok - 1901) + 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31 + 30 + inyDen+ pridaj2
           
    return inyPocetDni


# vypocita meno dna pre zadany datum - pondelok, utorok, streda, atd ...   
def menoDna1(den, mesiac, rok, inyDen, inyMesiac, inyRok):
    pocet1 = pocetDni1(den, mesiac, rok, inyDen, inyMesiac, inyRok)
    pondelok, utorok, streda, stvrtok, piatok, sobota, nedela = 'Pondelok','Utorok','Streda','Stvrtok','Piatok','Sobota','Nedela'
    if pocet1 in list(range(1, 73051, 7)):
        menoDna = utorok
    elif pocet1 in list(range(2, 73051, 7)):
        menoDna = streda
    elif pocet1 in list(range(3, 73051, 7)):
        menoDna = stvrtok
    elif pocet1 in list(range(4, 73051, 7)):
        menoDna = piatok
    elif pocet1 in list(range(5, 73051, 7)):
        menoDna = sobota
    elif pocet1 in list(range(6, 73051, 7)):
        menoDna = nedela
    elif pocet1 in list(range(7, 73051, 7)):
        menoDna = pondelok    
    print(den,'.',mesiac,'.',rok,' = ', menoDna)
    return menoDna


# vypocita meno dna pre druhy zadany datum - pondelok, utorok, streda, atd ...  
def menoDna2(den, mesiac, rok, inyDen, inyMesiac, inyRok):
    pocet2 = pocetDni2(den, mesiac, rok, inyDen, inyMesiac, inyRok)
    pondelok, utorok, streda, stvrtok, piatok, sobota, nedela = 'Pondelok','Utorok','Streda','Stvrtok','Piatok','Sobota','Nedela'
    if pocet2 in list(range(1, 73051, 7)):
        menoDna = utorok
    elif pocet2 in list(range(2, 73051, 7)):
        menoDna = streda
    elif pocet2 in list(range(3, 73051, 7)):
        menoDna = stvrtok
    elif pocet2 in list(range(4, 73051, 7)):
        menoDna = piatok
    elif pocet2 in list(range(5, 73051, 7)):
        menoDna = sobota
    elif pocet2 in list(range(6, 73051, 7)):
        menoDna = nedela
    elif pocet2 in list(range(7, 73051, 7)):
        menoDna = pondelok
    print(inyDen,'.',inyMesiac,'.',inyRok,' = ', menoDna)
    return menoDna

        
#vypise kalendar pre zadany mesiac v zadanom roku     
def vypisKalendara(den, mesiac, rok, inyDen, inyMesiac, inyRok):
    den = 1
    prvyDen = menoDna1(den, mesiac, rok, inyDen, inyMesiac, inyRok)
        
    if mesiac == 1 and prvyDen== 'Pondelok':
        print('Kalendar pre Januar', rok)
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format('po','ut','st','st','pi','so','ne'))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(1,2,3,4,5,6,7))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(8,9,10,11,12,13,14))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(15,16,17,18,19,20,21))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(22,23,24,25,26,27,28))
        print('{:>3}{:>3}{:>3}'.format(29,30,31))
    if mesiac == 1 and prvyDen == 'Utorok':
        print('Kalendar pre Januar', rok)
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format('po','ut','st','st','pi','so','ne'))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format('',1,2,3,4,5,6))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(7,8,9,10,11,12,13))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(14,15,16,17,18,19,20))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(21,22,23,24,25,26,27))
        print('{:>3}{:>3}{:>3}{:>3}'.format(28,29,30,31))
    if mesiac == 1 and prvyDen== 'Streda':
        print('Kalendar pre Januar', rok)
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format('po','ut','st','st','pi','so','ne'))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format('','',1,2,3,4,5))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(6,7, 8,9,10,11,12))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(13,14,15,16,17,18,19))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(20,21,22,23,24,25,26))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}'.format(27,28,29,30,31))
    if mesiac == 1 and prvyDen== 'Stvrtok':
        print('Kalendar pre Januar', rok)
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format('po','ut','st','st','pi','so','ne'))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format('','','', 1,2,3,4))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(5,6,7, 8,9,10,11))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(12,13,14,15,16,17,18))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(19,20,21,22,23,24,25))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(26, 27,28,29,30,31))
    if mesiac == 1 and prvyDen== 'Piatok':
        print('Kalendar pre Januar', rok)
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format('po','ut','st','st','pi','so','ne'))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format('','','', '',1,2,3))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(4,5,6,7, 8,9,10))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(11,12,13,14,15,16,17))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(18,19,20,21,22,23,24))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(25,26, 27,28,29,30,31))
    if mesiac == 1 and prvyDen== 'Sobota':
        print('Kalendar pre Januar', rok)
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format('po','ut','st','st','pi','so','ne'))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format('','','', '','', 1,2))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(3, 4,5,6,7, 8,9))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(10, 11,12,13,14,15,16))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(17,18,19,20,21,22,23))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(24,25,26, 27,28,29,30))
        print('{:>3}'.format(31))
    if mesiac == 1 and prvyDen== 'Nedela':
        print('Kalendar pre Januar', rok)
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format('po','ut','st','st','pi','so','ne'))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format('','','', '','','', 1))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(2,3, 4,5,6,7, 8))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(9,10, 11,12,13,14,15))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(16,17,18,19,20,21,22))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(23,24,25,26, 27,28,29))
        print('{:>3}{:>3}'.format(30,31))

    if mesiac == 3 and prvyDen== 'Pondelok':
        print('Kalendar pre Marec', rok)
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format('po','ut','st','st','pi','so','ne'))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(1,2,3,4,5,6,7))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(8,9,10,11,12,13,14))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(15,16,17,18,19,20,21))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(22,23,24,25,26,27,28))
        print('{:>3}{:>3}{:>3}'.format(29,30,31))
    if mesiac == 3 and prvyDen == 'Utorok':
        print('Kalendar pre Marec', rok)
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format('po','ut','st','st','pi','so','ne'))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format('',1,2,3,4,5,6))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(7,8,9,10,11,12,13))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(14,15,16,17,18,19,20))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(21,22,23,24,25,26,27))
        print('{:>3}{:>3}{:>3}{:>3}'.format(28,29,30,31))
    if mesiac == 3 and prvyDen== 'Streda':
        print('Kalendar pre Marec', rok)
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format('po','ut','st','st','pi','so','ne'))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format('','',1,2,3,4,5))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(6,7, 8,9,10,11,12))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(13,14,15,16,17,18,19))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(20,21,22,23,24,25,26))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}'.format(27,28,29,30,31))
    if mesiac == 3 and prvyDen== 'Stvrtok':
        print('Kalendar pre Marec', rok)
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format('po','ut','st','st','pi','so','ne'))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format('','','', 1,2,3,4))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(5,6,7, 8,9,10,11))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(12,13,14,15,16,17,18))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(19,20,21,22,23,24,25))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(26, 27,28,29,30,31))
    if mesiac == 3 and prvyDen== 'Piatok':
        print('Kalendar pre Marec', rok)
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format('po','ut','st','st','pi','so','ne'))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format('','','', '',1,2,3))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(4,5,6,7, 8,9,10))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(11,12,13,14,15,16,17))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(18,19,20,21,22,23,24))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(25,26, 27,28,29,30,31))
    if mesiac == 3 and prvyDen== 'Sobota':
        print('Kalendar pre Marec', rok)
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format('po','ut','st','st','pi','so','ne'))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format('','','', '','', 1,2))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(3, 4,5,6,7, 8,9))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(10, 11,12,13,14,15,16))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(17,18,19,20,21,22,23))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(24,25,26, 27,28,29,30))
        print('{:>3}'.format(31))
    if mesiac == 3 and prvyDen== 'Nedela':
        print('Kalendar pre Marec', rok)
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format('po','ut','st','st','pi','so','ne'))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format('','','', '','','', 1))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(2,3, 4,5,6,7, 8))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(9,10, 11,12,13,14,15))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(16,17,18,19,20,21,22))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(23,24,25,26, 27,28,29))
        print('{:>3}{:>3}'.format(30,31))

    if mesiac == 5 and prvyDen== 'Pondelok':
        print('Kalendar pre Maj', rok)
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format('po','ut','st','st','pi','so','ne'))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(1,2,3,4,5,6,7))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(8,9,10,11,12,13,14))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(15,16,17,18,19,20,21))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(22,23,24,25,26,27,28))
        print('{:>3}{:>3}{:>3}'.format(29,30,31))
    if mesiac == 5 and prvyDen == 'Utorok':
        print('Kalendar pre Maj', rok)
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format('po','ut','st','st','pi','so','ne'))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format('',1,2,3,4,5,6))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(7,8,9,10,11,12,13))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(14,15,16,17,18,19,20))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(21,22,23,24,25,26,27))
        print('{:>3}{:>3}{:>3}{:>3}'.format(28,29,30,31))
    if mesiac == 5 and prvyDen== 'Streda':
        print('Kalendar pre Maj', rok)
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format('po','ut','st','st','pi','so','ne'))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format('','',1,2,3,4,5))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(6,7, 8,9,10,11,12))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(13,14,15,16,17,18,19))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(20,21,22,23,24,25,26))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}'.format(27,28,29,30,31))
    if mesiac == 5 and prvyDen== 'Stvrtok':
        print('Kalendar pre Maj', rok)
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format('po','ut','st','st','pi','so','ne'))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format('','','', 1,2,3,4))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(5,6,7, 8,9,10,11))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(12,13,14,15,16,17,18))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(19,20,21,22,23,24,25))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(26, 27,28,29,30,31))
    if mesiac == 5 and prvyDen== 'Piatok':
        print('Kalendar pre Maj', rok)
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format('po','ut','st','st','pi','so','ne'))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format('','','', '',1,2,3))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(4,5,6,7, 8,9,10))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(11,12,13,14,15,16,17))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(18,19,20,21,22,23,24))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(25,26, 27,28,29,30,31))
    if mesiac == 5 and prvyDen== 'Sobota':
        print('Kalendar pre Maj', rok)
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format('po','ut','st','st','pi','so','ne'))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format('','','', '','', 1,2))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(3, 4,5,6,7, 8,9))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(10, 11,12,13,14,15,16))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(17,18,19,20,21,22,23))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(24,25,26, 27,28,29,30))
        print('{:>3}'.format(31))
    if mesiac == 5 and prvyDen== 'Nedela':
        print('Kalendar pre Maj', rok)
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format('po','ut','st','st','pi','so','ne'))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format('','','', '','','', 1))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(2,3, 4,5,6,7, 8))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(9,10, 11,12,13,14,15))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(16,17,18,19,20,21,22))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(23,24,25,26, 27,28,29))
        print('{:>3}{:>3}'.format(30,31))

    if mesiac == 7 and prvyDen== 'Pondelok':
        print('Kalendar pre Jul', rok)
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format('po','ut','st','st','pi','so','ne'))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(1,2,3,4,5,6,7))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(8,9,10,11,12,13,14))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(15,16,17,18,19,20,21))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(22,23,24,25,26,27,28))
        print('{:>3}{:>3}{:>3}'.format(29,30,31))
    if mesiac == 7 and prvyDen == 'Utorok':
        print('Kalendar pre Jul', rok)
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format('po','ut','st','st','pi','so','ne'))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format('',1,2,3,4,5,6))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(7,8,9,10,11,12,13))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(14,15,16,17,18,19,20))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(21,22,23,24,25,26,27))
        print('{:>3}{:>3}{:>3}{:>3}'.format(28,29,30,31))
    if mesiac == 7 and prvyDen== 'Streda':
        print('Kalendar pre Jul', rok)
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format('po','ut','st','st','pi','so','ne'))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format('','',1,2,3,4,5))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(6,7, 8,9,10,11,12))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(13,14,15,16,17,18,19))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(20,21,22,23,24,25,26))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}'.format(27,28,29,30,31))
    if mesiac == 7 and prvyDen== 'Stvrtok':
        print('Kalendar pre Jul', rok)
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format('po','ut','st','st','pi','so','ne'))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format('','','', 1,2,3,4))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(5,6,7, 8,9,10,11))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(12,13,14,15,16,17,18))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(19,20,21,22,23,24,25))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(26, 27,28,29,30,31))
    if mesiac == 7 and prvyDen== 'Piatok':
        print('Kalendar pre Jul', rok)
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format('po','ut','st','st','pi','so','ne'))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format('','','', '',1,2,3))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(4,5,6,7, 8,9,10))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(11,12,13,14,15,16,17))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(18,19,20,21,22,23,24))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(25,26, 27,28,29,30,31))
    if mesiac == 7 and prvyDen== 'Sobota':
        print('Kalendar pre Jul', rok)
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format('po','ut','st','st','pi','so','ne'))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format('','','', '','', 1,2))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(3, 4,5,6,7, 8,9))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(10, 11,12,13,14,15,16))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(17,18,19,20,21,22,23))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(24,25,26, 27,28,29,30))
        print('{:>3}'.format(31))
    if mesiac == 7 and prvyDen== 'Nedela':
        print('Kalendar pre Jul', rok)
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format('po','ut','st','st','pi','so','ne'))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format('','','', '','','', 1))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(2,3, 4,5,6,7, 8))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(9,10, 11,12,13,14,15))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(16,17,18,19,20,21,22))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(23,24,25,26, 27,28,29))
        print('{:>3}{:>3}'.format(30,31))

    if mesiac == 8 and prvyDen== 'Pondelok':
        print('Kalendar pre August', rok)
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format('po','ut','st','st','pi','so','ne'))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(1,2,3,4,5,6,7))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(8,9,10,11,12,13,14))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(15,16,17,18,19,20,21))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(22,23,24,25,26,27,28))
        print('{:>3}{:>3}{:>3}'.format(29,30,31))
    if mesiac == 8 and prvyDen == 'Utorok':
        print('Kalendar pre August', rok)
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format('po','ut','st','st','pi','so','ne'))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format('',1,2,3,4,5,6))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(7,8,9,10,11,12,13))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(14,15,16,17,18,19,20))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(21,22,23,24,25,26,27))
        print('{:>3}{:>3}{:>3}{:>3}'.format(28,29,30,31))
    if mesiac == 8 and prvyDen== 'Streda':
        print('Kalendar pre August', rok)
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format('po','ut','st','st','pi','so','ne'))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format('','',1,2,3,4,5))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(6,7, 8,9,10,11,12))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(13,14,15,16,17,18,19))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(20,21,22,23,24,25,26))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}'.format(27,28,29,30,31))
    if mesiac == 8 and prvyDen== 'Stvrtok':
        print('Kalendar pre August', rok)
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format('po','ut','st','st','pi','so','ne'))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format('','','', 1,2,3,4))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(5,6,7, 8,9,10,11))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(12,13,14,15,16,17,18))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(19,20,21,22,23,24,25))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(26, 27,28,29,30,31))
    if mesiac == 8 and prvyDen== 'Piatok':
        print('Kalendar pre August', rok)
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format('po','ut','st','st','pi','so','ne'))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format('','','', '',1,2,3))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(4,5,6,7, 8,9,10))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(11,12,13,14,15,16,17))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(18,19,20,21,22,23,24))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(25,26, 27,28,29,30,31))
    if mesiac == 8 and prvyDen== 'Sobota':
        print('Kalendar pre August', rok)
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format('po','ut','st','st','pi','so','ne'))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format('','','', '','', 1,2))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(3, 4,5,6,7, 8,9))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(10, 11,12,13,14,15,16))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(17,18,19,20,21,22,23))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(24,25,26, 27,28,29,30))
        print('{:>3}'.format(31))
    if mesiac == 8 and prvyDen== 'Nedela':
        print('Kalendar pre August', rok)
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format('po','ut','st','st','pi','so','ne'))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format('','','', '','','', 1))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(2,3, 4,5,6,7, 8))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(9,10, 11,12,13,14,15))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(16,17,18,19,20,21,22))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(23,24,25,26, 27,28,29))
        print('{:>3}{:>3}'.format(30,31))

    if mesiac == 10 and prvyDen== 'Pondelok':
        print('Kalendar pre Oktober', rok)
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format('po','ut','st','st','pi','so','ne'))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(1,2,3,4,5,6,7))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(8,9,10,11,12,13,14))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(15,16,17,18,19,20,21))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(22,23,24,25,26,27,28))
        print('{:>3}{:>3}{:>3}'.format(29,30,31))
    if mesiac == 10 and prvyDen == 'Utorok':
        print('Kalendar pre Oktober', rok)
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format('po','ut','st','st','pi','so','ne'))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format('',1,2,3,4,5,6))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(7,8,9,10,11,12,13))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(14,15,16,17,18,19,20))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(21,22,23,24,25,26,27))
        print('{:>3}{:>3}{:>3}{:>3}'.format(28,29,30,31))
    if mesiac == 10 and prvyDen== 'Streda':
        print('Kalendar pre Oktober', rok)
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format('po','ut','st','st','pi','so','ne'))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format('','',1,2,3,4,5))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(6,7, 8,9,10,11,12))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(13,14,15,16,17,18,19))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(20,21,22,23,24,25,26))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}'.format(27,28,29,30,31))
    if mesiac == 10 and prvyDen== 'Stvrtok':
        print('Kalendar pre Oktober', rok)
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format('po','ut','st','st','pi','so','ne'))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format('','','', 1,2,3,4))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(5,6,7, 8,9,10,11))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(12,13,14,15,16,17,18))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(19,20,21,22,23,24,25))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(26, 27,28,29,30,31))
    if mesiac == 10 and prvyDen== 'Piatok':
        print('Kalendar pre Oktober', rok)
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format('po','ut','st','st','pi','so','ne'))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format('','','', '',1,2,3))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(4,5,6,7, 8,9,10))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(11,12,13,14,15,16,17))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(18,19,20,21,22,23,24))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(25,26, 27,28,29,30,31))
    if mesiac == 10 and prvyDen== 'Sobota':
        print('Kalendar pre Oktober', rok)
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format('po','ut','st','st','pi','so','ne'))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format('','','', '','', 1,2))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(3, 4,5,6,7, 8,9))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(10, 11,12,13,14,15,16))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(17,18,19,20,21,22,23))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(24,25,26, 27,28,29,30))
        print('{:>3}'.format(31))
    if mesiac == 10 and prvyDen== 'Nedela':
        print('Kalendar pre Oktober', rok)
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format('po','ut','st','st','pi','so','ne'))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format('','','', '','','', 1))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(2,3, 4,5,6,7, 8))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(9,10, 11,12,13,14,15))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(16,17,18,19,20,21,22))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(23,24,25,26, 27,28,29))
        print('{:>3}{:>3}'.format(30,31))

    if mesiac == 12 and prvyDen== 'Pondelok':
        print('Kalendar pre December', rok)
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format('po','ut','st','st','pi','so','ne'))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(1,2,3,4,5,6,7))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(8,9,10,11,12,13,14))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(15,16,17,18,19,20,21))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(22,23,24,25,26,27,28))
        print('{:>3}{:>3}{:>3}'.format(29,30,31))
    if mesiac == 12 and prvyDen == 'Utorok':
        print('Kalendar pre December', rok)
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format('po','ut','st','st','pi','so','ne'))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format('',1,2,3,4,5,6))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(7,8,9,10,11,12,13))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(14,15,16,17,18,19,20))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(21,22,23,24,25,26,27))
        print('{:>3}{:>3}{:>3}{:>3}'.format(28,29,30,31))
    if mesiac == 12 and prvyDen== 'Streda':
        print('Kalendar pre December', rok)
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format('po','ut','st','st','pi','so','ne'))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format('','',1,2,3,4,5))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(6,7, 8,9,10,11,12))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(13,14,15,16,17,18,19))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(20,21,22,23,24,25,26))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}'.format(27,28,29,30,31))
    if mesiac == 12 and prvyDen== 'Stvrtok':
        print('Kalendar pre December', rok)
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format('po','ut','st','st','pi','so','ne'))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format('','','', 1,2,3,4))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(5,6,7, 8,9,10,11))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(12,13,14,15,16,17,18))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(19,20,21,22,23,24,25))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(26, 27,28,29,30,31))
    if mesiac == 12 and prvyDen== 'Piatok':
        print('Kalendar pre December', rok)
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format('po','ut','st','st','pi','so','ne'))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format('','','', '',1,2,3))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(4,5,6,7, 8,9,10))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(11,12,13,14,15,16,17))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(18,19,20,21,22,23,24))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(25,26, 27,28,29,30,31))
    if mesiac == 12 and prvyDen== 'Sobota':
        print('Kalendar pre December', rok)
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format('po','ut','st','st','pi','so','ne'))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format('','','', '','', 1,2))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(3, 4,5,6,7, 8,9))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(10, 11,12,13,14,15,16))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(17,18,19,20,21,22,23))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(24,25,26, 27,28,29,30))
        print('{:>3}'.format(31))
    if mesiac == 12 and prvyDen== 'Nedela':
        print('Kalendar pre December', rok)
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format('po','ut','st','st','pi','so','ne'))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format('','','', '','','', 1))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(2,3, 4,5,6,7, 8))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(9,10, 11,12,13,14,15))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(16,17,18,19,20,21,22))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(23,24,25,26, 27,28,29))
        print('{:>3}{:>3}'.format(30,31))

    if mesiac == 4 and prvyDen == 'Pondelok':
        print('Kalendar pre April', rok)
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format('po','ut','st','st','pi','so','ne'))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(1,2,3,4,5,6,7))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(8,9,10,11,12,13,14))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(15,16,17,18,19,20,21))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(22,23,24,25,26,27,28))
        print('{:>3}{:>3}'.format(29,30))
    if mesiac == 4 and prvyDen == 'Utorok':
        print('Kalendar pre April', rok)
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format('po','ut','st','st','pi','so','ne'))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format('',1,2,3,4,5,6))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(7,8,9,10,11,12,13))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(14,15,16,17,18,19,20))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(21,22,23,24,25,26,27))
        print('{:>3}{:>3}{:>3}'.format(28,29,30))
    if mesiac == 4 and prvyDen == 'Streda':
        print('Kalendar pre April', rok)
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format('po','ut','st','st','pi','so','ne'))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format('','', 1,2,3,4,5))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(6,7,8,9,10,11,12))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(13,14,15,16,17,18,19))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(20,21,22,23,24,25,26))
        print('{:>3}{:>3}{:>3}{:>3}'.format(27,28,29,30))
    if mesiac == 4 and prvyDen == 'Stvrtok':
        print('Kalendar pre April', rok)
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format('po','ut','st','st','pi','so','ne'))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format('','','',1,2,3,4))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(5,6,7,8,9,10,11))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(12,13,14,15,16,17,18))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(19,20,21,22,23,24,25))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}'.format(26, 27,28,29,30))
    if mesiac == 4 and prvyDen == 'Piatok':
        print('Kalendar pre April', rok)
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format('po','ut','st','st','pi','so','ne'))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format('','','','',1,2,3))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(4,5,6,7,8,9,10))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(11,12,13,14,15,16,17))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(18,19,20,21,22,23,24))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(25, 26, 27,28,29,30))
    if mesiac == 4 and prvyDen == 'Sobota':
        print('Kalendar pre April', rok)
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format('po','ut','st','st','pi','so','ne'))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format('','','','','',1,2))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(3,4,5,6,7,8,9))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(10,11,12,13,14,15,16))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(17,18,19,20,21,22,23))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(24,25, 26, 27,28,29,30))
    if mesiac == 4 and prvyDen == 'Nedela':
        print('Kalendar pre April', rok)
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format('po','ut','st','st','pi','so','ne'))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format('','','','','','',1))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(2,3,4,5,6,7,8))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(9, 10,11,12,13,14,15))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(16,17,18,19,20,21,22))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(23,24,25, 26, 27,28,29))
        print('[:>3}'.format(30))

    if mesiac == 6 and prvyDen == 'Pondelok':
        print('Kalendar pre Jun', rok)
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format('po','ut','st','st','pi','so','ne'))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(1,2,3,4,5,6,7))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(8,9,10,11,12,13,14))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(15,16,17,18,19,20,21))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(22,23,24,25,26,27,28))
        print('{:>3}{:>3}'.format(29,30))
    if mesiac == 6 and prvyDen == 'Utorok':
        print('Kalendar pre Jun', rok)
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format('po','ut','st','st','pi','so','ne'))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format('',1,2,3,4,5,6))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(7,8,9,10,11,12,13))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(14,15,16,17,18,19,20))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(21,22,23,24,25,26,27))
        print('{:>3}{:>3}{:>3}'.format(28,29,30))
    if mesiac == 6 and prvyDen == 'Streda':
        print('Kalendar pre Jun', rok)
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format('po','ut','st','st','pi','so','ne'))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format('','', 1,2,3,4,5))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(6,7,8,9,10,11,12))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(13,14,15,16,17,18,19))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(20,21,22,23,24,25,26))
        print('{:>3}{:>3}{:>3}{:>3}'.format(27,28,29,30))
    if mesiac == 6 and prvyDen == 'Stvrtok':
        print('Kalendar pre Jun', rok)
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format('po','ut','st','st','pi','so','ne'))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format('','','',1,2,3,4))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(5,6,7,8,9,10,11))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(12,13,14,15,16,17,18))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(19,20,21,22,23,24,25))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}'.format(26, 27,28,29,30))
    if mesiac == 6 and prvyDen == 'Piatok':
        print('Kalendar pre Jun', rok)
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format('po','ut','st','st','pi','so','ne'))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format('','','','',1,2,3))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(4,5,6,7,8,9,10))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(11,12,13,14,15,16,17))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(18,19,20,21,22,23,24))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(25, 26, 27,28,29,30))
    if mesiac == 6 and prvyDen == 'Sobota':
        print('Kalendar pre Jun', rok)
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format('po','ut','st','st','pi','so','ne'))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format('','','','','',1,2))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(3,4,5,6,7,8,9))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(10,11,12,13,14,15,16))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(17,18,19,20,21,22,23))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(24,25, 26, 27,28,29,30))
    if mesiac == 6 and prvyDen == 'Nedela':
        print('Kalendar pre Jun', rok)
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format('po','ut','st','st','pi','so','ne'))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format('','','','','','',1))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(2,3,4,5,6,7,8))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(9, 10,11,12,13,14,15))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(16,17,18,19,20,21,22))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(23,24,25, 26, 27,28,29))
        print('[:>3}'.format(30))

    if mesiac == 9 and prvyDen == 'Pondelok':
        print('Kalendar pre September', rok)
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format('po','ut','st','st','pi','so','ne'))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(1,2,3,4,5,6,7))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(8,9,10,11,12,13,14))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(15,16,17,18,19,20,21))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(22,23,24,25,26,27,28))
        print('{:>3}{:>3}'.format(29,30))
    if mesiac == 9 and prvyDen == 'Utorok':
        print('Kalendar pre September', rok)
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format('po','ut','st','st','pi','so','ne'))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format('',1,2,3,4,5,6))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(7,8,9,10,11,12,13))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(14,15,16,17,18,19,20))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(21,22,23,24,25,26,27))
        print('{:>3}{:>3}{:>3}'.format(28,29,30))
    if mesiac == 9 and prvyDen == 'Streda':
        print('Kalendar pre September', rok)
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format('po','ut','st','st','pi','so','ne'))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format('','', 1,2,3,4,5))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(6,7,8,9,10,11,12))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(13,14,15,16,17,18,19))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(20,21,22,23,24,25,26))
        print('{:>3}{:>3}{:>3}{:>3}'.format(27,28,29,30))
    if mesiac == 9 and prvyDen == 'Stvrtok':
        print('Kalendar pre September', rok)
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format('po','ut','st','st','pi','so','ne'))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format('','','',1,2,3,4))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(5,6,7,8,9,10,11))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(12,13,14,15,16,17,18))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(19,20,21,22,23,24,25))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}'.format(26, 27,28,29,30))
    if mesiac == 9 and prvyDen == 'Piatok':
        print('Kalendar pre September', rok)
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format('po','ut','st','st','pi','so','ne'))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format('','','','',1,2,3))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(4,5,6,7,8,9,10))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(11,12,13,14,15,16,17))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(18,19,20,21,22,23,24))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(25, 26, 27,28,29,30))
    if mesiac == 9 and prvyDen == 'Sobota':
        print('Kalendar pre September', rok)
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format('po','ut','st','st','pi','so','ne'))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format('','','','','',1,2))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(3,4,5,6,7,8,9))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(10,11,12,13,14,15,16))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(17,18,19,20,21,22,23))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(24,25, 26, 27,28,29,30))
    if mesiac == 9 and prvyDen == 'Nedela':
        print('Kalendar pre September', rok)
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format('po','ut','st','st','pi','so','ne'))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format('','','','','','',1))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(2,3,4,5,6,7,8))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(9, 10,11,12,13,14,15))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(16,17,18,19,20,21,22))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(23,24,25, 26, 27,28,29))
        print('[:>3}'.format(30))

    if mesiac == 11 and prvyDen == 'Pondelok':
        print('Kalendar pre November', rok)
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format('po','ut','st','st','pi','so','ne'))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(1,2,3,4,5,6,7))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(8,9,10,11,12,13,14))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(15,16,17,18,19,20,21))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(22,23,24,25,26,27,28))
        print('{:>3}{:>3}'.format(29,30))
    if mesiac == 11 and prvyDen == 'Utorok':
        print('Kalendar pre November', rok)
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format('po','ut','st','st','pi','so','ne'))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format('',1,2,3,4,5,6))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(7,8,9,10,11,12,13))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(14,15,16,17,18,19,20))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(21,22,23,24,25,26,27))
        print('{:>3}{:>3}{:>3}'.format(28,29,30))
    if mesiac == 11 and prvyDen == 'Streda':
        print('Kalendar pre November', rok)
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format('po','ut','st','st','pi','so','ne'))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format('','', 1,2,3,4,5))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(6,7,8,9,10,11,12))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(13,14,15,16,17,18,19))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(20,21,22,23,24,25,26))
        print('{:>3}{:>3}{:>3}{:>3}'.format(27,28,29,30))
    if mesiac == 11 and prvyDen == 'Stvrtok':
        print('Kalendar pre November', rok)
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format('po','ut','st','st','pi','so','ne'))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format('','','',1,2,3,4))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(5,6,7,8,9,10,11))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(12,13,14,15,16,17,18))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(19,20,21,22,23,24,25))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}'.format(26, 27,28,29,30))
    if mesiac == 11 and prvyDen == 'Piatok':
        print('Kalendar pre November', rok)
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format('po','ut','st','st','pi','so','ne'))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format('','','','',1,2,3))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(4,5,6,7,8,9,10))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(11,12,13,14,15,16,17))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(18,19,20,21,22,23,24))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(25, 26, 27,28,29,30))
    if mesiac == 11 and prvyDen == 'Sobota':
        print('Kalendar pre November', rok)
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format('po','ut','st','st','pi','so','ne'))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format('','','','','',1,2))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(3,4,5,6,7,8,9))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(10,11,12,13,14,15,16))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(17,18,19,20,21,22,23))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(24,25, 26, 27,28,29,30))
    if mesiac == 11 and prvyDen == 'Nedela':
        print('Kalendar pre November', rok)
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format('po','ut','st','st','pi','so','ne'))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format('','','','','','',1))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(2,3,4,5,6,7,8))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(9, 10,11,12,13,14,15))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(16,17,18,19,20,21,22))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(23,24,25, 26, 27,28,29))
        print('[:>3}'.format(30))

    if mesiac == 2 and prvyDen == 'Pondelok' and rok in (1904,1908,1912,1916,1920,1924,1928,1932,1936,1940,1944,1948,1952,1956,1960,1964,1968,1972,1976,1980,1984,1988,1992,1996,2000,2004,2008,2012,2016,2020,2024,2028,2032,2036,2040,2044,2048,2052,2056,2060,2064,2068,2072,2076,2080,2084,2088,2092,2096,2100):
        print('Kalendar pre Februar', rok)
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format('po','ut','st','st','pi','so','ne'))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(1,2,3,4,5,6,7))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(8,9,10,11,12,13,14))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(15,16,17,18,19,20,21))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(22,23,24,25,26,27,28))
        print('{:>3}'.format(29))
    if mesiac == 2 and prvyDen == 'Utorok' and rok in (1904,1908,1912,1916,1920,1924,1928,1932,1936,1940,1944,1948,1952,1956,1960,1964,1968,1972,1976,1980,1984,1988,1992,1996,2000,2004,2008,2012,2016,2020,2024,2028,2032,2036,2040,2044,2048,2052,2056,2060,2064,2068,2072,2076,2080,2084,2088,2092,2096,2100):
        print('Kalendar pre Februar', rok)
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format('po','ut','st','st','pi','so','ne'))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format('',1,2,3,4,5,6))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(7,8,9,10,11,12,13))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(14,15,16,17,18,19,20))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(21,22,23,24,25,26,27))
        print('{:>3}{:>3}'.format(28,29))
    if mesiac == 2 and prvyDen == 'Streda' and rok in (1904,1908,1912,1916,1920,1924,1928,1932,1936,1940,1944,1948,1952,1956,1960,1964,1968,1972,1976,1980,1984,1988,1992,1996,2000,2004,2008,2012,2016,2020,2024,2028,2032,2036,2040,2044,2048,2052,2056,2060,2064,2068,2072,2076,2080,2084,2088,2092,2096,2100):
        print('Kalendar pre Februar', rok)
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format('po','ut','st','st','pi','so','ne'))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format('','', 1,2,3,4,5))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(6,7,8,9,10,11,12))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(13,14,15,16,17,18,19))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(20,21,22,23,24,25,26))
        print('{:>3}{:>3}{:>3}'.format(27,28,29))
    if mesiac == 2 and prvyDen == 'Stvrtok' and rok in (1904,1908,1912,1916,1920,1924,1928,1932,1936,1940,1944,1948,1952,1956,1960,1964,1968,1972,1976,1980,1984,1988,1992,1996,2000,2004,2008,2012,2016,2020,2024,2028,2032,2036,2040,2044,2048,2052,2056,2060,2064,2068,2072,2076,2080,2084,2088,2092,2096,2100):
        print('Kalendar pre Februar', rok)
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format('po','ut','st','st','pi','so','ne'))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format('','','',1,2,3,4))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(5,6,7,8,9,10,11))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(12,13,14,15,16,17,18))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(19,20,21,22,23,24,25))
        print('{:>3}{:>3}{:>3}{:>3}'.format(26, 27,28,29))
    if mesiac == 2 and prvyDen == 'Piatok' and rok in (1904,1908,1912,1916,1920,1924,1928,1932,1936,1940,1944,1948,1952,1956,1960,1964,1968,1972,1976,1980,1984,1988,1992,1996,2000,2004,2008,2012,2016,2020,2024,2028,2032,2036,2040,2044,2048,2052,2056,2060,2064,2068,2072,2076,2080,2084,2088,2092,2096,2100):
        print('Kalendar pre Februar', rok)
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format('po','ut','st','st','pi','so','ne'))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format('','','','',1,2,3))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(4,5,6,7,8,9,10))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(11,12,13,14,15,16,17))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(18,19,20,21,22,23,24))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}'.format(25, 26, 27,28,29))
    if mesiac == 2 and prvyDen == 'Sobota' and rok in (1904,1908,1912,1916,1920,1924,1928,1932,1936,1940,1944,1948,1952,1956,1960,1964,1968,1972,1976,1980,1984,1988,1992,1996,2000,2004,2008,2012,2016,2020,2024,2028,2032,2036,2040,2044,2048,2052,2056,2060,2064,2068,2072,2076,2080,2084,2088,2092,2096,2100):
        print('Kalendar pre Februar', rok)
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format('po','ut','st','st','pi','so','ne'))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format('','','','','',1,2))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(3,4,5,6,7,8,9))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(10,11,12,13,14,15,16))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(17,18,19,20,21,22,23))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(24,25, 26, 27,28,29))
    if mesiac == 2 and prvyDen == 'Nedela' and rok in (1904,1908,1912,1916,1920,1924,1928,1932,1936,1940,1944,1948,1952,1956,1960,1964,1968,1972,1976,1980,1984,1988,1992,1996,2000,2004,2008,2012,2016,2020,2024,2028,2032,2036,2040,2044,2048,2052,2056,2060,2064,2068,2072,2076,2080,2084,2088,2092,2096,2100):
        print('Kalendar pre Februar', rok)
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format('po','ut','st','st','pi','so','ne'))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format('','','','','','',1))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(2,3,4,5,6,7,8))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(9, 10,11,12,13,14,15))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(16,17,18,19,20,21,22))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(23,24,25, 26, 27,28,29))
    
    if mesiac == 2 and prvyDen == 'Pondelok' and rok not in (1904,1908,1912,1916,1920,1924,1928,1932,1936,1940,1944,1948,1952,1956,1960,1964,1968,1972,1976,1980,1984,1988,1992,1996,2000,2004,2008,2012,2016,2020,2024,2028,2032,2036,2040,2044,2048,2052,2056,2060,2064,2068,2072,2076,2080,2084,2088,2092,2096,2100):
        print('Kalendar pre Februar', rok)
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format('po','ut','st','st','pi','so','ne'))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(1,2,3,4,5,6,7))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(8,9,10,11,12,13,14))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(15,16,17,18,19,20,21))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(22,23,24,25,26,27,28))
    if mesiac == 2 and prvyDen == 'Utorok' and rok not in (1904,1908,1912,1916,1920,1924,1928,1932,1936,1940,1944,1948,1952,1956,1960,1964,1968,1972,1976,1980,1984,1988,1992,1996,2000,2004,2008,2012,2016,2020,2024,2028,2032,2036,2040,2044,2048,2052,2056,2060,2064,2068,2072,2076,2080,2084,2088,2092,2096,2100):
        print('Kalendar pre Februar', rok)
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format('po','ut','st','st','pi','so','ne'))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format('',1,2,3,4,5,6))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(7,8,9,10,11,12,13))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(14,15,16,17,18,19,20))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(21,22,23,24,25,26,27))
        print('{:>3}'.format(28))
    if mesiac == 2 and prvyDen == 'Streda' and rok not in (1904,1908,1912,1916,1920,1924,1928,1932,1936,1940,1944,1948,1952,1956,1960,1964,1968,1972,1976,1980,1984,1988,1992,1996,2000,2004,2008,2012,2016,2020,2024,2028,2032,2036,2040,2044,2048,2052,2056,2060,2064,2068,2072,2076,2080,2084,2088,2092,2096,2100):
        print('Kalendar pre Februar', rok)
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format('po','ut','st','st','pi','so','ne'))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format('','', 1,2,3,4,5))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(6,7,8,9,10,11,12))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(13,14,15,16,17,18,19))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(20,21,22,23,24,25,26))
        print('{:>3}{:>3}'.format(27,28))
    if mesiac == 2 and prvyDen == 'Stvrtok' and rok not in (1904,1908,1912,1916,1920,1924,1928,1932,1936,1940,1944,1948,1952,1956,1960,1964,1968,1972,1976,1980,1984,1988,1992,1996,2000,2004,2008,2012,2016,2020,2024,2028,2032,2036,2040,2044,2048,2052,2056,2060,2064,2068,2072,2076,2080,2084,2088,2092,2096,2100):
        print('Kalendar pre Februar', rok)
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format('po','ut','st','st','pi','so','ne'))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format('','','',1,2,3,4))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(5,6,7,8,9,10,11))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(12,13,14,15,16,17,18))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(19,20,21,22,23,24,25))
        print('{:>3}{:>3}{:>3}'.format(26, 27,28))
    if mesiac == 2 and prvyDen == 'Piatok' and rok not in (1904,1908,1912,1916,1920,1924,1928,1932,1936,1940,1944,1948,1952,1956,1960,1964,1968,1972,1976,1980,1984,1988,1992,1996,2000,2004,2008,2012,2016,2020,2024,2028,2032,2036,2040,2044,2048,2052,2056,2060,2064,2068,2072,2076,2080,2084,2088,2092,2096,2100):
        print('Kalendar pre Februar', rok)
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format('po','ut','st','st','pi','so','ne'))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format('','','','',1,2,3))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(4,5,6,7,8,9,10))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(11,12,13,14,15,16,17))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(18,19,20,21,22,23,24))
        print('{:>3}{:>3}{:>3}{:>3}'.format(25, 26, 27,28))
    if mesiac == 2 and prvyDen == 'Sobota' and rok not in (1904,1908,1912,1916,1920,1924,1928,1932,1936,1940,1944,1948,1952,1956,1960,1964,1968,1972,1976,1980,1984,1988,1992,1996,2000,2004,2008,2012,2016,2020,2024,2028,2032,2036,2040,2044,2048,2052,2056,2060,2064,2068,2072,2076,2080,2084,2088,2092,2096,2100):
        print('Kalendar pre Februar', rok)
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format('po','ut','st','st','pi','so','ne'))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format('','','','','',1,2))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(3,4,5,6,7,8,9))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(10,11,12,13,14,15,16))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(17,18,19,20,21,22,23))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}'.format(24,25, 26, 27,28))
    if mesiac == 2 and prvyDen == 'Nedela' and rok not in (1904,1908,1912,1916,1920,1924,1928,1932,1936,1940,1944,1948,1952,1956,1960,1964,1968,1972,1976,1980,1984,1988,1992,1996,2000,2004,2008,2012,2016,2020,2024,2028,2032,2036,2040,2044,2048,2052,2056,2060,2064,2068,2072,2076,2080,2084,2088,2092,2096,2100):
        print('Kalendar pre Februar', rok)
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format('po','ut','st','st','pi','so','ne'))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format('','','','','','',1))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(2,3,4,5,6,7,8))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(9, 10,11,12,13,14,15))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(16,17,18,19,20,21,22))
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(23,24,25, 26, 27,28))
