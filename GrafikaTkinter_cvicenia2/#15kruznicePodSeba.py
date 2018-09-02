#15 nakreslite pod seba 5 postupne sa zväčšujúcich kružníc, pričom ich stredy ležia na priamke rovnobežnej s y-ovou osou. Polomery kružníc môžu byť napr. 10, 20, 30, 40, 50.
#15 - dalo mi to dost skusania
import tkinter
canvas = tkinter.Canvas(height = 500, width =500)
canvas.pack()
x, y, r = 100, 20, 10
for i in range(7):
    canvas.create_oval(x-r, y-r, x+r, y+r)
    y = 2*r +y +10
    r += 10
canvas.mainloop()