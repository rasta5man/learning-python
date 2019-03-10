import tkinter

vyska = 50

class Utvar:                                    # materska trieda pre vsetky utvary

    def __init__(self, x, y, farba, canvas):
        self.x = x
        self.y = y
        self.farba = farba
        self.canvas = canvas

    def posun(self, dx, dy):                    # definuje posun utvarov z ovladacieho panelu na pracovnu plochu   
        self.x += dx
        self.y += dy
        canvas.move(self.id, dx, dy)
        #self.canvas.move(self.id, dx, dy)      # neviem ktroy je spravne, ale funguju obidva

    def zmen_farbu(self, farba):
        self.farba = farba
        canvas.itemconfig(self.id, fill = farba)
        #self.canvas.itemconfig(self.id, fill = farba)    # neviem ktroy je spravne, ale funguju obidva


class Stvorec(Utvar):

    def __init__(self, x, y, farba, canvas):
        super().__init__(x, y, farba, canvas)
        self.id = canvas.create_rectangle(self.x, self.y, self.x + vyska, self.y + vyska, fill= self.farba, width = 3)
        self.povodneX = self.x
        self.povodneY = self.y
    
    def je_klik(self, x, y):
        if self.x <= x <=self.x+vyska and self.y <= y <= self.y+vyska:
            return True
    
    def __str__(self):
        return 'stvorec,{},{},{}'.format(self.x, self.y, self.farba)

    def kopia(self):
        return Stvorec(self.x,self.y,self.farba,canvas)
    
    def vrat_sa_naspat(self):
        canvas.coords(self.id, self.povodneX, self.povodneY, self.povodneX+vyska, self.povodneY+vyska)


class Kruh(Utvar):

    def __init__(self, x, y, farba, canvas):
        super().__init__(x,y,farba, canvas)
        self.r = vyska/2
        self.povodneX = self.x
        self.povodneY = self.y
        self.id = canvas.create_oval(self.x-self.r, self.y-self.r, self.x+self.r, self.y+self.r, fill=self.farba, width = 3)
    
    def __str__(self):
        return 'kruh,{},{},{}'.format(self.x, self.y, self.farba)

    def je_klik(self,x,y):
        return (self.x - x)**2 + (self.y-y)**2 < (vyska/2)**2

    def kopia(self):
        return Kruh(self.x, self.y, self.farba, canvas)

    def vrat_sa_naspat(self):
        canvas.coords(self.id, self.povodneX - self.r, self.povodneY - self.r, self.povodneX + self.r, self.povodneY + self.r )


class Obdlznik(Utvar):

    def __init__(self, x, y, sirka, farba, canvas):
        super().__init__(x,y,farba,canvas)
        self.sirka = sirka
        self.povodneX = self.x
        self.povodneY = self.y
        self.id = canvas.create_rectangle(self.x, self.y, self.x +self.sirka, self.y + vyska, fill = self.farba, width = 3)

    def __str__(self):
        return 'obdlznik,{},{},{},{}'.format(self.x, self.y, self.sirka, self.farba) 

    def je_klik(self, x, y):
        return self.x <= x <=self.x+self.sirka and self.y <= y <= self.y+vyska

    def vrat_sa_naspat(self):
        canvas.coords(self.id, self.povodneX, self.povodneY, self.povodneX + self.sirka, self.povodneY + vyska)

    def kopia(self):
        return Obdlznik(self.x, self.y, self.sirka, self.farba, canvas)


class Obdlznik1(Utvar):

    def __init__(self, x, y, sirka, farba, canvas):
        super().__init__(x,y,farba, canvas)
        self.sirka = sirka
        self.povodneX = self.x
        self.povodneY = self.y
        self.id = canvas.create_rectangle(self.x, self.y, self.x +vyska, self.y + self.sirka, fill = self.farba, width = 3)

    def __str__(self):
        return 'obdlznik1,{},{},{},{}'.format(self.x, self.y, self.sirka, self.farba)

    def je_klik(self, x, y):
        return self.x <= x <=self.x+vyska and self.y <= y <= self.y+self.sirka

    def vrat_sa_naspat(self):
        canvas.coords(self.id, self.povodneX, self.povodneY, self.povodneX + vyska, self.povodneY + self.sirka)

    def kopia(self):
        return Obdlznik1(self.x, self.y, self.sirka, self.farba, canvas)


