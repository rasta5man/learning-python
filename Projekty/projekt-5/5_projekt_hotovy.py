'''5. projekt - 12 bodov

Napíšte program v Pythone, ktorý rieši túto úlohu:

Noviny New York Times publikovali zoznam "bestsellerov" od roku 1942. Tento zoznam vznikol na základe celoštátneho sledovania najviac predaných výtlačkov.

Vašou úlohou bude navrhnúť, implementovať a testovať program, ktorý umožní používateľovi vyhľadávať v tomto zozname podmnožinu kníh, ktoré spĺňajú nejaké kritérium. Pre zjednodušenie bude dátový
súbor obsahovať len knihy z oblastí beletria (Fiction) a literatúra faktu (Nonfiction) od roku 1942.

Súbor bestseller.txt obsahuje sadu dát. Každý riadok súboru obsahuje údaje pre jednu knihu: názov, autora, vydavateľa, dátum, kedy sa prvýkrát dostala na prvé miesto.
Údaje v riadku sú navzájom oddelené znakmi tabulátora '\t'.

Váš program prečíta tento súbor a vytvorí z neho štruktúru zoznam kníh. Ak sa mu tento zoznam kníh nepodarí zostaviť, vypíše zodpovedajúce chybové hlásenie a skončí.

Po skonštruovaní zoznamu kníh, program zobrazí ponuku možností a umožní používateľovi vyhľadávať knihy podľa určitých kritérií. Položky menu sú:

    Výpis všetkých kníh z nejakého rozsahu rokov: Zobrazí výzvu na dva roky (štartový a koncový rok), potom vypíše všetky knihy, ktoré sú v zozname medzi týmito dvoma rokmi (vrátane).
    Napríklad, ak používateľ zadá "1970" a "1973", zobrazia sa všetky knihy, ktoré boli bestsellermi v rokoch 1970, 1971, 1972 alebo 1973.
    Výpis všetkých kníh z určitého mesiaca a roku: Zobrazí sa výzva na mesiac a rok, potom vypíše všetky knihy, ktoré boli bestsellermi v priebehu tohto mesiaca.
    Napríklad, ak používateľ zadá "7" a "1985" , zobrazia sa všetky knihy, ktoré boli bestsellermi v priebehu mesiaca júl v roku 1985.
    Hľadanie kníh nejakého autora: Zobrazí sa výzva na zadanie reťazca, potom vypíše všetky knihy, ktorých autor obsahuje tento reťazec (bez ohľadu na veľkosť písmen).
    Napríklad, ak používateľ zadá "ST", vypíšu sa všetky knihy, ktorých meno autora obsahuje reťazec "ST", "St", "sT" alebo "st".
    Hľadanie názvu: Zobrazí sa výzva na zadanie reťazca, potom vypíše všetky knihy, ktorých názov obsahuje tento reťazec (bez ohľadu na veľkosť písmen).
    Napríklad, ak používateľ zadá "secret", najdú sa tri knihy: "The Secret of Santa Vittoria" od Roberta Crichtona, "The Secret Pilgrim" od Johna le Carré a "Harry Potter and the Chamber of Secrets".

Poznámky

    Váš program sa musí skladať z minimálne štyroch funkcií: funkcie pre spracovanie každej zo štyroch volieb menu uvedených vyššie.
    Nie je povolené používanie žiadnych globálnych premenných: môžete používať iba premenné, ktoré sú v mennom priestore funkcií, t.j. ktoré vo funkcii vznikli priradením alebo
    sú parametrami funkcie.
    V programe môžete používať postupnosti ako reťazce, zoznamy a n-tice, ale žiadne iné štruktúrované typy.
    Ak nejakému dotazu nevyhovujú žiadne knihy, program by mal o tom vypísať nejakú správu.
    Váš program bude pokračovať, kým používateľ nezadá "K" (alebo "k") ako svoju voľbu.
    Váš program by mal žiadať len také vstupy, ktoré súvisia s požadovanou voľbou.
    Váš program správne spracuje aj chybné vstupy od používateľa. Ak sa pri zadávaní vstupu vyskytnú nejaké problémy, program na to upozorní a umožní užívateľovi vybrať inú možnosť.

Ukážkový výstup

Čo chceš robiť?
 1: Vyhľadávať podľa rokov
 2: Vyhľadávať podľa mesiaca a roku
 3: Vyhľadávať podľa autora
 4: Vyhľadávať podľa titulu
 K: Koniec
>1
Zadaj štartový rok: 1960
Zadaj koncový rok: 1962

Všetky tituly medzi 1960 a 1962:
 A Shade of Difference, by Allen Drury (10/28/1962)
 Franny and Zooey, by J. D. Sallinger (10/29/1961)
 Hawaii, by James Michener (1/17/1960)
 Seven Days in May, by Fletcher Knebel (11/18/1962)
 Ship of Fools, by Katherine Anne Porter (4/29/1962)
 The Agony and the Ecstasy, by Irving Stone (4/23/1961)
 The Last of the Just, by André Schwarz-Bart (3/26/1961)
 Born Free, by Joy Adamson (8/7/1960)
 Calories Don't Count, by Herman Taller (3/25/1962)
 May This House Be Safe from Tigers, by Alexander King (3/13/1960)
 Silent Spring, by Rachel Carson (10/28/1962)
 The Making of the President - 1960, by Theodore H. White (9/10/1961)
 The New English Bible, by Oxford University Press (Editor) (5/28/1961)
 The Rise and Fall of the Third Reich, by William Shirer (12/4/1960)
 The Rothchilds, by Frederic Morton (6/24/1962)
 The Waste Makers, by Vance Packard (11/6/1960)
 Travels with Charley, by John Steinbeck (10/21/1962)

Čo chceš robiť?
 1: Vyhľadávať podľa rokov
 2: Vyhľadávať podľa mesiaca a roku
 3: Vyhľadávať podľa autora
 4: Vyhľadávať podľa titulu
 K: Koniec
>2
Zadaj mesiac (ako číslo 1-12): 9
Zadaj rok: 1990

Všetky tituly v 9. 1990:
 Four Past Midnight, by Stephen King (9/16/1990)
 Memories of Midnight, by Sidney Sheldon (9/2/1990)
 Darkness Visible, by William Styron (9/16/1990)
 Millie's Book, by Barbara Bush (9/30/1990)
 Trump: Surviving at the Top, by Donald Trump (9/9/1990)

Čo chceš robiť?
 1: Vyhľadávať podľa rokov
 2: Vyhľadávať podľa mesiaca a roku
 3: Vyhľadávať podľa autora
 4: Vyhľadávať podľa titulu
 K: Koniec
>3
Zadaj meno autora (alebo časť mena): tolkein
 Silmarillion, by J. R. R. Tolkein (10/2/1977)
 The Children of the Húrin, by J.R.R. Tolkein (5/6/2007)

Čo chceš robiť?
 1: Vyhľadávať podľa rokov
 2: Vyhľadávať podľa mesiaca a roku
 3: Vyhľadávať podľa autora
 4: Vyhľadávať podľa titulu
 K: Koniec
>4
Zadaj titul (alebo časť titulu): secret
 Harry Potter and the Chamber of Secrets, by J. K. Rowling (6/20/1999)
 The Secret of Santa Vittoria, by Robert Crichton (11/20/1966)
 The Secret Pilgrim, by John le Carré (1/20/1991)

Váš odovzdaný program musí začínať tromi riadkami komentárov:

    # 5. projekt: bestseller
    # autor: Janko Hraško
    # dátum: 31.10.2013

Používajte len také konštrukcie jazyka Python, ktoré sme sa zatiaľ učili. '''

