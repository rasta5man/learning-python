'''
Zadanie:
Program si vypyta pocet hodin a minut.
Potom vykresli dvoje hodiny. Ked kliknete SPACE, spusti sa odpocet prvych, druhe stoja.
Ked kliknete opat SPACE, prve sa zastavia a zacne sa odpocet druhych. Ked odpocet niektorych hodin
dojde po nulu, program vypise 'CAS VYPRSAL'. Program konci a space uz dalej nefunguje
'''

import tkinter

hod = int(input('zadaj pocet hodin: '))
minu = int(input('zadaj pocet minut: '))

class Hodiny:
    #triedne atributy
    pole=[]                         #obe hodiny pridam do pola
    i = 0                           #i sa zvacsuje a modulo vzdy ukazuje na jedny a potom druhe 

    def __init__(self, hodiny, minuty, sekundy=0):
        self.cas = 3600*hodiny + 60*minuty + sekundy
        self.bezi = None            #zapina a vypina casovac
        self.canvas = tkinter.Canvas(width =400, height = 250)
        self.canvas.pack()
        self.id = self.canvas.create_text(200,150, text = self, font = 'arial 30')
        
    def __str__(self):
        return '{}:{:02}:{:02}'.format(self.cas//3600, self.cas//60%60, self.cas%60)

    def nazov(self):
        self.canvas.create_text(200, 30, text = 'Sachove hodiny', font='arial 40', fill = 'blue')
   
    def aktivuj(self):              
        self.canvas.bind_all('<space>', self.startCasovaca)

    def startCasovaca(self, event):
        self.bezi = True
        self.canvas.unbind_all('<space>')
        Hodiny.i += 1
        Hodiny.pole[Hodiny.i%2].bezi = False
        Hodiny.pole[Hodiny.i%2].canvas.bind_all('<space>', Hodiny.pole[Hodiny.i%2].startCasovaca)
        self.casovac()
        
    def casovac(self):
        if self.bezi:
            if self.cas == 0:
                self.canvas.create_text(200, 200, text = 'Cas vyprsal', font='arial, 50', fill = 'red')
                self.bezi = False
                Hodiny.pole[Hodiny.i%2].bezi = False
                Hodiny.pole[Hodiny.i%2].canvas.unbind_all('<space>')
            else:
                self.cas -= 1
                self.canvas.itemconfig(self.id, text = self)
                self.canvas.after(998, self.casovac)

hod1 = Hodiny(hod,minu)
hod2 = Hodiny(hod,minu)
hod1.nazov()                        #vypise nazov iba na prvej ploche

Hodiny.pole=[hod1,hod2] 
hod1.aktivuj()                      # aktivuje zviazanie SPACE s funkciou startCasovaca
