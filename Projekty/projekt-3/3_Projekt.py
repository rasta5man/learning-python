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

def kalendar(den, mesiac, rok, inyDen, inyMesiac, inyRok):
    dobryDatum(den, mesiac, rok, inyDen, inyMesiac, inyRok)
    menoMesiaca(den, mesiac, rok, inyDen, inyMesiac, inyRok)
    pocetDni(den, mesiac, rok, inyDen, inyMesiac, inyRok)
    pocetDnivMesiaci(den, mesiac, rok, inyDen, inyMesiac, inyRok)
    vypisKalendara(den, mesiac, rok, inyDen, inyMesiac, inyRok)
    menoDna(den, mesiac, rok, inyDen, inyMesiac, inyRok)
    
def dobryDatum(den, mesiac, rok, inyDen, inyMesiac, inyRok):
    zaciatocny = 1901
    konecny = 2100
    if rok in range(1901,2101):
        if mesiac == 1 or mesiac==3 or mesiac ==5 or mesiac ==7 or mesiac ==8 or mesiac==10 or mesiac==12:
            if den not in range(1,32):
                print ('deň je zle zadaný dátum')
            else:
                print('zadali ste datum: ', den,'.',mesiac,'.',rok)
        if mesiac == 4 or mesiac==6 or mesiac ==9 or mesiac ==11:
            if den not in range(1,30):
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
            if inyDen not in range(1,30):
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

           
def pocetDni(den, mesiac, rok, inyDen, inyMesiac, inyRok):
    zaciatocny = 1901
    konecny = 2100
    februar = 28

    pridaj = 0
    for i in range(1904, 2101, 4):
            if rok >= i:
                pridaj += 1
    """vysledok:
        1904 1908 1912 1916 1920 1924 1928 1932 1936 1940 1944 1948 1952 1956 1960
        1964 1968 1972 1976 1980 1984 1988 1992 1996 2000 2004 2008 2012 2016 2020
        2024 2028 2032 2036 2040 2044 2048 2052 2056 2060 2064 2068 2072 2076 2080 2084 2088 2092 2096 2100 
    # prestupneRoky = 1904, 1908, 1912, 1916, 1920, 1924 ... = 1901 + (1*4-1), 1901 + (2*4-1), 1901+(3*4-1), 4*4-1
    if rok-1901 == 4*x -1 
    pridaj = rok - 1901
    """
    if mesiac == 1:
        pocetDni = 365*(rok - 1901) + den + pridaj
        print('pocet dni od 1.1.1901 do ', den,'.',mesiac,'.',rok, '=', pocetDni)

    if mesiac == 2:
        pocetDni = 365*(rok - 1901) + 31 + den + pridaj
        print('pocet dni od 1.1.1901 do ', den,'.',mesiac,'.',rok, '=', pocetDni)
    if mesiac == 3:
        pocetDni = 365*(rok - 1901) + 31 + februar + den+ pridaj
        print('pocet dni od 1.1.1901 do ', den,'.',mesiac,'.',rok, '=', pocetDni) 
    
    if mesiac == 4:
        pocetDni = 365*(rok - 1901) + 31 + februar + 31 + den+ pridaj
        print('pocet dni od 1.1.1901 do ', den,'.',mesiac,'.',rok, '=', pocetDni) 
    
    if mesiac == 5:
        pocetDni = 365*(rok - 1901) + 31 + februar + 31 + 30 + den+ pridaj
        print('pocet dni od 1.1.1901 do ', den,'.',mesiac,'.',rok, '=', pocetDni) 
    
    if mesiac == 6:
        pocetDni = 365*(rok - 1901) + 31 + februar + 31 + 30 + 31 + den+ pridaj
        print('pocet dni od 1.1.1901 do ', den,'.',mesiac,'.',rok, '=', pocetDni) 
    
    if mesiac == 7:
        pocetDni = 365*(rok - 1901) + 31 + februar + 31 + 30 + 31 + 30 + den+ pridaj
        print('pocet dni od 1.1.1901 do ', den,'.',mesiac,'.',rok, '=', pocetDni) 
    
    if mesiac == 8:
        pocetDni = 365*(rok - 1901) + 31 + februar + 31 + 30 + 31 + 30 + 31 + den+ pridaj
        print('pocet dni od 1.1.1901 do ', den,'.',mesiac,'.',rok, '=', pocetDni) 
    
    if mesiac == 9:
        pocetDni = 365*(rok - 1901) + 31 + februar + 31 + 30 + 31 + 30 + 31 + 31 + den+ pridaj
        print('pocet dni od 1.1.1901 do ', den,'.',mesiac,'.',rok, '=', pocetDni) 
    if mesiac == 10:
        pocetDni = 365*(rok - 1901) + 31 + februar + 31 + 30 + 31 + 30 + 31 + 31 + 30 + den+ pridaj
        print('pocet dni od 1.1.1901 do ', den,'.',mesiac,'.',rok, '=', pocetDni) 
    if mesiac == 11:
        pocetDni = 365*(rok - 1901) + 31 + februar + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31 + den+ pridaj
        print('pocet dni od 1.1.1901 do ', den,'.',mesiac,'.',rok, '=', pocetDni) 
    
    if mesiac == 12:
        pocetDni = 365*(rok - 1901) + 31 + februar + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31 + 30 + den+ pridaj
        print('pocet dni od 1.1.1901 do ', den,'.',mesiac,'.',rok, '=', pocetDni)

   
    if inyMesiac == 1:
        inyPocetDni = 365*(inyRok - 1901) + inyDen + pridaj
        print('pocet dni od 1.1.1901 do ', inyDen,'.',inyMesiac,'.',inyRok, '=', inyPocetDni)

    

    if inyMesiac == 2:
        inyPocetDni = 365*(inyRok - 1901) + 31 + inyDen + pridaj
        print('pocet dni od 1.1.1901 do ', inyDen,'.',inyMesiac,'.',inyRok, '=', inyPocetDni)
    if inyMesiac == 3:
        inyPocetDni = 365*(inyRok - 1901) + 31 + februar + inyDen+ pridaj
        print('pocet dni od 1.1.1901 do ', inyDen,'.',inyMesiac,'.',inyRok, '=', inyPocetDni) 
    
    if inyMesiac == 4:
        inyPocetDni = 365*(inyRok - 1901) + 31 + februar + 31 + inyDen+ pridaj
        print('pocet dni od 1.1.1901 do ', inyDen,'.',inyMesiac,'.',inyRok, '=', inyPocetDni) 
    
    if inyMesiac == 5:
        inyPocetDni = 365*(inyRok - 1901) + 31 + februar + 31 + 30 + inyDen+ pridaj
        print('pocet dni od 1.1.1901 do ', inyDen,'.',inyMesiac,'.',inyRok, '=', inyPocetDni) 
    
    if inyMesiac == 6:
        inyPocetDni = 365*(inyRok - 1901) + 31 + februar + 31 + 30 + 31 + inyDen+ pridaj
        print('pocet dni od 1.1.1901 do ', inyDen,'.',inyMesiac,'.',inyRok, '=', inyPocetDni) 
    
    if inyMesiac == 7:
        inyPocetDni = 365*(inyRok - 1901) + 31 + februar + 31 + 30 + 31 + 30 + inyDen+ pridaj
        print('pocet dni od 1.1.1901 do ', inyDen,'.',inyMesiac,'.',inyRok, '=', inyPocetDni) 
    
    if inyMesiac == 8:
        inyPocetDni = 365*(inyRok - 1901) + 31 + februar + 31 + 30 + 31 + 30 + 31 + inyDen+ pridaj
        print('pocet dni od 1.1.1901 do ', inyDen,'.',inyMesiac,'.',inyRok, '=', inyPocetDni) 
    
    if inyMesiac == 9:
        inyPocetDni = 365*(inyRok - 1901) + 31 + februar + 31 + 30 + 31 + 30 + 31 + 31 + inyDen+ pridaj
        print('pocet dni od 1.1.1901 do ', inyDen,'.',inyMesiac,'.',inyRok, '=', inyPocetDni) 
    if inyMesiac == 10:
        inyPocetDni = 365*(inyRok - 1901) + 31 + februar + 31 + 30 + 31 + 30 + 31 + 31 + 30 + inyDen+ pridaj
        print('pocet dni od 1.1.1901 do ', inyDen,'.',inyMesiac,'.',inyRok, '=', inyPocetDni) 
    if inyMesiac == 11:
        inyPocetDni = 365*(inyRok - 1901) + 31 + februar + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31 + inyDen+ pridaj
        print('pocet dni od 1.1.1901 do ', inyDen,'.',inyMesiac,'.',inyRok, '=', inyPocetDni) 
    
    if inyMesiac == 12:
        inyPocetDni = 365*(inyRok - 1901) + 31 + februar + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31 + 30 + inyDen+ pridaj
        print('pocet dni od 1.1.1901 do ', inyDen,'.',inyMesiac,'.',inyRok, '=', inyPocetDni)
            
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
        
