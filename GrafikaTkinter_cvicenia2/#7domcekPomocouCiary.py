#7*. Pomocou jednej lomenej čiary (create_line) nakreslite domček (štvorec s oboma uhlopriečkami a trojuholníkovou strechou) jedným ťahom.
#    mohlo by vám pomôcť, ak si najprv do piatich premenných priradíte súradnice piatich vrcholov domčeka a pomocou nich zavoláte kreslenie lomenej čiary (napr. a=(50,100),...)
import tkinter
p = tkinter.Canvas(width=600, height = 600)
p.pack()
a = (300, 50)
b = 200, 200
c = 400, 200
d = 200, 400
e = 400, 400
p.create_line(e, c, b, e, d, c, a, b, d, fill = 'blue', tag = 'd')
p.mainloop()