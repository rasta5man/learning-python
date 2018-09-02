#9
'''
funkcia vypisuj(n) na náhodnú pozíciu v grafickej ploche vypíše n textov: červeným písmom PYTHON alebo modrým PASCAL - tieto texty sa budú objavovať s rovnakou pravdepodobnosťou, napr. vypisuj(100) vypíše približne 50x PYTHON a 50x PASCAL

    >>> obrázok <<<

        funkcia nevracia žiadnu hodnotu (neobsahuje return), len niečo kreslí pomocou tkinter
        funkciu otestujte s rôznymi parametrami, napr. vypisuj(10), vypisuj(100), ... 
'''
import random, tkinter
canvas = tkinter.Canvas()
canvas.pack()
def vypisuj(n):
    for i in range(n):
        if random.randrange(2):
            canvas.create_text(random.randrange(380), random.randrange(250), text = 'PYTHON', fill = 'red')
        else:
            canvas.create_text(random.randrange(380), random.randrange(250), text = 'Pascal', fill = 'blue')