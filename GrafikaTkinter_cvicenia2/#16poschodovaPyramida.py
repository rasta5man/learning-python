#16 Nakreslite n-poschodovú pyramídu (n prečítajte zo vstupu): každé poschodie tvorí obdĺžnik s výškou 20 a s vodorovnou stranou postupne 20, 40, 60, ... Tieto obdĺžniky sú vycentrované. 
import tkinter
canvas = tkinter.Canvas()
canvas.pack()
pocet = int(input('zadaj pocet: '))
x, y, v, s = 200, 20, 20, 20
for i in range(pocet):
    canvas.create_rectangle(x - s/2, y, x + s/2, y+v, fill = 'pink')
    s = s+20
    y = y+v
canvas.mainloop()