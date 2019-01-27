import tkinter

vyska = 50

class Utvar:

    def __init__(self, x, y):
        self.canvas = canvas
        self.r = vyska
        self.x = x
        self.y = y
        
    def posun(self, dx, dy):
        self.x += dx
        self.y += dy
        self.canvas.move(self.id, dx, dy)

class Stvorec(Utvar):

    def __init__(self, x, y):
        super().__init__(x, y)
        self.id = self.canvas.create_rectangle(self.x,self.y,self.x +self.r,self.y+self.r, fill = 'red')
        
    def je_klik(self, x, y):
        if self.x<=x<self.x+self.r and self.y<=y<self.y+self.r:
            return True

class Kruh(Utvar):

    def __init__(self, x, y):
        super().__init__(x,y)
        self.id = canvas.create_oval(self.x-self.r/2, self.y-self.r/2, self.x+self.r/2, self.y+self.r/2, fill = 'blue')

    def je_klik(self, x, y):
        return (self.x-x)**2 +(self.y -y)**2 < (self.r/2)**2

        
class Program:

    def __init__(self):
        self.canvas = canvas
        self.canvas.bind('<Button-1>', self.on_klik)
        self.zoznam = []

    def na_co_klikam(self, event):
        ix = len(self.zoznam)-1
        while ix >= 0 and not self.zoznam[ix].je_klik(event.x, event.y):
            ix -= 1
        if ix < 0:
            return None
        else:
            return self.zoznam[ix]
        
    def on_klik(self, event):
        self.utvar = self.na_co_klikam(event)
        if self.utvar == None:
            return
        self.x0, self.y0 = event.x, event.y
        #if utvar.je_klik(event.x, event.y):
        self.canvas.bind('<B1-Motion>', self.udalost_pohyb)
        self.canvas.bind('<ButtonRelease-1>', self.udalost_pusti)

    def udalost_pohyb(self, event):
        self.utvar.posun(event.x - self.x0, event.y - self.y0)
        self.x0, self.y0 = event.x, event.y

    def udalost_pusti(self, event):
        self.canvas.unbind('<B1-Motion>')
        self.canvas.unbind('<ButtonRelease-1>')
        

canvas = tkinter.Canvas(width = 500, height= 500)
canvas.pack()

stv1 = Stvorec(50,50)
k1  = Kruh(150,150) 

p = Program()
p.zoznam.append(stv1)
p.zoznam.append(k1)


'''
import tkinter
canvas = tkinter.Canvas()
canvas.pack()

x,y = 50,50
stv = canvas.create_rectangle(x,y,x+50,y+50, fill='red', outline='red')
x0,y0 = 0,0

def udalost_tahaj_start(event):
    global x0, y0
    x0, y0 = event.x, event.y
    if x<=x0<x+50 and y<=y0<y+50:
        canvas.bind('<B1-Motion>', udalost_tahaj)
        canvas.bind('<ButtonRelease-1>', udalost_pusti)
        
def posun(dx, dy):
    global x,y
    x += dx
    y += dy
    canvas.move(stv, dx, dy)

def udalost_tahaj(event):
    global x0,y0
    posun(event.x-x0, event.y-y0)
    x0, y0 = event.x, event.y

def udalost_pusti(event):
    canvas.unbind('<B1-Motion>')
    canvas.unbind('<ButtonRelease-1>')

canvas.bind('<Button-1>', udalost_tahaj_start)


##############################################################
# U L O H A    8
# v tomto kode ostane kopia stvorca tam kde ho premiestnim a povosny stvorec sa vrati na povodne miesto
import tkinter
canvas = tkinter.Canvas()
canvas.pack()

x,y = 50,50
stv = canvas.create_rectangle(x,y,x+50,y+50, fill='red', outline='red')
x0,y0 = 0,0

def udalost_tahaj_start(event):
    global x0, y0
    x0, y0 = event.x, event.y
    if x<=x0<x+50 and y<=y0<y+50:
        canvas.bind('<B1-Motion>', udalost_tahaj)
        canvas.bind('<ButtonRelease-1>', udalost_pusti)
        
def posun(dx, dy):
    global x,y
    x += dx
    y += dy
    canvas.move(stv, dx, dy)

def udalost_tahaj(event):
    
    global x0,y0
    posun(event.x-x0, event.y-y0)
    x0, y0 = event.x, event.y

def udalost_pusti(event):
    global x, y
    canvas.create_rectangle(x, y, x+50, y+50, fill='red', outline ='red')
    x, y = 50,50
    canvas.coords(stv, x, y, x+50, y+50)
    canvas.unbind('<B1-Motion>')
    canvas.unbind('<ButtonRelease-1>')

canvas.bind('<Button-1>', udalost_tahaj_start)

'''

