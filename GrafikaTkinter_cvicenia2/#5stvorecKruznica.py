#5*. Program si najprv vypýta (input) číslo a potom nakreslí štvorec so stranou tejto veľkosti a k nemu nakreslí kružnicu opísanú.

strana = int(input('zadaj dlzku strany: '))
a = strana/2
import tkinter
p = tkinter.Canvas(width=500, height=500)
p.pack()
r = (a**2 + a**2)**.5
p.create_rectangle(200-a, 200-a, 200+a, 200+a)
p.create_oval(200-r, 200-r, 200+r, 200+r)