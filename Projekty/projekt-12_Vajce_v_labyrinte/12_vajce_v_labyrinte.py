'''
program nacita txt subor, kde su ulozene suradnice vajca, klucov, dveri a precodnych a neprechodnych oblasti. 
Vajce potom zbiera kluce a tym moze prechadzat cez zatvorene dvere. Cielom hry je dostat sa na zlte miesto.
'''

import tkinter
import re

class Vajce:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.id = None
        #self.sirka_vajca = 20
        #self.vyska_vajca = 26
        
    def kresli(self, g):
        self.g = g
        self.g.delete(self.id)
        self.id = g.create_oval(self.x +10, self.y +7, self.x + 30, self.y+33, fill = 'white')

    def pohni(self, dx, dy):
        self.x += dx
        self.y += dy
        self.g.move(self.id, dx, dy)


class Klucik:

    pocet = 0

    def __init__(self, x, y, polygon):
        self.x = x
        self.y = y
        self.polygon = polygon
        self.id = None

    def kresli(self, g):
        self.g = g
        self.id = g.create_polygon(self.polygon)

    def zmaz(self):
        self.g.delete(self.id)
        self.id = None

    def blizko(self, x, y):     # bod (x, y) nie je od kľúčika ďalej ako 20
        if self.id is not None and (abs(self.x - x)) <=20 and abs((self.y-y))<=20:
            Klucik.pocet += 1
            self.zmaz()

class Dvere:

    def __init__(self, x, y):
        # dvere su modry stvorec 40x40
        self.x = x
        self.y = y
        self.farba = 'blue'
        self.id = None

    def kresli(self, g):
        self.g = g
        self.g.delete(self.id)
        self.id = g.create_rectangle(self.x, self.y, self.x+40, self.y+40, fill = self.farba)

    def zmen_stav(self):      # zmeň farbu dverí
        self.farba = 'seagreen'
        return self.farba


