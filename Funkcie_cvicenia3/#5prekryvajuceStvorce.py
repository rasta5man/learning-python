#5 funkcia stvorce(n) nakresli n štvorcov so stranou 40, pričom sa tieto štvorce musia prekrývať - každý ďalší je posunutý trochu v pravo a dole 
def stvorce(n):
    import tkinter
    canvas = tkinter.Canvas()
    canvas.pack()
    x, y, a= 10, 10, 40
    for i in range(n):
        canvas.create_rectangle(x, y, x+a, y+a)
        x += 35
        y += 10