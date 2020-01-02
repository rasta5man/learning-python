'''
Hra na hadanie nahodne vybranych slov. Zadavate pismena a ak sa character v slove nenachadza, odvisnete.
Ak uhadnete, program vypise - Hura
'''


import tkinter, random
canvas = tkinter.Canvas()
canvas.pack()

canvas.create_text(180,20, text = 'hangman', font = 'arial 20', fill = 'blue')
o1 = canvas.create_rectangle(300, 20, 360, 50)
t1 = canvas.create_text(330, 35, text = 'New game' )
canvas.create_line(30,250,30,100, 100,100, 100, 120, width = 3, fill ='black')



words = ['vyhoda','pondelok', 'hlava', 'klavesnica', 'uniforma', 'kytica', 'lupa' , 'hokejka', 'pero', 'pocitac', 'vetrovka', 'indian', 'kuzel', 'voda', 'kuchyna', 'serial', 'topanka', 'matematika']
word = random.choice(words)

x, y, s = 20, 50, 30

for character in word:
    character = canvas.create_rectangle(x, y, x+s, y+s)
    x += s

def start_game(event):
    t,z = event.x, event.y
    if 300<=t<=370 and 20<=z<=50:
        canvas.delete(o1,t1)
        canvas.unbind('<Button-1>')
        canvas.update()
        hangman()
        
def hangman():
    guessed = set()
    count = -1
    for i in range(len(word)+10):
        if set(word) == guessed:
            canvas.create_text(250,150, text = 'YOU WON', font = 'arial 20', fill = 'red')
            break
        guessed_character = str(input('Guess a character: '))
        if guessed_character in word:
            guessed.add(guessed_character)
            for j in range(len(word)):
                if word[j] == guessed_character:
                    t3 = canvas.create_text(35+j*s, 65, text = guessed_character.upper(), font = 'arial 20')
                    canvas.update()

        else:
            count += 1
            if count ==0:
                canvas.create_oval(90,120,110,140, tag = 'hang')
                canvas.update()
            if count == 1:
                canvas.create_line(100,140,100, 180, tag = 'hang')
                canvas.update()
            if count == 2:
                canvas.create_line(100,150, 80, 140, tag = 'hang')
                canvas.update()
            if count == 3:
                canvas.create_line(100,150, 120,140, tag = 'hang')
                canvas.update()
            if count == 4:
                canvas.create_line(100,180, 80, 220, tag = 'hang')
                canvas.update()
            if count == 5:
                canvas.create_line(100,180,120,220)
                t2 = canvas.create_text( 250,150, text = 'Sorry, you lose', font = 'arial 20', fill = 'red')
                canvas.update()
                break

canvas.bind('<Button-1>', start_game)
canvas.mainloop()