class Program: 
    def __init__(self, meno_suboru):
        self.meno_suboru = meno_suboru
        self.pocet_riadkov_hracej_plochy = 0
        self.pole = []
        self.dvere = {}
        self.polygon_kluca = []
        self.suradnice_klucov = []
        self.kluce = []
        self.vel = 40
        self.farba = ['seagreen', 'brown','yellow']

        #self.riadok = []
        
        self.citaj_vstupny_txt_subor()
        
        self.g = tkinter.Canvas(height = self.vel*len(self.pole), width = self.vel*len(self.pole[0]))
        self.g.pack()

        #print(self.riadok)
        self.spracuj_vstupny_txt_subor()
        
        print(self.pole)
        #print(self.polygon_kluca)
        #print(type(self.polygon_kluca))
        print(self.dvere)
        #print(self.suradnice_klucov)

        self.kresli()
        self.vykresli_kluce()
        
        self.g.bind_all('<Key>', self.pohni)
        self.g.mainloop()

    def citaj_vstupny_txt_subor(self):
        with open(self.meno_suboru, 'r') as subor:
            riadok = list(subor.readline().strip())
            self.pocet_riadkov_hracej_plochy += 1
            while riadok:
                self.pole.append(riadok)
                riadok = list(subor.readline().strip())
                self.pocet_riadkov_hracej_plochy += 1
            polygon_kluca = subor.readline().strip()
            self.polygon_kluca = re.split('\s',polygon_kluca)   # spravi list zo suradnic
            riadok = subor.readline().strip()
            riadok = re.split('\s',riadok) #spravi list zo suradnic klucov
            while riadok:
                self.suradnice_klucov.append(tuple(riadok))
                riadok = subor.readline().strip()
                if riadok:
                    riadok = re.split('\s',riadok)
            subor.close()


    def vykresli_kluce(self):
        #polygon_kluca = ['-15', '7', '-8', '0', '-1', '7', '15', '7', '15', '10', '12', '10', '12', '14', '5', '14', '5', '10', '-1', '10', '-8', '17', '-15', '10']
        #suradnice_klucov = [['260', '180'], ['160', '200'], ['60', '320'], ['60', '340'], ['60', '60'], ['60', '80']]
    
        c=[0]*len(self.polygon_kluca)

        for a,b in enumerate(self.suradnice_klucov):
            for i in range(len(self.polygon_kluca)):
                if i%2 == 0:
                    c[i] = int(self.polygon_kluca[i]) + int(b[0])
                else:
                    c[i] = int(self.polygon_kluca[i]) + int(b[1])
                #print(c)
            #self.kluce.append(c)
            self.kluc = Klucik(int(b[0]), int(b[1]), c)
            self.kluce.append(self.kluc)
            self.kluc.kresli(self.g)
            c=[0]*len(self.polygon_kluca)
    

    def kresli(self):
        # aby to bolo spravne, trebalo otocit riadok a stlpec ()
        for s in range(len(self.pole[0])):
            for r in range(len(self.pole)):
                x,y = s*self.vel, r*self.vel
                f = self.farba['.xk'.index(self.pole[r][s])]
                if f == 'brown':
                    self.g.create_rectangle(x, y, x+self.vel, y+self.vel, fill = f)
                else:
                    self.g.create_rectangle(x, y, x+self.vel, y+self.vel, fill = f, outline = f)
        for kluc, hodnota in self.dvere.items():
            hodnota.x= hodnota.x*self.vel
            hodnota.y = hodnota.y*self.vel
            hodnota.kresli(self.g)
        
        print(self.vajce.x, self.vajce.y)
        self.vajce.x = 6 * self.vel
        self.vajce.y = 5 * self.vel
        print(self.vajce.x, self.vajce.y)
        self.vajce.kresli(self.g)





    #def pohni(self, dx, dy):        # zavolá sa z udalosti stlačenie šípky
        
    def pohni(self, event):
        key = event.keysym
        # key type is 'str'
        #self.x +10, self.y +7, self.x + 30, self.y+33
        def hore():
            r = (self.vajce.y + 7 -4)//40
            s = (self.vajce.x+30)//40
            print(r, s)
            #print(Klucik.pocet)
            if self.pole[r][s] == 'x':
                return

            else:
                for kluc, hodnota in self.dvere.items():
                    if '{}{}'.format(s,r) == kluc:
                        
                        if Klucik.pocet>0:
                            self.dvere.pop(kluc)
                            Klucik.pocet -= 1
                            hodnota.zmen_stav()
                            hodnota.kresli(self.g)
                            self.vajce.kresli(self.g)
                    
                        else:
                            return
                for klucik in self.kluce:
                    klucik.blizko(int(self.vajce.x), int(self.vajce.y))
                self.vajce.pohni(0,-4)
                # for klucik in self.kluce:
                #     klucik.blizko(int(self.vajce.x), int(self.vajce.y))
                # for kluc, hodnota in self.dvere.items():
                #     if '{}{}'.format(s,r) == kluc:
                #         if Klucik.pocet>1:
                #             hodnota.zmen_stav()
                #             hodnota.kresli(self.g)
                #             self.vajce.kresli(self.g)

        def dole():
            r = (self.vajce.y+33+4)//40 
            s = (self.vajce.x+30)//40
            print(r, s)
            #print(Klucik.pocet)
            if self.pole[r][s] == 'k':
                self.g.create_text(300,90, text = 'HURAAAAA', fill='red', font='Arial 40 bold')
                self.g.update()
            if self.pole[r][s] == 'x':
                return

            else:
                for kluc, hodnota in self.dvere.items():
                    if '{}{}'.format(s,r) == kluc:
                        if Klucik.pocet>0:
                            self.dvere.pop(kluc)
                            Klucik.pocet -= 1
                            hodnota.zmen_stav()
                            hodnota.kresli(self.g)
                            self.vajce.kresli(self.g)
                        else:
                            return
                for klucik in self.kluce:
                    klucik.blizko(int(self.vajce.x), int(self.vajce.y))
                self.vajce.pohni(0,4)
            # for kluc, hodnota in self.dvere.items():
            #     if kluc == '{}{}'.format(s,r):
            #         return
            # if self.pole[r][s] == 'x':
            #     return
            
            # else:
            #     self.vajce.pohni(0,4)
            #     for klucik in self.kluce:
            #         klucik.blizko(int(self.vajce.x), int(self.vajce.y))
            #     for kluc, hodnota in self.dvere.items():
            #         if '{}{}'.format(s,r) == kluc:
            #             hodnota.zmen_stav()
            #             hodnota.kresli(self.g)
            #             self.vajce.kresli(self.g)
        
        def vlavo():
            r = ((self.vajce.y+7)//40)
            s = (self.vajce.x + 10 -4)//40
            print(r, s)
            #print(Klucik.pocet)
            if self.pole[r][s] == 'x':
                return

            else:
                for kluc, hodnota in self.dvere.items():
                    if '{}{}'.format(s,r) == kluc:
                        if Klucik.pocet>0:
                            self.dvere.pop(kluc)
                            Klucik.pocet -= 1
                            hodnota.zmen_stav()
                            hodnota.kresli(self.g)
                            self.vajce.kresli(self.g)
                        else:
                            return
                for klucik in self.kluce:
                    klucik.blizko(int(self.vajce.x), int(self.vajce.y))
                self.vajce.pohni(-4,0)
            
            # if self.pole[r][s] == 'x':
            #     return
            
            # else:
            #     self.vajce.pohni(-4,0)
            #     for klucik in self.kluce:
            #         klucik.blizko(int(self.vajce.x), int(self.vajce.y))
            # for kluc, hodnota in self.dvere.items():
            #         if '{}{}'.format(s,r) == kluc:
            #             hodnota.zmen_stav()
            #             hodnota.kresli(self.g)
            #             self.vajce.kresli(self.g)

        def vpravo():
            r = (self.vajce.y + 7)//40
            s = (self.vajce.x + 30 +4)//40
            print(r, s)
            #print(Klucik.pocet)
            if self.pole[r][s] == 'x':
                return

            else:
                for kluc, hodnota in self.dvere.items():
                    if '{}{}'.format(s,r) == kluc:
                        if Klucik.pocet>0:
                            self.dvere.pop(kluc)
                            Klucik.pocet -= 1
                            hodnota.zmen_stav()
                            hodnota.kresli(self.g)
                            self.vajce.kresli(self.g)
                        else:
                            return
                for klucik in self.kluce:
                    klucik.blizko(int(self.vajce.x), int(self.vajce.y))
                self.vajce.pohni(4,0)
            # if self.pole[r][s] == 'x':
            #     return
            # else:
            #     self.vajce.pohni(4,0)
            #     for klucik in self.kluce:
            #         klucik.blizko(int(self.vajce.x), int(self.vajce.y))
            # for kluc, hodnota in self.dvere.items():
            #         if '{}{}'.format(s,r) == kluc:
            #             hodnota.zmen_stav()
            #             hodnota.kresli(self.g)
            #             self.vajce.kresli(self.g)
        
        if key == 'Up':
            hore()
        if key == 'Down':
            dole()
        if key == 'Left':
            vlavo()
        if key == 'Right':
            vpravo()
    
    def spracuj_vstupny_txt_subor(self):
        print(self.pole)
        for r in range(len(self.pole)):
            for s in range(len(self.pole[r])):
                if self.pole[r][s] == 'v':
                    self.vajce = Vajce(s,r)
                    self.pole[r][s] = '.'
                if self.pole[r][s] == 'z':
                    self.dvere['{}{}'.format(s,r)] = Dvere(s,r)
                    self.pole[r][s] = '.'


Program('12_vajce_labyrint1.txt')