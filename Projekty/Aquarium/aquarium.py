from kor import *
import random

class Aquarium:
    def __init__(self):
        self.k = Kor()
        self.k.ht()
        self.draw_aquarium()
        
    def draw_aquarium(self):
        self.k.pu()
        self.k.setpos(290,290)
        self.k.pd()
        self.k.seth(270)
        self.k._pw = 10
        for i in range(3):
            self.k.fd(580)
            self.k.rt(90)
        self.k._pw = 3
        self.k.setpos(-285,285)
        self.k.rt(20)                   # water at the top
        self.k.fd(50)
        self.k.lt(40)
        self.k.fd(50)
        self.k.rt(40)
        self.k.fd(50)
        self.k.lt(40)
        self.k.fd(50)
        self.k.rt(40)
        self.k.fd(50)
        self.k.lt(40)
        self.k.fd(50)
        self.k.rt(40)
        self.k.fd(50)
        self.k.lt(40)
        self.k.fd(50)
        self.k.rt(40)
        self.k.fd(50)
        self.k.lt(40)
        self.k.fd(50)
        self.k.rt(40)
        self.k.fd(50)
        self.k.lt(38)
        self.k.fd(65)

class Fish():
    def __init__(self, x, y):
        self.x, self.y = x, y
        self.stepX = random.choice([-4,-2, 2, 4])   # random choice for speed of swim of fish
        self.stepY = random.choice([-2,0,2])        # random choice for angle of swim of fish
        self.k = None                               # turtle, that draw fish
        self.counter = random.randrange(50)         # when the counter is modulo200 0, fish randomly turns
        self.life = 200                             # when the life is 0, fish dies
        self.concrete_food = None                   # fish spot particular food
        self.distance = None                        # distance of food from fish
        
    def draw_fish_left(self):
        self.k.ht()
        self.k.setpos(self.x, self.y)
        self.k.seth(40)
        for i in range(9):
            self.k.fd(6)
            self.k.rt(15)
        self.k.pu()
        self.k.setpos(self.x, self.y)
        self.k.seth(-40)
        self.k.pd()
        for i in range(9):
            self.k.fd(6)
            self.k.lt(15)
        self.k.seth(270)
        self.k.fd(30)
        self.k.pu()                             # eye of fish
        self.k.setpos(self.x+9, self.y +2)
        self.k.pd()
        for i in range(18):
            self.k.fd(0.5)
            self.k.lt(20)
        self.k.pu()                             # indicator of life   
        self.k.setpos(self.x +5 , self.y + 20)
        self.k.pd()
        self.length = (self.life) / 6.5         # length of line over fish indicates life
        self.k._pw = 3                          # width of life line
        self.k.seth(0)
        self.k.fd(self.length)                   # draw life line
    
    def draw_fish_right(self):
        self.k.ht()
        self.k.setpos(self.x, self.y)
        self.k.seth(140)
        for i in range(9):
            self.k.fd(6)
            self.k.lt(15)
        self.k.pu()
        self.k.setpos(self.x, self.y)
        self.k.seth(-140)
        self.k.pd()
        for i in range(9):
            self.k.fd(6)
            self.k.rt(15)
        self.k.seth(270)
        self.k.fd(30)
        self.k.pu()                             # eye of fish
        self.k.setpos(self.x-9, self.y+2)
        self.k.pd()
        for i in range(18):
            self.k.fd(0.5)
            self.k.lt(20)
        self.k.pu()                             # indicator of life
        self.k.setpos(self.x -5, self.y + 20)
        self.k.pd()
        self.k.seth(180)
        self.length = (self.life) / 6.5
        self.k._pw = 3
        self.k.fd(self.length)
 
class Food():
    def __init__(self, x, y):
        self.x, self.y = x, y
        self.k = None
        self.step = random.choice([-1,-2])
            
    def draw_food(self):
        self.k._pw = random.choice([2,4])
        self.k.ht()
        for i in range(3):
            self.k.fd(5)
            self.k.rt(120)