# 5. projekt: bestseller
# autor: Rasta5man king KovaK
# dátum: 10.8.2018

# nacita zoznam knih zo suboru do pola (polozky pola su polia s hodnotami - 0=nazov knihy, 1=autor, 2=vydavatelstvo, 3=datum, 4=fiction )
def zapisSuboru(subor):
    zoznamKnih=[]
    with open(subor) as subor:
        riadok = ' '
        while riadok != '':
            riadok = subor.readline()
            riadok = riadok.strip()
            polezRiadka = riadok.split('\t')
            zoznamKnih.append(polezRiadka)
    subor.close()
    zoznamKnih.pop()
    return zoznamKnih

#funkcia vypise knihy zo suboru podla zadanych rokov
def rozsahRokov():
    zaciatok = input('zadaj startovy rok: ')
    koniec = input('zadaj koncovy rok: ')
    pole = zapisSuboru('/Users/Tomik/Downloads/learning-python/Projekty/projekt-5/5_projekt_bestsellers.txt')
    print('\nToto su vsetky tituly v rokoch medzi', zaciatok, ' a ', koniec, ':\n')
    # nasledujuce dva for cykly vyberu z pola zoznamKnih datum a potom rozdelia na pole z 3 prvkov - mesiac, den a rok( napr.
    # datumy = ['8/30/2000', '9/24/1978', atd a potom datumyRozdelene=[['8','30','2000'],['9','24','1978'], atd...)
    datumy=[]
    datumyRozdelene=[]
    pocet = 0
    for i in range (len(pole)):
        datumy.append(pole[i][3])
    for i in range(len(datumy)):
        retazec = datumy[i].split('/')
        datumyRozdelene.append(retazec)
    for i in range(len(datumyRozdelene)):
        for j in range(int(zaciatok), int(koniec)+1):
            if str(j) == datumyRozdelene[i][2]:
                print ('  ',pole[i][0],', by',pole[i][1],'(',pole[i][3],')')
                pocet += 1
    print()
    print('Pocet najdenych titulov = ', pocet)
    print()