class Trojuholnik(Utvar):

    def __init__(self, x, y, farba, canvas):
        super().__init__(x, y, farba, canvas)
        self.povodneX = self.x
        self.povodneY = self.y
        self.id = canvas.create_polygon(self.x, self.y, self.x + vyska, self.y, self.x + vyska/2, self.y - vyska, self.x, self.y, fill = self.farba, outline ='black',  width =3)

    def __str__(self):
        return 'trojuholnik,{},{},{}'.format(self.x, self.y, self.farba)

    def je_klik(self,x,y):
        return self.x <= x <=self.x+ vyska and self.y >= y > self.y-vyska

    def kopia(self):
        return Trojuholnik(self.x, self.y, self.farba, canvas)

    def vrat_sa_naspat(self):
        canvas.coords(self.id, self.povodneX, self.povodneY, self.povodneX + vyska, self.povodneY, self.povodneX + vyska/2, self.povodneY - 50, self.povodneX, self.povodneY)


class Oval(Utvar):

    def __init__(self, x, y, farba, canvas):
        super().__init__(x, y, farba, canvas)
        self.povodneX = self.x
        self.povodneY = self.y
        self.id = canvas.create_oval(self.x - vyska-15, self.y -vyska/2, self.x+vyska-15, self.y + vyska/2, fill =self.farba, width = 3)

    def __str__(self):
        return 'oval,{},{},{}'.format(self.x, self.y, self.farba)

    def je_klik(self,x,y):
        return (self.x - x)**2 + (self.y-y)**2 < (vyska/2)**2

    def kopia(self):
        return Oval(self.x, self.y, self.farba, canvas)

    def vrat_sa_naspat(self):
        canvas.coords(self.id, self.povodneX - vyska - 15, self.povodneY - vyska/2, self.povodneX + vyska - 15, self.povodneY + vyska/2)


class Vedierko(Utvar):

    def __init__(self, x, y, farba, canvas):
        super().__init__(x,y,farba, canvas)
        self.r = 15
        self.povodneX = self.x
        self.povodneY = self.y
        self.id = canvas.create_oval(self.x - self.r, self.y - self.r, self.x+self.r, self.y+self.r, fill = self.farba, width = 5)

    def je_klik(self,x,y):
        return (self.x - x)**2 + (self.y-y)**2 < (self.r)**2

    def vrat_sa_naspat(self):
        canvas.coords(self.id, self.povodneX - self.r, self.povodneY - self.r, self.povodneX + self.r, self.povodneY + self.r )


