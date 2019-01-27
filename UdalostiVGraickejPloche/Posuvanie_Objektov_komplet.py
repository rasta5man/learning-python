import tkinter, random

class Kruh:

    def __init__(self, x, y, r, farba='red'):
        self.x = x
        self.y = y
        self.r = r
        self.farba = farba
        self.id = None
        self.typ = 'kruh'

    def kresli(self, g):
        self.g = g
        if self.id != None:
            self.g.delete(self.id)
        self.id = self.g.create_oval(self.x-self.r,self.y-self.r,
                      self.x+self.r,self.y+self.r,
                      fill=self.farba)

    def posun(self, dx=0, dy=0):
        self.x += dx
        self.y += dy
        self.kresli(self.g)

    def zmen(self, r):
        self.r = r
        self.kresli(self.g)

    def zmen_farbu(self, farba):
        self.farba = farba
        self.kresli(self.g)
        
    def je_klik(self, x, y):
        return (self.x-x)**2+(self.y-y)**2 < self.r**2

class Obdlznik:

    def __init__(self, x, y, sirka, vyska, farba='red'):
        self.x = x
        self.y = y
        self.sirka = sirka
        self.vyska = vyska
        self.farba = farba
        self.id = None
        self.typ = 'obdlznik'

    def kresli(self, g):
        self.g = g
        if self.id != None:
            self.g.delete(self.id)
        self.id = self.g.create_rectangle(self.x,self.y,
                      self.x+self.sirka,self.y+self.vyska,
                      fill=self.farba)

    def posun(self, dx=0, dy=0):
        self.x += dx
        self.y += dy
        self.g.move(self.id, dx, dy)

    def zmen(self, sirka, vyska):
        self.sirka = sirka
        self.vyska = vyska
        self.g.coords(self.id, self.x,self.y,
                      self.x+self.sirka,self.y+self.vyska)

    def zmen_farbu(self, farba):
        self.farba = farba
        self.g.itemconfig(self.id, fill=farba)

    def je_klik(self, x, y):
        return self.x<=x<self.x+self.sirka and self.y<=y<self.y+self.vyska

class Program:
    def __init__(self):
        self.pole = []
        self.g = tkinter.Canvas(bg='white', width=600, height=600)
        self.g.pack()
        for i in range(20):
            if random.randrange(2) == 0:
                self.pridaj(Kruh(random.randint(50, 550),random.randint(50, 550), 30, 'blue'))
            else:
                self.pridaj(Obdlznik(random.randint(50, 550),random.randint(50, 550), 40, 40))

        self.g.bind('<Button-3>', self.udalost_pravy_klik)
        self.g.bind('<Button-1>', self.udalost_tahaj_start)
        
    def udalost_pravy_klik(self, e):
        if random.randrange(2) == 0:
            self.pridaj(Kruh(e.x, e.y, 50, nahodna_farba()))
        else:
            self.pridaj(Obdlznik(e.x, e.y, 50, 50, nahodna_farba()))

    def kto(self, e):
        ix = len(self.pole)-1
        while ix >= 0 and not self.pole[ix].je_klik(e.x, e.y):
            ix -= 1
        if ix < 0:
            return None
        else:
            return self.pole[ix]

    def udalost_tahaj_start(self, e):
        self.utvar = self.kto(e)
        if self.utvar == None:
            return
        self.ex, self.ey = e.x, e.y
        self.g.bind('<B1-Motion>', self.udalost_tahaj)
        self.g.bind('<ButtonRelease-1>', self.udalost_pusti)

    def udalost_tahaj(self, e):
        self.utvar.posun(e.x-self.ex, e.y-self.ey)
        self.ex, self.ey = e.x, e.y

    def udalost_pusti(self, e):
        self.g.unbind('<B1-Motion>')
        self.g.unbind('<ButtonRelease-1>')
        self.utvar = None
            
    def pridaj(self, utvar):
        self.pole.append(utvar)
        utvar.kresli(self.g)

def nahodna_farba():
    r = random.randrange(256)
    g = random.randrange(256)
    b = random.randrange(256)
    return '#{:02x}{:02x}{:02x}'.format(r,g,b)

Program()
