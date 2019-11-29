'''
Hra na hadanie nahodne vybranych slov. Zadavate pismena a ak sa pismeno v slove nenachadza, odvisnete.
Ak uhadnete, program vypise - Hura
'''


import tkinter, random
canvas = tkinter.Canvas()
canvas.pack()

canvas.create_text(180,20, text = 'Sibenica', font = 'arial 20', fill = 'blue')
o1 = canvas.create_rectangle(300, 20, 360, 50)
t1 = canvas.create_text(330, 35, text = 'Nova Hra' )
canvas.create_line(30,250,30,100, 100,100, 100, 120, width = 3, fill ='black')



slova = ['vyhoda','pondelok', 'hlava', 'klavesnica', 'uniforma', 'kytica', 'lupa' , 'hokejka', 'pero', 'pocitac', 'vetrovka', 'indian', 'kuzel', 'voda', 'kuchyna', 'serial', 'topanka', 'matematika']
slovo = random.choice(slova)

x, y, s = 20, 50, 30

for pismeno in slovo:
    pismeno = canvas.create_rectangle(x, y, x+s, y+s)
    x += s

def zaciatok_hry(event):
    t,z = event.x, event.y
    if 300<=t<=370 and 20<=z<=50:
        canvas.delete(o1,t1)
        canvas.unbind('<Button-1>')
        canvas.update()
        sibenica()
        
def sibenica():
    hadane = set()
    pocet = -1
    for i in range(len(slovo)+10):
        if set(slovo) == hadane:
            canvas.create_text(250,150, text = 'GRATULUJEM', font = 'arial 20', fill = 'red')
            break
        hadane_pismeno = str(input('hadaj pismeno: '))
        if hadane_pismeno in slovo:
            hadane.add(hadane_pismeno)
            for j in range(len(slovo)):
                if slovo[j] == hadane_pismeno:
                    t3 = canvas.create_text(35+j*s, 65, text = hadane_pismeno.upper(), font = 'arial 20')
                    canvas.update()

        else:
            pocet += 1
            if pocet ==0:
                canvas.create_oval(90,120,110,140, tag = 'obesenec')
                canvas.update()
            if pocet == 1:
                canvas.create_line(100,140,100, 180, tag = 'obesenec')
                canvas.update()
            if pocet == 2:
                canvas.create_line(100,150, 80, 140, tag = 'obesenec')
                canvas.update()
            if pocet == 3:
                canvas.create_line(100,150, 120,140, tag = 'obesenec')
                canvas.update()
            if pocet == 4:
                canvas.create_line(100,180, 80, 220, tag = 'obesenec')
                canvas.update()
            if pocet == 5:
                canvas.create_line(100,180,120,220)
                t2 = canvas.create_text( 250,150, text = 'NEUHADOL SI', font = 'arial 20', fill = 'red')
                canvas.update()
                break

canvas.bind('<Button-1>', zaciatok_hry)
canvas.mainloop()