class Tlacidlo(Utvar):      # definuje tri tlacidla z ovladacieho panelu (zapis do suboru, citaj zo suboru a zmaz pracovnu plochu

    def __init__(self, x, y, s, farba, canvas):
        super().__init__(x, y, farba, canvas)
        self.sirka= s
        self.text = ''
        self.id = canvas.create_rectangle(self.x, self.y, self.x + self.sirka, self.y + vyska, fill = self.farba, width = 3)
    
    def je_klik(self, x, y):
        if self.x <= x <= self.x + self.sirka and self.y <= y <= self.y + vyska:
            return True
        
    def citaj_subor(self, event):
        # najskor zmazem vsetky utvary z pola, ktore nepatria do ovladacieho panela
        for utvar in range(16, len(program.zoznam_vsetkych_utvarov)):
            canvas.delete(program.zoznam_vsetkych_utvarov[utvar].id)
        program.zoznam_vsetkych_utvarov = program.zoznam_vsetkych_utvarov[:16]
        try:
            with open('8_utvary.txt', 'r') as subor:
                for riadok in subor:
                    utvar = riadok.strip().split(',')
                    if utvar[0] == 'stvorec':
                        stvorec = Stvorec(int(utvar[1]), int(utvar[2]), utvar[3], canvas)
                        program.pridaj_utvar_do_skupiny(stvorec)
                    elif utvar[0] == 'kruh':
                        kruh = Kruh(int(utvar[1]), int(utvar[2]), utvar[3], canvas)
                        program.pridaj_utvar_do_skupiny(kruh)
                    elif utvar[0] == 'obdlznik':
                        obdlznik = Obdlznik(int(utvar[1]), int(utvar[2]), int(utvar[3]), utvar[4], canvas)
                        program.pridaj_utvar_do_skupiny(obdlznik)
                    elif utvar[0] == 'obdlznik1':
                        obdlznik1 = Obdlznik1(int(utvar[1]), int(utvar[2]), int(utvar[3]), utvar[4], canvas)
                        program.pridaj_utvar_do_skupiny(obdlznik1)
                    elif utvar[0] == 'trojuholnik':
                        trojuholnik = Trojuholnik(int(utvar[1]), int(utvar[2]), utvar[3], canvas)
                        program.pridaj_utvar_do_skupiny(trojuholnik)
                    elif utvar[0] == 'oval':
                        oval = Oval(int(utvar[1]), int(utvar[2]), utvar[3], canvas)
                        program.pridaj_utvar_do_skupiny(oval)
                subor.close()
        except FileNotFoundError:
            print ('subor sa nenasiel')

    def zapis_do_suboru(self, event):
        # do suboru zapisujem utvary zo zonamu od 16 -->> 0-15 su utvary na ovladacom paneli
        with open('8_utvary.txt', 'w') as subor:
            for i in range(16, len(program.zoznam_vsetkych_utvarov)):
                subor.write(str(program.zoznam_vsetkych_utvarov[i]))
                subor.write('\n')
            print('vsetky utvary uspesne zapisane')
        subor.close()

    def zmaz_plochu(self, event):
        #prvych 15 objektov je ovladacich, preto sa iteruje az od cisla 16 az po koniec pola
        if program.zoznam_vsetkych_utvarov:
            for i in range(16, len(program.zoznam_vsetkych_utvarov)):
                canvas.delete(program.zoznam_vsetkych_utvarov[i].id)
            program.zoznam_vsetkych_utvarov = program.zoznam_vsetkych_utvarov[:16]
            # funguje aj ked to dam takto, neviem ktore je spravne
            # program.zoznam_vsetkych_utvarov[:] = program.zoznam_vsetkych_utvarov[:16]


