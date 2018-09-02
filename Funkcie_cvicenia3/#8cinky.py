''' 
#8
Napíšte dve funkcie: najprv funkciu kruh(r, x, y), ktorá nakreslí čierny kruh s polomerom r a so stredom (x,y). Potom funkciu cinky(x, y), ktorá nakreslí činky, t.j. dva čierne kruhy s priemerom 50, medzi ktorými je hrubá čierna tyč, kruhy sú navzájom vzdialené 50 a stred tyče má súradnice (x, y). Na kreslenie kruhov musíte použiť vašu funkciu kruh(...)

        funkcia nevracia žiadnu hodnotu (neobsahuje return), len niečo kreslí pomocou tkinter
        funkciu otestujte s rôznymi parametrami, napr. cinky(150, 100), ... 
'''
def kruh(r, x, y):
    canvas.create_oval(x-r, y-r, x+r, y+r, fill ='black')
def cinky(x,y):
    r = 25
    canvas.create_line(x-25+50, y, x+25+50, y, width = 7)
    kruh(25, x, y)
    kruh(25, x+100, y)
import tkinter
canvas = tkinter.Canvas()
canvas.pack()
cinky(150,100)