#funkcia vypise knihy zo suboru podla mena autora (moze byt zadany aj malymi pismenami)
def menoAutora():
    menoAutora = input('Zadaj meno autora (alebo časť mena): ')
    menoAutora = menoAutora.lower()
    pole = zapisSuboru('/Users/Tomik/Downloads/learning-python/Projekty/projekt-5/5_projekt_bestsellers.txt')
    print('\nToto su vsetky tituly od autora', menoAutora, ':\n')
    pocet = 0
    for i in range(len(pole)):
        retazec = pole[i][1]
        retazec = retazec.lower()
        if menoAutora in retazec:
            print ('  ',pole[i][0],', by',pole[i][1],'(',pole[i][3],')')
            pocet += 1
    print()
    print(' Pocet najdenych titulov = ', pocet)
    print()

#funkcia vypise knihy zo suboru podla mesiaca a roku
def mesiacRok():
    mesiac = input('Zadaj mesiac (ako číslo 1-12): ')
    rok = input('zadaj rok: ')
    pole = zapisSuboru('/Users/Tomik/Downloads/learning-python/Projekty/projekt-5/5_projekt_bestsellers.txt')
    print('\nToto su vsetky tituly v ', mesiac, '. mesiaci a v ' , rok,  'roku :\n')
    # nasledujuce dva for cykly vyberu z pola zoznamKnih datum a potom rozdelia na pole z 3 prvkov - mesiac, den a rok( napr.
    # datumy = ['8/30/2000', '9/24/1978', atd a potom datumyRozdelene=[['8','30','2000'],['9','24','1978'], atd...)
    datumy=[]
    datumyRozdelene=[]
    pocet = 0
    for i in range (len(pole)):
        datumy.append(pole[i][3])
    for i in range(len(datumy)):
        retazec = datumy[i].split('/')
        datumyRozdelene.append(retazec)
    for i in range(len(datumyRozdelene)):
        if mesiac == datumyRozdelene[i][0] and rok == datumyRozdelene[i][2]:
            print ('  ',pole[i][0],', by',pole[i][1],'(',pole[i][3],')')
            pocet += 1
    print()
    print('Pocet najdenych titulov = ', pocet)
    print()

#funkcia vypise knihy zo suboru podla nazvu knihy (moze byt zadany aj malymi pismenami)
def titul():
    titul = input('Zadaj titul (alebo časť titulu): ')
    titul = titul.lower()
    pole = zapisSuboru('/Users/Tomik/Downloads/learning-python/Projekty/projekt-5/5_projekt_bestsellers.txt')
    print('\nToto su vsetky tituly ', titul, ':\n')
    pocet = 0
    for i in range(len(pole)):
        retazec = pole[i][0]
        retazec = retazec.lower()
        if titul in retazec:
            print ('  ',pole[i][0],', by',pole[i][1],'(',pole[i][3],')'  )
            pocet += 1
    print()
    print('Pocet najdenych titulov = ', pocet)
    print()

def vyberMenu():
    return input('\nČo chceš robiť?\n 1: Vyhľadávať podľa rokov\n 2: Vyhľadávať podľa mesiaca a roku\n 3: Vyhľadávať podľa autora\n 4: Vyhľadávať podľa titulu\n K: Koniec\n>')

vstup = vyberMenu()
while vstup != 'K':

    if  vstup == '1':
        rozsahRokov()
    elif vstup == '2':
        mesiacRok()
    elif vstup == '3':
        menoAutora()
    elif vstup == '4':
        titul()
    elif vstup == 'k' or vstup == 'K':
        print()
        print('*****************************')
        print('Dakujeme za pouzitie programu')
        print('*****************************')
        input()
        break
    else:
        print()
        print('************************************************')
        print('Prosim zadajte polozku z menu - 1,2,3,4, alebo K')
        print('************************************************')
        print()

    vstup = vyberMenu()