class Program():
    
    def __init__(self, sirka, height, canvas, rozdelenie):
        self.sirka = sirka
        self.height = height
        self.rozdelenie = rozdelenie
        self.canvas = canvas
        self.canvas.create_rectangle(3, 3, self.rozdelenie + 4, self.height, width = 4, fill = 'gold')
        self.canvas.create_rectangle(self.rozdelenie + 12, 3, self.sirka, self.height, width = 4, fill = 'white')
        self.zoznam_vsetkych_utvarov = []
        self.canvas.bind('<Button-1>', self.on_klik)
        
    def on_klik(self, event):
        self.utvar = self.na_co_klikam(event)
        self.x0, self.y0 = event.x, event.y
        if self.utvar == None:
            return
        elif self.utvar == tlacidlo1:
            self.canvas.bind('<ButtonRelease-1>', tlacidlo1.citaj_subor)
        elif self.utvar == tlacidlo2:
            self.canvas.bind('<ButtonRelease-1>', tlacidlo2.zapis_do_suboru)
        elif self.utvar == tlacidlo3:
            self.canvas.bind('<ButtonRelease-1>', tlacidlo3.zmaz_plochu)
        else:
            self.canvas.bind('<B1-Motion>', self.udalost_tahaj)
            self.canvas.bind('<ButtonRelease-1>', self.udalost_pusti)
           
    def udalost_tahaj(self, event):
        self.utvar.posun(event.x - self.x0, event.y - self.y0)
        self.x0 = event.x
        self.y0 = event.y
        
    def udalost_pusti(self, event):
        if isinstance(self.utvar, Vedierko):
            self.vedierko_je_na_utvare(event.x, event.y)
            self.utvar.x = self.utvar.povodneX
            self.utvar.y = self.utvar.povodneY
            self.utvar.vrat_sa_naspat()
        if self.utvar.id != 9 and self.utvar.id != 10 and self.utvar.id !=11 and self.utvar.id !=12 \
            and self.utvar.id != 13 and self.utvar.id !=14 and self.utvar.id != 15 and self.utvar.id != 16 \
            and self.utvar.id != 17 and self.utvar.id != 18 and self.utvar.id != 19 and self.utvar.id != 20 \
            and self.utvar.id != 21:
            if self.utvar.x>780 or self.utvar.x<220 or self.utvar.y>580 or self.utvar.y<20:
                canvas.delete(self.utvar.id)
        if self.utvar.id == 9 or self.utvar.id == 10 or self.utvar.id == 11 or self.utvar.id==12 or self.utvar.id == 13 \
            or self.utvar.id == 14:
            if 780>event.x >250 and 580>event.y>20:
                new = self.utvar.kopia()
                self.pridaj_utvar_do_skupiny(new)
                self.utvar.x = self.utvar.povodneX
                self.utvar.y = self.utvar.povodneY
                self.utvar.vrat_sa_naspat()
            else:
                self.utvar.x = self.utvar.povodneX
                self.utvar.y = self.utvar.povodneY
                self.utvar.vrat_sa_naspat()
        self.canvas.unbind('<B1-Motion>')
        self.canvas.unbind('<ButtonRelease-1>')
        
        #debugoval som
        #print(self.zoznam_vsetkych_utvarov)
        #print(self.utvar.id)
        #print(self.utvar.x, self.utvar.y)
        
    def na_co_klikam(self, event):
        ix = len(self.zoznam_vsetkych_utvarov)-1
        while ix >= 0 and not self.zoznam_vsetkych_utvarov[ix].je_klik(event.x, event.y):
            ix -= 1
        if ix < 0:
            return None
        else:
            return self.zoznam_vsetkych_utvarov[ix]
        
    def pridaj_utvar_do_skupiny(self, utvar):
        self.zoznam_vsetkych_utvarov.append(utvar)
    
    def vedierko_je_na_utvare(self,x,y):
        for i in range(16, len(self.zoznam_vsetkych_utvarov)):
            if isinstance(self.zoznam_vsetkych_utvarov[i], Kruh):
                if (self.zoznam_vsetkych_utvarov[i].x - x)**2 + (self.zoznam_vsetkych_utvarov[i].y-y)**2 < (self.zoznam_vsetkych_utvarov[i].r)**2:
                    self.zoznam_vsetkych_utvarov[i].zmen_farbu(self.utvar.farba)
            elif isinstance(self.zoznam_vsetkych_utvarov[i], Stvorec):
                if self.zoznam_vsetkych_utvarov[i].x <= x <=self.zoznam_vsetkych_utvarov[i].x+vyska and \
                    self.zoznam_vsetkych_utvarov[i].y <= y <= self.zoznam_vsetkych_utvarov[i].y+vyska:
                    self.zoznam_vsetkych_utvarov[i].zmen_farbu(self.utvar.farba)
            elif isinstance(self.zoznam_vsetkych_utvarov[i], Obdlznik):
                if self.zoznam_vsetkych_utvarov[i].x <= x <=self.zoznam_vsetkych_utvarov[i].x+self.zoznam_vsetkych_utvarov[i].sirka and \
                    self.zoznam_vsetkych_utvarov[i].y <= y <= self.zoznam_vsetkych_utvarov[i].y+vyska:
                    self.zoznam_vsetkych_utvarov[i].zmen_farbu(self.utvar.farba)
            elif isinstance(self.zoznam_vsetkych_utvarov[i], Obdlznik1):
                if self.zoznam_vsetkych_utvarov[i].x <= x <=self.zoznam_vsetkych_utvarov[i].x+vyska and \
                    self.zoznam_vsetkych_utvarov[i].y <= y <= self.zoznam_vsetkych_utvarov[i].y+self.zoznam_vsetkych_utvarov[i].sirka:
                    self.zoznam_vsetkych_utvarov[i].zmen_farbu(self.utvar.farba)
            elif isinstance(self.zoznam_vsetkych_utvarov[i], Trojuholnik):
                if self.zoznam_vsetkych_utvarov[i].x <= x <=self.zoznam_vsetkych_utvarov[i].x+ vyska and self.zoznam_vsetkych_utvarov[i].y >= y > self.zoznam_vsetkych_utvarov[i].y-vyska:
                    self.zoznam_vsetkych_utvarov[i].zmen_farbu(self.utvar.farba)
            elif isinstance(self.zoznam_vsetkych_utvarov[i], Oval):
                if (self.zoznam_vsetkych_utvarov[i].x - x)**2 + (self.zoznam_vsetkych_utvarov[i].y-y)**2 < (vyska/2)**2:
                    self.zoznam_vsetkych_utvarov[i].zmen_farbu(self.utvar.farba)