class Program:
    def __init__(self):
        bgcolor('white')            # inicializacion of canvas
        self.fish_list=[]
        self.food=[]
        Aquarium().draw_aquarium()
        Kor.g.bind('<Button-3>', self.add_fish)
        Kor.g.bind('<Button-1>', self.add_food)
        Kor.g.bind('<B1-Motion>', self.add_food)
        self.timer()
        Kor.g.mainloop()
    
    def add_fish(self, event):
        self.fish_list.append(Fish(event.x - Kor._x0, Kor._y0 - event.y))
    
    def add_food(self, event):
        if event.x >15 and event.x < 580:
            self.food.append(Food(event.x - Kor._x0, Kor._y0 - event.y))

    def timer(self):
        Kor.g.delete('all')
        Aquarium().draw_aquarium()

        for fish in self.fish_list:
            fish.k = Kor(fish.x, fish.y)
            # logic, when fish is close to food
            if fish.concrete_food is None or fish.concrete_food not in self.food:
                for food in self.food:
                    food.k = Kor(food.x, food.y)
                    fish.distance = fish.k.distance(food.x, food.y)
                    if fish.distance < 150:
                        fish.concrete_food = food
                        break
            else:
                # logic of movement of fish towards food
                fish.distance = fish.k.distance(fish.concrete_food.x,  fish.concrete_food.y)
                if fish.distance < 150:
                    if fish.x > fish.concrete_food.x and fish.y > fish.concrete_food.y:
                        if fish.concrete_food.x -30 < fish.x < fish.concrete_food.x +30:
                            fish.y += -7
                        else:
                            if fish.stepX > 0:
                                fish.stepX = -6
                            fish.y += -7
                    if fish.x > fish.concrete_food.x and fish.y < fish.concrete_food.y:
                        if fish.concrete_food.x -30 < fish.x < fish.concrete_food.x +30:
                            fish.y += 2
                        else:
                            if fish.stepX > 0:
                                fish.stepX = -6
                            fish.y += 2
                    if fish.x < fish.concrete_food.x and fish.y > fish.concrete_food.y:
                        if fish.concrete_food.x -30 < fish.x < fish.concrete_food.x +30:
                            fish.y += -7
                        else:
                            if fish.stepX < 0:
                                fish.stepX = 6
                            fish.y += -7
                    if fish.x < fish.concrete_food.x and fish.y < fish.concrete_food.y:
                        if fish.concrete_food.x -30 < fish.x < fish.concrete_food.x +30:
                            fish.y += 2
                        else:
                            if fish.stepX < 0:
                                fish.stepX = 6
                            fish.y += 2
                # fish eats food, when coords are in range -6 +6, all atributes change to None
                if (fish.x == fish.concrete_food.x or fish.x == fish.concrete_food.x+1 or fish.x == fish.concrete_food.x+2 or \
                fish.x == fish.concrete_food.x-1 or fish.x == fish.concrete_food.x-2 or fish.x == fish.concrete_food.x+3 or \
                fish.x == fish.concrete_food.x-3 or fish.x == fish.concrete_food.x+4 or fish.x == fish.concrete_food.x-4 or 
                fish.x == fish.concrete_food.x-5 or fish.x == fish.concrete_food.x+5 or fish.x == fish.concrete_food.x+6 or fish.x == fish.concrete_food.x-6) \
                and (fish.y == fish.concrete_food.y or  fish.y == fish.concrete_food.y+1 or fish.y == fish.concrete_food.y-1 \
                or fish.y == fish.concrete_food.y +2 or fish.y == fish.concrete_food.y -2 or fish.y == fish.concrete_food.y+3 \
                or fish.y == fish.concrete_food.y-3 or fish.y == fish.concrete_food.y -4 or fish.y == fish.concrete_food.y +4 or \
                fish.y == fish.concrete_food.y -5 or fish.y == fish.concrete_food.y +5 or fish.y == fish.concrete_food.y+6 or fish.y == fish.concrete_food.y-6):
                    if fish.life < 200:
                        fish.life += 50
                    if fish.concrete_food in self.food:
                        self.food.remove(fish.concrete_food)
                    fish.concrete_food = None
                    fish.distance = None
                    fish.stepX = random.choice([-4,-2, 2, 4])

        # logic of turning of fish at the end of aquarium or random turn of fish
            if fish.counter%200 == 0:
                if fish.concrete_food is None:
                    fish.stepX *= -1
                    fish.stepY = random.choice([-1,-2,0,1,2])
            if fish.x > 245:
                fish.x += -5
                fish.stepX *= -1
                fish.stepY = random.choice([0,1,-1,2,-2])
            if fish.x < -245:
                fish.x += 5
                fish.stepX *= -1
                fish.stepY = random.choice([0,1,-1,2,-2])
            if fish.y < -265:
                fish.y += 10
                fish.stepY *= -1
            if fish.y > 265:
                fish.stepY *= -1
            if fish.life==0:
                self.fish_list.remove(fish)

            fish.x += fish.stepX
            fish.y += fish.stepY 
            # drawing of fish according to swim direction            
            if fish.stepX < 0:
                fish.draw_fish_left()
            else:
                fish.draw_fish_right()
            fish.counter += 1
            fish.life -= 0.5
        # drawing of food          
        for food in self.food:
            food.y += food.step
            if food.y < -265:
                self.food.remove(food)
            food.k = Kor(food.x, food.y)
            food.draw_food()

        Kor.g.after(100, self.timer)

Program()