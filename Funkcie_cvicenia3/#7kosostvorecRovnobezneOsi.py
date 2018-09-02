#7 funkcia kosostvorec(x, y) nakreslí zelený kosoštvorec so stredom (x, y) a so stranou 50 - uhlopriečky kosoštvorca budú rovnobežné so súradnými osami 
import tkinter
canvas=tkinter.Canvas()
canvas.pack()
def kosostvorec(x,y):
    c = 50
    s = ((c**2)/2)**.5
    a = x-s, y
    b = x, y-s
    c = x+s, y
    d = x, y+s
    canvas.create_polygon(a,b,c,d,fill='green')