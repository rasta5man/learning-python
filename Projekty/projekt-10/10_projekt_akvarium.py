from kor import *
import random

class Rybka():
    def __init__(self, x, y):
        self.x, self.y = x, y
        self.krok = random.choice([-10,-7, -4, 4, 7, 10])
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
 
class Potrava():
    def __init__(self, x, y):
        pass

    def pohni(self):
        pass

class Program:
    
    def __init__(self):
        bgcolor('white')
        self.rybky=[]
        Kor.g.bind('<Button-1>', self.pridaj_rybku)
        self.timer()
        Kor.g.mainloop()
    
    def pridaj_rybku(self, event):
        self.rybky.append(Rybka(event.x - Kor._x0, Kor._y0 - event.y))
    
    def timer(self):
        Kor.g.delete('all')
        for rybka in self.rybky:
            if rybka.counter%100 == 0:
                rybka.krok *= -1
            if rybka.x > 250:
                rybka.krok *= -1
            if rybka.x < -250:
                rybka.krok *= -1
            rybka.x += rybka.krok
            rybka.k = Kor(rybka.x, rybka.y)
            if rybka.krok < 0:
                rybka.kresli_rybku_vlavo()
            else:
                rybka.kresli_rybku_vpravo()
            rybka.counter += 1
        Kor.g.after(100, self.timer)

Program()

def main():
    pass