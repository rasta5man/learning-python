#13 Program najprv prečíta číslo - veľkosť polomeru kruhu a potom vedľa seba vykreslí 10 kruhov v jednom rade so zadanou veľkosťou strany, pričom sa kruhy nedotýkajú, ale majú rozostupy 10. 
import tkinter
canvas = tkinter.Canvas()
canvas.pack()
r = int(input('zadaj polomer: '))
x, y = 10, 100
for i in range(10):
    canvas.create_oval(x, y, x+r, y+r, fill = 'red')
    x = x+r+10