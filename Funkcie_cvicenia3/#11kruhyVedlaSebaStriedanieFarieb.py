#11
'''
funkcia kruhy(n) nakreslí vedľa seba do jedného radu n kruhov s polomerom 20, pričom sa striedajú tri farby: červená, modrá, žltá

    >>> obrázok <<<

        funkcia nevracia žiadnu hodnotu (neobsahuje return), len niečo kreslí pomocou tkinter, možno využijete funkciu farba(ix) z 5. prednášky
        funkciu otestujte s rôznymi parametrami, napr. kruhy(5), kruhy(6), kruhy(7), kruhy(8), ... 
'''
import tkinter, random
canvas = tkinter.Canvas(width=1400, height=200)
canvas.pack()
def kruhy(n):
    canvas.delete('all')
    x, y, r = 40, 150, 20
    farba1, farba2, farba3 = 'red', 'blue', 'yellow'
    for i in range(n):
        canvas.create_oval(x-r, y-r, x+r, y+r, fill = farba1)
        x +=42
        farba1, farba2, farba3 = farba2, farba3, farba1