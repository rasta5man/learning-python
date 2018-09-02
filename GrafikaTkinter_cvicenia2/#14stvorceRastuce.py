#14 Program nakreslí vedľa seba 10 štvorcov, ktoré sa navzájom dotýkajú stranou, ich spodná strana leží na jednej priamke a ich veľkosti sa postupne zväčšujú: 15, 20, 25, 30, 35, ... 
import tkinter
canvas = tkinter.Canvas()
canvas.pack()
x, y, s = 10, 100, 15
for i in range(10):
    canvas.create_rectangle(x, y-s, x+s, y)
    x=x+s
    s = s+5