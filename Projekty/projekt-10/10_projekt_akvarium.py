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
        self.krokX = random.choice([-10,-7, -4, 4, 7, 10])
        self.krokY = random.choice([-2,-1,0,1,2])
        self.k = None
        self.counter = random.randrange(50)
        self.zivot = 20
        
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
 
class Potrava():
    def __init__(self, x, y):
        self.x, self.y = x, y
        self.k = None
        self.krok = random.choice([-2,-3,-4])

            
    def vykresli_potravu(self):
        self.k._pw = random.choice([2,3,4])
        self.k.ht()
        for i in range(3):
            self.k.fd(5)
            self.k.rt(120)

class Program:
    
    def __init__(self):
        bgcolor('white')
        self.rybky=[]
        self.potrava=[]
        Akvarium().vykresli_akvarium()
        Kor.g.bind('<Button-3>', self.pridaj_rybku)
        Kor.g.bind('<Button-1>', self.pridaj_potravu)
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
            if rybka.counter%100 == 0:
                rybka.krokX *= -1
                rybka.krokY = random.choice([-1,-2,-3,0,1,2,3])
            if rybka.x > 248:
                rybka.krokX *= -1
            if rybka.x < -248:
                rybka.krokX *= -1
                rybka.krokY = random.choice([0,1,-1,2,-2,3,-3])
            if rybka.y > -260:
                rybka.krokY *= -1
            if rybka.y < 260:
                rybka.krokY *= -1
            rybka.x += rybka.krokX
            rybka.y += rybka.krokY 
            rybka.k = Kor(rybka.x, rybka.y)
            if rybka.krokX < 0:
                rybka.kresli_rybku_vlavo()
            else:
                rybka.kresli_rybku_vpravo()
            rybka.counter += 1
        for potrava in self.potrava:
            potrava.y += potrava.krok
            if potrava.y < -275:
                self.potrava.remove(potrava)
            potrava.k = Kor(potrava.x, potrava.y)
            potrava.vykresli_potravu()
        Kor.g.after(100, self.timer)

Program()