def menoDna(den, mesiac, rok, inyDen, inyMesiac, inyRok):

    menoDna1, menoDna2, menoDna3, menoDna4, menoDna5, menoDna6, menoDna7 = 'utorok',  'streda', 'stvrtok', 'piatok', 'sobota', 'nedela', 'pondelok'
    if den == 1 and mesiac == 1 and rok == 1901:
        for i in range(1, 32):
            print( i, 'je ', menoDna1 )
            menoDna1,menoDna2,menoDna3, menoDna4, menoDna5, menoDna6, menoDna7 = menoDna2, menoDna3, menoDna4, menoDna5, menoDna6, menoDna7, menoDna1
         
    
        
        
def vypisKalendara(den, mesiac, rok, inyDen, inyMesiac, inyRok):
    print (' po  ut  st  st  pi  so  ne')
    prvyDenvMesiaci = 'utorok'
    poslednyDenvMesiaci = 'sobota'
    #menoDna1, menoDna2, menoDna3, menoDna4, menoDna5, menoDna6, menoDna7 = 'utorok',  'streda', 'stvrtok', 'piatok', 'sobota', 'nedela', 'pondelok'
    #for i in range (1, pocetDnivMesiaci(den, mesiac, rok, inyDen, inyMesiac, inyRok)+1):
    #    print('{:3}{:3}{:3}{:3}{:3}{:3}{:3}'.format(menoDna1,menoDna2,menoDna3, menoDna4, menoDna5, menoDna6, menoDna7))
    menoDna1, menoDna2, menoDna3, menoDna4, menoDna5, menoDna6, menoDna7 = 'utorok',  'streda', 'stvrtok', 'piatok', 'sobota', 'nedela', 'pondelok'
    if den == 1 and mesiac == 1 and rok == 1901:
        for i in range(1, 32):
            print( i, end=' ' )
            menoDna1,menoDna2,menoDna3, menoDna4, menoDna5, menoDna6, menoDna7 = menoDna2, menoDna3, menoDna4, menoDna5, menoDna6, menoDna7, menoDna1
