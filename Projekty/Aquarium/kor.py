#
# kor.py: zjednodusena verzia modulu turtle.py - korytnacia grafika vychadza z tkinter
# Version 4.12.2013
#

import tkinter, math

class Kor:
    g = None
    gwidth = 600
    gheight = 600
    
    def __init__(self, x=0, y=0, h=0):
        self._init()
        self._home = (x, y, h)
        self._id = None          # id pre tvar korytnacky
        self._attr()             # inicializuj vsetky atributy

    def _attr(self):
        self._x, self._y, self._h = self._home
        self._pc = 'black'       # farba pera
        self._fc = 'black'       # farba vyplne (pre fill)
        self._pw = 1             # hrubka pera
        self._down = True        # ci je pero dole
        self._pole = []          # pole id vsetkych nakreslenych objektov (pre clear a reset)
        self._fill = False       # ci je zapnute begin_fill
        self._poly = []          # pole canvas-suradnic pre end_fill
        self._shown = True       # ci je zobrazena alebo skryta
        self._kresli()           # prekresli tvar korytnacky

    def _init(self):             # inicializacia grafickej plochy
        if Kor.g is None:
            Kor.g = tkinter.Canvas(bg='white', width=Kor.gwidth, height=Kor.gheight)
            Kor.g.pack()
            Kor._x0 = Kor.gwidth//2       # x-suradnica (0,0) v canvase
            Kor._y0 = Kor.gheight//2      # y-suradnica (0,0) v canvase

    def _pos(self, x=None, y=None):   # interna metoda na prevod kor-suradnic na canvas-suradnice
        if x is None:
            x, y = self._x, self._y
        return (x + self._x0, self._y0 - y)
    
    def _kresli(self):           # interna metoda kresli tvar korytnacky
        if self._id is not None:
            self.g.delete(self._id)
            self._id = None
        if self._shown:
            x1, y1 = self._pos()
            x2, y2 = self._pos(self._x+5*math.cos(math.radians(self._h+180)), self._y+5*math.sin(math.radians(self._h+180)))
            self._id = self.g.create_line(x2,y2,x1,y1,arrow='last')
        
    def _append_poly(self):      # interna metoda pre ulozenie suradnic pre fill
        self._poly.append(self._pos())

    def __del__(self):
        if self._id is not None:
            self.g.delete(self._id)
        #self.clear()

    def __repr__(self):
        return 'Kor({:.2f},{:.2f},{:.2f})'.format(self._x, self._y, self._h).replace('.00','')

    #------------------------------------------------------------------------

    def rt(self, uhol):
        self.seth(self._h - uhol)

    def lt(self, uhol):
        self.seth(self._h + uhol)

    def seth(self, uhol):
        self._h = uhol%360
        self._kresli()

    def heading(self):
        return self._h

    def towards(self, x, y=None):
        if y is None:
            x, y = x
        x, y = x - self._x, y - self._y
        return math.degrees(math.atan2(y, x)) % 360.0

    right = rt
    left = lt
    setheading = seth

    #------------------------------------------------------------------------
    
    def fd(self, dlzka):
        self.setpos(self._x + math.cos(math.radians(self._h)) * dlzka,
                    self._y + math.sin(math.radians(self._h)) * dlzka)

    def bk(self, dlzka):
        self.fd(-dlzka)

    def setpos(self, x, y=None):
        if y is None:
            x, y = x
        if self._down:
            self._pole.append(self.g.create_line(self._pos(), self._pos(x, y),
                                                 width=self._pw,fill=self._pc,
                                                 capstyle='round'))
        self.movepos(x, y)

    def movepos(self, x, y=None):
        if y is None:
            x, y = x
        self._x, self._y = x, y
        self._append_poly()
        self._kresli()

    def pos(self):
        return (self._x, self._y)

    def xcor(self):
        return self._x

    def ycor(self):
        return self._y

    def home(self):
        self.setpos(self._home[:2])
        self._h = self._home[2]
        self._kresli()

    def dot(self, velkost=None, farba=None):
        if velkost is None:
            velkost = self._pw
        if farba is None:
            farba = self._pc
        velkost /= 2
        x, y = self._pos()
        self._pole.append(self.g.create_oval(x-velkost,y-velkost,x+velkost,y+velkost,
                                             outline=farba,fill=farba))
        self._kresli()

    def distance(self, x, y=None):
        if y is None:
            x, y = x
        return math.sqrt((self._x-x)**2+(self._y-y)**2)

    forward = fd
    back = bk
    position = pos
    setposition = setpos

    #------------------------------------------------------------------------
    
    def pu(self):
        self._down = False

    def pd(self):
        self._down = True

    def pencolor(self, farba=None):
        if farba is None:
            return self._pc
        else:
            self._pc = farba

    def fillcolor(self, farba=None):
        if farba is None:
            return self._fc
        else:
            self._fc = farba

    def pensize(self, pw=None):
        if pw is None:
            return self._pw
        else:
            self._pw = pw

    def st(self):
        self._shown = True
        
    def ht(self):
        self._shown = False
        
    penup = up = pu
    pendown = down = pd
    width = pensize
    showturtle = st
    hideturtle = ht

    #------------------------------------------------------------------------
    
    def begin_fill(self):
        self._fill = True
        self._poly = []
        self._append_poly()

    def end_fill(self):
        if self._fill:
            self._pole.append(
                self.g.create_polygon(self._poly, fill=self._fc,
                                      outline=self._pc, width=self._pw))
        self._fill = False
        self._poly = []

    #------------------------------------------------------------------------

    def clear(self):
        for i in self._pole:
            self.g.delete(i)
        self._pole = []

    def reset(self):
        self.clear()
        self._attr()


#-------------------------------------------------------

def bgcolor(farba):
    '''nastav farbu garfickej plochy'''
    Kor._init(Kor)
    Kor.g['bg'] = farba

def wait(ms):
    '''zastav vypocet na ms milisekund'''
    Kor._init(Kor)
    Kor.g.update()
    Kor.g.after(ms)

#-------------------------------------------------------

import random

def ni(a, b):
    '''nahodny interval'''
    return random.randint(a, b)

def nf():
    '''nahodna farba'''
    return '#{:06x}'.format(random.randrange(16777216))

#-------------------------------------------------------

if __name__ == "__main__":
    Kor().dot(100, 'red')