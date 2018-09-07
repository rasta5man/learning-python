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







# spusiaca funkcia 
def kalendar(den, mesiac, rok, inyDen, inyMesiac, inyRok):
    dobryDatum(den, mesiac, rok, inyDen, inyMesiac, inyRok)
    menoDna1(den, mesiac, rok, inyDen, inyMesiac, inyRok)
    menoDna2(den, mesiac, rok, inyDen, inyMesiac, inyRok)
    print('Pocet dni od 1.1.1901 po ', den,'.',mesiac,'.',rok,' = ', pocetDni1(den, mesiac, rok, inyDen, inyMesiac, inyRok))
    print('Pocet dni od 1.1.1901 po ', inyDen,'.',inyMesiac,'.',inyRok,' = ', pocetDni2(den, mesiac, rok, inyDen, inyMesiac, inyRok))
    pocet = abs(pocetDni1(den, mesiac, rok, inyDen, inyMesiac, inyRok) - pocetDni2(den, mesiac, rok, inyDen, inyMesiac, inyRok))
    print('Pocet dni od', den,'.',mesiac,'.',rok,' po', inyDen,'.',inyMesiac,'.',inyRok,' = ', pocet)
    menoMesiaca(den, mesiac, rok, inyDen, inyMesiac, inyRok)
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
        pocetDni = 365*(rok - 1901) + den + pridaj1
    elif mesiac == 2:
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
        inyPocetDni = 365*(inyRok - 1901) + inyDen + pridaj2
    elif inyMesiac == 2:
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





def pocetDnivMesiaci(den, mesiac, rok, inyDen, inyMesiac, inyRok):
    if mesiac == 1 or mesiac == 3 or mesiac==5 or mesiac ==7 or mesiac == 8 or mesiac == 10 or mesiac == 12:
        return 31
    if mesiac == 4 or mesiac == 6 or mesiac == 9 or mesiac == 11:
        return 30
    if mesiac == 2 and rok%4 != 0:
        return 28
    if mesiac == 2 and rok % 4 == 0:
        return 29




def menoMesiaca(den, mesiac, rok, inyDen, inyMesiac, inyRok):
    if mesiac == 1:
        print('kalendar pre januar', rok)
    elif mesiac ==2:
        print('kalendar pre februar', rok)
    elif mesiac ==3:
        print('kalendar pre marec', rok)
    elif mesiac ==4:
        print('kalendar pre april', rok)
    elif mesiac ==5:
        print('kalendar pre maj', rok)
    elif mesiac ==6:
        print('kalendar pre jun', rok)
    elif mesiac ==7:
        print('kalendar pre jul', rok)
    elif mesiac ==8:
        print('kalendar pre august', rok)
    elif mesiac ==9:
        print('kalendar pre september', rok)
    elif mesiac ==10:
        print('kalendar pre oktober', rok)
    elif mesiac ==11:
        print('kalendar pre november', rok)
    elif mesiac == 12:
        print('kalendar pre december', rok)
    else:
        print('restartujte program a zadajte spravny mesiac')




# vypocita meno dna pre zadany datum - pondelok, utorok, streda, atd ...   
def menoDna1(den, mesiac, rok, inyDen, inyMesiac, inyRok):
    pocet1 = pocetDni1(den, mesiac, rok, inyDen, inyMesiac, inyRok)
    if pocet1 in list(range(1, 73051, 7)):
        print(den,'.',mesiac,'.',rok,' = utorok ')
    elif pocet1 in list(range(2, 73051, 7)):
        print(den,'.',mesiac,'.',rok,' = streda ')
    elif pocet1 in list(range(3, 73051, 7)):
        print(den,'.',mesiac,'.',rok,' = stvrtok ')
    elif pocet1 in list(range(4, 73051, 7)):
        print(den,'.',mesiac,'.',rok,' = piatok ')
    elif pocet1 in list(range(5, 73051, 7)):
        print(den,'.',mesiac,'.',rok,' = sobota ')
    elif pocet1 in list(range(6, 73051, 7)):
        print(den,'.',mesiac,'.',rok,' = nedela ')
    elif pocet1 in list(range(7, 73051, 7)):
        print(den,'.',mesiac,'.',rok,' = pondelok ')    




# vypocita meno dna pre druhy zadany datum - pondelok, utorok, streda, atd ...  
def menoDna2(den, mesiac, rok, inyDen, inyMesiac, inyRok):
    pocet2 = pocetDni2(den, mesiac, rok, inyDen, inyMesiac, inyRok)
    if pocet2 in list(range(1, 73051, 7)):
        print(inyDen,'.',inyMesiac,'.',inyRok,' = utorok ')
    elif pocet2 in list(range(2, 73051, 7)):
        print(inyDen,'.',inyMesiac,'.',inyRok,' = streda ')
    elif pocet2 in list(range(3, 73051, 7)):
        print(inyDen,'.',inyMesiac,'.',inyRok,' = stvrtok ')
    elif pocet2 in list(range(4, 73051, 7)):
        print(inyDen,'.',inyMesiac,'.',inyRok,' = piatok ')
    elif pocet2 in list(range(5, 73051, 7)):
        print(inyDen,'.',inyMesiac,'.',inyRok,' = sobota ')
    elif pocet2 in list(range(6, 73051, 7)):
        print(inyDen,'.',inyMesiac,'.',inyRok,' = nedela ')
    elif pocet2 in list(range(7, 73051, 7)):
        print(inyDen,'.',inyMesiac,'.',inyRok,' = pondelok ')



        
#nedorobene       
def vypisKalendara(den, mesiac, rok, inyDen, inyMesiac, inyRok):
    print (' po  ut  st  st  pi  so  ne')
    prvyDenvMesiaci = 'utorok'
    poslednyDenvMesiaci = 'sobota'
    #menoDna1, menoDna2, menoDna3, menoDna4, menoDna5, menoDna6, menoDna7 = 'utorok',  'streda', 'stvrtok', 'piatok', 'sobota', 'nedela', 'pondelok'
    #for i in range (1, pocetDnivMesiaci(den, mesiac, rok, inyDen, inyMesiac, inyRok)+1):
    #    print('{:3}{:3}{:3}{:3}{:3}{:3}{:3}'.format(menoDna1,menoDna2,menoDna3, menoDna4, menoDna5, menoDna6, menoDna7))
    menoDna1, menoDna2, menoDna3, menoDna4, menoDna5, menoDna6, menoDna7 = 'utorok',  'streda', 'stvrtok', 'piatok', 'sobota', 'nedela', 'pondelok'
    if den == 1 and mesiac == 1 and rok == 1901:
        utorok = 1
        streda = 2
        stvrtok = 3
        piatok = 4
        sobota = 5
        nedela = 6
        pondelok = 7













