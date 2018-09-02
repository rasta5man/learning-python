#10 - moje riesenie = funguje pre cele cisla delitelne 10
'''
funkcia krabica(v) nakreslí štvorec veľkosti v x v, do ktorého naukladá čo najviac štvorčekov veľkosti 10x10 - štvorčeky z veľkého štvorca nesmú 
trčať (môžete ich vyfarbiť náhodnými farbami)

    >>> obrázok <<<

        funkcia nevracia žiadnu hodnotu (neobsahuje return), len niečo kreslí pomocou tkinter
        funkciu otestujte s rôznymi parametrami, napr. krabica(40), krabica(55), ... 
'''
import tkinter, random
canvas = tkinter.Canvas(width = 400, height = 400)
canvas.pack()

def krabica(v):
    canvas.delete('all')
    x, y = 200, 200
    r = v/2
    x = 200-r
    y = 200-r
    canvas.create_rectangle(x, y, 200+r, 200+r)
    for i in range(v//10):
        for j in range(v//10):
            farba = f'#{random.randrange(256**3):06x}'
            canvas.create_rectangle(x, y, x+10, y+10, fill = farba)
            x = x+10
        y = y + 10
        x = x - v

#10 - riesenie z cviceni, funguje pre hocijake cisla

def nahodna_farba():
    return '#{:06x}'.format(random.randrange(256*256*256))

def krabica(v):
    x,y = 100,150
    g.create_rectangle(x-1, y+1, x+v+1, y-v-1, fill='gray95', outline='gray77')
    for xx in range(x, x+v-9, 10):
        for yy in range(y, y-v+9, -10):
            g.create_rectangle(xx, yy, xx+10, yy-10, fill=nahodna_farba())

import tkinter, random
g = tkinter.Canvas(bg='white')
g.pack()
krabica(55)