from kor import *
import random

class Akvarium:
    def __init__(self):
        self.k = Kor()
        self.k.ht()
        self.vykresli_akvarium()
        
    def vykresli_akvarium(self):
        self.k.pu()
        self.k.setpos(290,290)
        self.k.pd()
        self.k.seth(270)
        self.k._pw = 10
        for i in range(3):
            self.k.fd(580)
            self.k.rt(90)
        self.k._pw = 3
        self.k.setpos(-285,285)
        self.k.rt(20)                   # voda hore
        self.k.fd(50)
        self.k.lt(40)
        self.k.fd(50)
        self.k.rt(40)
        self.k.fd(50)
        self.k.lt(40)
        self.k.fd(50)
        self.k.rt(40)
        self.k.fd(50)
        self.k.lt(40)
        self.k.fd(50)
        self.k.rt(40)
        self.k.fd(50)
        self.k.lt(40)
        self.k.fd(50)
        self.k.rt(40)
        self.k.fd(50)
        self.k.lt(40)
        self.k.fd(50)
        self.k.rt(40)
        self.k.fd(50)
        self.k.lt(38)
        self.k.fd(65)

class Rybka():
    def __init__(self, x, y):
        self.x, self.y = x, y
        self.krokX = random.choice([-4,-2, 2, 4])   # nahodny vyber pre rychlost pohybu rybky
        self.krokY = random.choice([-2,0,2])        # nahodny vyber pre uhol pohybu rybky
        self.k = None                               # korytnacka vykresluje rybku
        self.counter = random.randrange(50)         # ked je counter modulo200 0, rybka sa nahodne otoci
        self.zivot = 200                            # ked je zivot 0, rybka zomrie
        self.konkretna_potrava = None               # rybka zameria konkretnu potravu
        self.vzdialenost = None                     # vzdialenost rybky od potravy
        
    def kresli_rybku_vlavo(self):
        self.k.ht()
        self.k.setpos(self.x, self.y)
        self.k.seth(40)
        for i in range(9):
            self.k.fd(6)
            self.k.rt(15)
        self.k.pu()
        self.k.setpos(self.x, self.y)
        self.k.seth(-40)
        self.k.pd()
        for i in range(9):
            self.k.fd(6)
            self.k.lt(15)
        self.k.seth(270)
        self.k.fd(30)
        self.k.pu()                         #oko rybky
        self.k.setpos(self.x+9, self.y +2)
        self.k.pd()
        for i in range(18):
            self.k.fd(0.5)
            self.k.lt(20)
        self.k.pu()                         #indikator zivota     
        self.k.setpos(self.x +5 , self.y + 20)
        self.k.pd()
        self.k._pw = self.zivot / 20
        self.k.seth(0)
        self.k.fd(30)
    
    def kresli_rybku_vpravo(self):
        self.k.ht()
        self.k.setpos(self.x, self.y)
        self.k.seth(140)
        for i in range(9):
            self.k.fd(6)
            self.k.lt(15)
        self.k.pu()
        self.k.setpos(self.x, self.y)
        self.k.seth(-140)
        self.k.pd()
        for i in range(9):
            self.k.fd(6)
            self.k.rt(15)
        self.k.seth(270)
        self.k.fd(30)
        self.k.pu()                         #oko rybky
        self.k.setpos(self.x-9, self.y+2)
        self.k.pd()
        for i in range(18):
            self.k.fd(0.5)
            self.k.lt(20)
        self.k.pu()                         #indikator zivota
        self.k.setpos(self.x -5, self.y + 20)
        self.k.pd()
        self.k._pw = self.zivot / 20
        self.k.seth(180)
        self.k.fd(30)
 
class Potrava():
    def __init__(self, x, y):
        self.x, self.y = x, y
        self.k = None
        self.krok = random.choice([-1,-2])
            
    def vykresli_potravu(self):
        self.k._pw = random.choice([2,4])
        self.k.ht()
        for i in range(3):
            self.k.fd(5)
            self.k.rt(120)

