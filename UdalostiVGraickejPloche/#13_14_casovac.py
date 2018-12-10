'''
V globálnej premennej farba = 'red' je nastavená nejaká farba, nastavte časovač, ktorý každú 0.05 sekundy vypíše na náhodnú pozíciu náhodné písmeno (od 'a' do 'z') s danou farbou (zvoľte 
vhodný font). Počas behu časovača, meňte nastavenú farbu a sledujte, čo sa robí
Do riešenia predchádzajúcej úlohy dorobte ďalší časovač, ktorý každých 5 sekúnd zmení obsah premennej farba na náhodnú farbu
porozmýšľajte aj o treťom časovači (napr. každých 8 sekúnd), ktorý zmení veľkosť vykresľovaných písmen na náhodné číslo od 10 do 30
'''


# riesenie s pouzitim triedy Program
####################################
import tkinter
from random import randrange as rr

class Program:

    def __init__(self):
        self.canvas = tkinter.Canvas(height = 400, width = 400)
        self.canvas.pack()
        self.farba = ''
        self.size = 0
        
    def casovac(self):
        self.canvas.delete('all')
        self.text = self.canvas.create_text(rr(30,370), rr(30,370), text = chr(rr(65,90)))
        self.canvas.itemconfig(self.text, fill = self.farba, font = ('arial' , self.size))
        self.canvas.after(400, self.casovac)
        
    def zmenaFarby(self):
        self.farba = '#{:06x}'.format(rr(0,256**3))
        self.canvas.after(5000, self.zmenaFarby)
        return self.farba

    def zmenaVelkosti(self):
        self.size = rr(30,90,20)
        self.canvas.after(5000, self.zmenaVelkosti)
        return self.size
        
new = Program()
new.zmenaFarby()
new.zmenaVelkosti()
new.casovac()





#riesenie s pouzitim triednych atributov##########################
############################################################
import tkinter
from random import randrange as rr

class Program:
    
    farba = ''
    size = 0
    canvas = None
           
    def casovac(self):
        self.canvas.delete('all')
        self.canvas.create_text(rr(30,370), rr(30,370), text = chr(rr(65,90)), fill= Program.farba, font =('arial', Program.size))
        self.canvas.after(400, self.casovac)
        
    def zmenaFarby(self):
        Program.farba = '#{:06x}'.format(rr(0,256**3))
        self.canvas.after(5000, self.zmenaFarby)
        return Program.farba

    def zmenaVelkosti(self):
        Program.size = rr(10,90,20)
        self.canvas.after(5000, self.zmenaVelkosti)
        return Program.size
     
        
Program.canvas = tkinter.Canvas(width=400, height=400)
Program.canvas.pack()

Program().zmenaFarby()
Program().zmenaVelkosti()
Program().casovac()
Program.canvas.mainloop()




#riesenie s pouzitim funkcii, bez tried ##########################
############################################################
import tkinter, random
canvas = tkinter.Canvas(height = 400, width = 400)
canvas.pack()
bezi = True
velkost = 0
farba = ''
text = canvas.create_text(0, 0, text ='')

def zmen():
    global farba
    farba = '#{:06x}'.format(random.randrange(256**3))
    canvas.after(5000, zmen)
    return farba

def zmenVelkost():
    global velkost
    velkost = random.randrange(20,80,20)
    canvas.after(5000, zmenVelkost)
    return velkost

def casovac():
    canvas.coords(text, random.randrange(30,370), random.randrange(30,370))
    canvas.itemconfig(text, text = chr(random.randrange(67,90)), fill = farba, font =('arial', velkost))
    if bezi:
        canvas.after(300, casovac)
    
casovac()
zmen()
zmenVelkost()