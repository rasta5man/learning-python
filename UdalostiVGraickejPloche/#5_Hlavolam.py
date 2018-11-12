'''
Zadanie
V zozname máme čísla 0 až n v náhodnom poradí

        napr. zoznam = [3, 0, 1, 2]

Tento zoznam reprezentuje takýto hlavolam:
máme n+1 políčok (štvorčekov) v každom okrem jedného je číslo od 1 do n.
Políčko s 0 vykreslíme ako prázdne ostatné so zodpovedajúcim číslom v strede.
Kliknutie do jedného zo štvorčekov s číslom presťahuje toto číslo na voľné
políčko (zároveň v zozname vymení 0 a toto kliknuté číslo).
Cieľom riešenia hlavolamu je preusporiadať čísla tak aby v prvých n políčkach
boli postupne čísla 1 až n a posledné políčko ostalo prázdne:
vtedy program vypíše ‚HURA‘.
'''

#5 - F U N G U J E - paradaaaa spravil som sam
import tkinter, random
canvas = tkinter.Canvas(width=500)
canvas.pack()

a = range(6)
zoznam = random.sample(a, len(a))

x = y = s = 50
for i in range(len(zoznam)):
    canvas.create_rectangle(x,y,x+s,y+s)
    x += 50

x=50

for i in range(len(zoznam)):
    if zoznam[i]:
        canvas.create_text(x+25, y+25, text = zoznam[i], font='arial 20 bold', tag = 'a'+ str(i))
    else:
        canvas.create_text(x+25, y+25, text = '', tag = 'a'+ str(i))
    x += 50

x=50
def vymen(event):
    z = w = 50
    global zoznam
    pomocnyZoznam = list(zoznam)
    x, y = event.x, event.y
    if y > 50 and y<100 and x>50 and x<100:
        if zoznam[0] != 0:
            nula = zoznam.index(0)
            pomocnyZoznam[0] = zoznam[nula]
            pomocnyZoznam[nula] = zoznam[0]
            zoznam=list(pomocnyZoznam)
            for i in range(len(zoznam)):
                canvas.delete('a'+ str(i))
            for i in range(len(zoznam)):
                if zoznam[i]:
                    canvas.create_text(z+25, w+25, text = zoznam[i], font='arial 20 bold', tag = 'a'+ str(i))
                else:
                    canvas.create_text(z+25, w+25, text = '', tag = 'a'+ str(i))
                z += 50
    if y > 50 and y<100 and x>100 and x<150:
        if zoznam[1] != 0:
            nula = zoznam.index(0)
            pomocnyZoznam[1] = zoznam[nula]
            pomocnyZoznam[nula] = zoznam[1]
            zoznam=list(pomocnyZoznam)
            for i in range(len(zoznam)):
                canvas.delete('a'+ str(i))
            for i in range(len(zoznam)):
                if zoznam[i]:
                    canvas.create_text(z+25, w+25, text = zoznam[i], font='arial 20 bold', tag = 'a'+ str(i))
                else:
                    canvas.create_text(z+25, w+25, text = '', tag = 'a'+ str(i))
                z += 50
    if y > 50 and y<100 and x>150 and x<200:   
        if zoznam[2] != 0:
            nula = zoznam.index(0)
            pomocnyZoznam[2] = zoznam[nula]
            pomocnyZoznam[nula] = zoznam[2]
            zoznam=list(pomocnyZoznam)
            for i in range(len(zoznam)):
                canvas.delete('a'+ str(i))
            for i in range(len(zoznam)):
                if zoznam[i]:
                    canvas.create_text(z+25, w+25, text = zoznam[i], font='arial 20 bold', tag = 'a'+ str(i))
                else:
                    canvas.create_text(z+25, w+25, text = '', tag = 'a'+ str(i))
                z += 50
    if y > 50 and y<100 and x>200 and x<250:
        if zoznam[3] != 0:
            nula = zoznam.index(0)
            pomocnyZoznam[3] = zoznam[nula]
            pomocnyZoznam[nula] = zoznam[3]
            zoznam=list(pomocnyZoznam)
            for i in range(len(zoznam)):
                canvas.delete('a'+ str(i))
            for i in range(len(zoznam)):
                if zoznam[i]:
                    canvas.create_text(z+25, w+25, text = zoznam[i], font='arial 20 bold', tag = 'a'+ str(i))
                else:
                    canvas.create_text(z+25, w+25, text = '', tag = 'a'+ str(i))
                z += 50
    if y > 50 and y<100 and x>250 and x<300:
        if zoznam[4] != 0:
            nula = zoznam.index(0)
            pomocnyZoznam[4] = zoznam[nula]
            pomocnyZoznam[nula] = zoznam[4]
            zoznam=list(pomocnyZoznam)
            for i in range(len(zoznam)):
                canvas.delete('a'+ str(i))
            for i in range(len(zoznam)):
                if zoznam[i]:
                    canvas.create_text(z+25, w+25, text = zoznam[i], font='arial 20 bold', tag = 'a'+ str(i))
                else:
                    canvas.create_text(z+25, w+25, text = '', tag = 'a'+ str(i))
                z += 50
    if y > 50 and y<100 and x>300 and x<350:
        if zoznam[5] != 0:
            nula = zoznam.index(0)
            pomocnyZoznam[5] = zoznam[nula]
            pomocnyZoznam[nula] = zoznam[5]
            zoznam=list(pomocnyZoznam)
            for i in range(len(zoznam)):
                canvas.delete('a'+ str(i))
            for i in range(len(zoznam)):
                if zoznam[i]:
                    canvas.create_text(z+25, w+25, text = zoznam[i], font='arial 20 bold', tag = 'a'+ str(i))
                else:
                    canvas.create_text(z+25, w+25, text = '', tag = 'a'+ str(i))
                z += 50
    if zoznam == [1,2,3,4,5,0]:
        canvas.create_text(200,150, text = 'H U R A', font = 'arial 40 bold', fill = 'red')
        
canvas.bind('<Button-1>', vymen)