canvas = tkinter.Canvas(height = 600, width = 800)
canvas.pack()
    
program = Program(800, 600, canvas, 200)
    
tlacidlo1 = Tlacidlo(20,20,160, 'red', canvas)
tlacidlo1.text = canvas.create_text(100,46, text = 'Prečítaj súbor', font = 'arial 11')
tlacidlo2= Tlacidlo(20,80,160, 'blue',canvas)
tlacidlo2.text = canvas.create_text(100,106, text='Zapíš do súboru', font = 'arial 11')
tlacidlo3 = Tlacidlo(20,140,160, 'green',canvas)
tlacidlo3.text = canvas.create_text(100,166, text='Zmaž pracovnú oblasť', font = 'arial 11')

stvorec = Stvorec(148,260, 'blue', canvas)
kruh = Kruh(118, 285, 'blue', canvas)
obdlznik = Obdlznik(8,260,80,'blue', canvas)
obdlznik1 = Obdlznik1(8, 320, 80, 'blue', canvas )
trojuholnik = Trojuholnik(64, 402, 'blue', canvas)
oval = Oval(163, 344, 'blue', canvas)
vedierko_cervene = Vedierko(25, 490, 'red', canvas)
vedierko_zelene = Vedierko(75, 490, 'green', canvas)
vedierko_modre = Vedierko(125, 490, 'blue', canvas)
vedierko_zlte = Vedierko(175, 490, 'yellow', canvas)
vedierko_hnede = Vedierko(25, 530, 'brown', canvas)
vedierko_cierne = Vedierko(75,530, 'black', canvas)
vedierko_biele = Vedierko(125,530,'white', canvas)

program.pridaj_utvar_do_skupiny(stvorec)
program.pridaj_utvar_do_skupiny(kruh)
program.pridaj_utvar_do_skupiny(tlacidlo1)
program.pridaj_utvar_do_skupiny(tlacidlo2)
program.pridaj_utvar_do_skupiny(tlacidlo3)
program.pridaj_utvar_do_skupiny(obdlznik)
program.pridaj_utvar_do_skupiny(obdlznik1)
program.pridaj_utvar_do_skupiny(trojuholnik)
program.pridaj_utvar_do_skupiny(oval)
program.pridaj_utvar_do_skupiny(vedierko_cervene)
program.pridaj_utvar_do_skupiny(vedierko_zelene)
program.pridaj_utvar_do_skupiny(vedierko_modre)
program.pridaj_utvar_do_skupiny(vedierko_zlte)
program.pridaj_utvar_do_skupiny(vedierko_hnede)
program.pridaj_utvar_do_skupiny(vedierko_cierne)
program.pridaj_utvar_do_skupiny(vedierko_biele)

canvas.mainloop()




    
