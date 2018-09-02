#2*. Nakreslite mesiac na tmavomodrej ('navy') oblohe: kreslite ho ako dva prekrývajúce sa kruhy, pričom prvý bude žltý a druhý tmavomodrý
import tkinter
canvas = tkinter.Canvas(bg='navy')
canvas.pack()
x, y, x1, r = 70, 70, 20, 30
canvas.create_oval(x-r, y-r, x+r, y+r, outline ='yellow', fill='yellow')
canvas.create_oval(x+x1-r, y-r, x+x1+r, y+r, outline = 'navy', fill='navy')