class Program:
    def __init__(self):
        bgcolor('white')            # inicializacia plochy
        self.rybky=[]
        self.potrava=[]
        Akvarium().vykresli_akvarium()
        Kor.g.bind('<Button-3>', self.pridaj_rybku)
        Kor.g.bind('<Button-1>', self.pridaj_potravu)
        Kor.g.bind('<B1-Motion>', self.pridaj_potravu)
        self.timer()
        Kor.g.mainloop()
    
    def pridaj_rybku(self, event):
        self.rybky.append(Rybka(event.x - Kor._x0, Kor._y0 - event.y))
    
    def pridaj_potravu(self, event):
        self.potrava.append(Potrava(event.x - Kor._x0, Kor._y0 - event.y))

    def timer(self):
        Kor.g.delete('all')
        Akvarium().vykresli_akvarium()

        for rybka in self.rybky:
            rybka.k = Kor(rybka.x, rybka.y)
            # logika ked je rybka k potrave blizko
            if rybka.konkretna_potrava is None:
                for potrava in self.potrava:
                    potrava.k = Kor(potrava.x, potrava.y)
                    rybka.vzdialenost = rybka.k.distance(potrava.x, potrava.y)
                    if rybka.vzdialenost < 150:
                        rybka.konkretna_potrava = potrava
                        break
            else:
                # logika pohybu rybky k potrave 
                rybka.vzdialenost = rybka.k.distance(rybka.konkretna_potrava.x,  rybka.konkretna_potrava.y)
                if rybka.vzdialenost < 150:
                    if rybka.x > rybka.konkretna_potrava.x and rybka.y > rybka.konkretna_potrava.y:
                        if rybka.konkretna_potrava.x -30 < rybka.x < rybka.konkretna_potrava.x +30:
                            rybka.y += -7
                        else:
                            if rybka.krokX > 0:
                                rybka.krokX = -6
                            rybka.y += -7
                    if rybka.x > rybka.konkretna_potrava.x and rybka.y < rybka.konkretna_potrava.y:
                        if rybka.konkretna_potrava.x -30 < rybka.x < rybka.konkretna_potrava.x +30:
                            rybka.y += 2
                        else:
                            if rybka.krokX > 0:
                                rybka.krokX = -6
                            rybka.y += 2
                    if rybka.x < rybka.konkretna_potrava.x and rybka.y > rybka.konkretna_potrava.y:
                        if rybka.konkretna_potrava.x -30 < rybka.x < rybka.konkretna_potrava.x +30:
                            rybka.y += -7
                        else:
                            if rybka.krokX < 0:
                                rybka.krokX = 6
                            rybka.y += -7
                    if rybka.x < rybka.konkretna_potrava.x and rybka.y < rybka.konkretna_potrava.y:
                        if rybka.konkretna_potrava.x -30 < rybka.x < rybka.konkretna_potrava.x +30:
                            rybka.y += 2
                        else:
                            if rybka.krokX < 0:
                                rybka.krokX = 6
                            rybka.y += 2
                # rybka zje potravu ak suradnice su v rozsahu -6 +6, atributy sa zmenia na None
                if (rybka.x == rybka.konkretna_potrava.x or rybka.x == rybka.konkretna_potrava.x+1 or rybka.x == rybka.konkretna_potrava.x+2 or \
                rybka.x == rybka.konkretna_potrava.x-1 or rybka.x == rybka.konkretna_potrava.x-2 or rybka.x == rybka.konkretna_potrava.x+3 or \
                rybka.x == rybka.konkretna_potrava.x-3 or rybka.x == rybka.konkretna_potrava.x+4 or rybka.x == rybka.konkretna_potrava.x-4 or 
                rybka.x == rybka.konkretna_potrava.x-5 or rybka.x == rybka.konkretna_potrava.x+5 or rybka.x == rybka.konkretna_potrava.x+6 or rybka.x == rybka.konkretna_potrava.x-6) \
                and (rybka.y == rybka.konkretna_potrava.y or  rybka.y == rybka.konkretna_potrava.y+1 or rybka.y == rybka.konkretna_potrava.y-1 \
                or rybka.y == rybka.konkretna_potrava.y +2 or rybka.y == rybka.konkretna_potrava.y -2 or rybka.y == rybka.konkretna_potrava.y+3 \
                or rybka.y == rybka.konkretna_potrava.y-3 or rybka.y == rybka.konkretna_potrava.y -4 or rybka.y == rybka.konkretna_potrava.y +4 or \
                rybka.y == rybka.konkretna_potrava.y -5 or rybka.y == rybka.konkretna_potrava.y +5 or rybka.y == rybka.konkretna_potrava.y+6 or rybka.y == rybka.konkretna_potrava.y-6):
                    if rybka.zivot < 200:
                        rybka.zivot += 50
                    if rybka.konkretna_potrava in self.potrava:
                        self.potrava.remove(rybka.konkretna_potrava)
                    rybka.konkretna_potrava = None
                    rybka.vzdialenost = None
                    rybka.krokX = random.choice([-4,-2, 2, 4])

        # logika otacania rybky pri krajoch akvaria a nahodne otocenie
            if rybka.counter%200 == 0:
                if rybka.konkretna_potrava is None:
                    rybka.krokX *= -1
                    rybka.krokY = random.choice([-1,-2,0,1,2])
            if rybka.x > 245:
                rybka.x += -5
                rybka.krokX *= -1
                rybka.krokY = random.choice([0,1,-1,2,-2])
            if rybka.x < -245:
                rybka.x += 5
                rybka.krokX *= -1
                rybka.krokY = random.choice([0,1,-1,2,-2])
            if rybka.y < -265:
                rybka.y += 10
                rybka.krokY *= -1
            if rybka.y > 265:
                rybka.krokY *= -1
            if rybka.zivot==0:
                self.rybky.remove(rybka)

            rybka.x += rybka.krokX
            rybka.y += rybka.krokY 
            # vykreslenie rybky podla smeru plavania            
            if rybka.krokX < 0:
                rybka.kresli_rybku_vlavo()
            else:
                rybka.kresli_rybku_vpravo()
            rybka.counter += 1
            rybka.zivot -= 0.5
        # vykreslenie potravy           
        for potrava in self.potrava:
            potrava.y += potrava.krok
            if potrava.y < -265:
                self.potrava.remove(potrava)
            potrava.k = Kor(potrava.x, potrava.y)
            potrava.vykresli_potravu()

        Kor.g.after(100, self.timer)

Program()