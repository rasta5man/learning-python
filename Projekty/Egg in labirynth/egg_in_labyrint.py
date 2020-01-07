import tkinter
import re

class Egg:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.id = None
                
    def draw(self, g):
        self.g = g
        self.g.delete(self.id)
        self.id = g.create_oval(self.x +10, self.y +7, self.x + 30, self.y+33, fill = 'white')

    def move(self, dx, dy):
        self.x += dx
        self.y += dy
        self.g.move(self.id, dx, dy)


class Key:

    count = 0

    def __init__(self, x, y, polygon):
        self.x = x
        self.y = y
        self.polygon = polygon
        self.id = None

    def draw(self, g):
        self.g = g
        self.id = g.create_polygon(self.polygon)

    def remove_key(self):
        self.g.delete(self.id)
        self.id = None

    def key_near_egg(self, x, y):                       # distance of (x, y) is less than 20 from the key
        if self.id is not None and (abs(self.x - x)) <=20 and abs((self.y-y))<=20:
            Key.count += 1
            self.remove_key()

class Dvere:

    def __init__(self, x, y):
        # door is a blue square 40x40
        self.x = x
        self.y = y
        self.color = 'blue'
        self.id = None

    def draw(self, g):
        self.g = g
        self.g.delete(self.id)
        self.id = g.create_rectangle(self.x, self.y, self.x+40, self.y+40, fill = self.color)

    def change_door_color(self):                            # change door color
        self.color = 'seagreen'
        return self.color


class Program: 
    def __init__(self, file):
        self.file = file
        self.number_of_game_rows = 0
        self.list_of_rows_in_input_file = []
        self.all_doors = {}
        self.key_polygon = []
        self.key_coords = []
        self.all_keys = []
        self.size = 40
        self.color = ['seagreen', 'brown','yellow']

        self.read_input_file()
        
        self.g = tkinter.Canvas(height = self.size*len(self.list_of_rows_in_input_file), width = self.size*len(self.list_of_rows_in_input_file[0]))
        self.g.pack()

        self.process_input_file()
        
        self.draw()
        self.draw_keys()
        
        self.g.bind_all('<Key>', self.move)
        self.g.mainloop()

    def read_input_file(self):
        with open(self.file, 'r') as subor:
            row = list(subor.readline().strip())
            self.number_of_game_rows += 1
            while row:
                self.list_of_rows_in_input_file.append(row)
                row = list(subor.readline().strip())
                self.number_of_game_rows += 1
            key_polygon = subor.readline().strip()
            self.key_polygon = re.split('\s',key_polygon)       # this makes list from coords
            row = subor.readline().strip()
            row = re.split('\s',row)                            # makes list from keys coords
            while row:
                self.key_coords.append(tuple(row))
                row = subor.readline().strip()
                if row:
                    row = re.split('\s',row)
            subor.close()


    def draw_keys(self):
        #key_polygon = ['-15', '7', '-8', '0', '-1', '7', '15', '7', '15', '10', '12', '10', '12', '14', '5', '14', '5', '10', '-1', '10', '-8', '17', '-15', '10']
        #key_coords = [['260', '180'], ['160', '200'], ['60', '320'], ['60', '340'], ['60', '60'], ['60', '80']]
    
        c=[0]*len(self.key_polygon)

        for a,b in enumerate(self.key_coords):
            for i in range(len(self.key_polygon)):
                if i%2 == 0:
                    c[i] = int(self.key_polygon[i]) + int(b[0])
                else:
                    c[i] = int(self.key_polygon[i]) + int(b[1])
            self.key = Key(int(b[0]), int(b[1]), c)
            self.all_keys.append(self.key)
            self.key.draw(self.g)
            c=[0]*len(self.key_polygon)
    

    def draw(self):
        # to make it draw correctly, row a column must be turned around ()
        for s in range(len(self.list_of_rows_in_input_file[0])):
            for r in range(len(self.list_of_rows_in_input_file)):
                x,y = s*self.size, r*self.size
                f = self.color['.xk'.index(self.list_of_rows_in_input_file[r][s])]
                if f == 'brown':
                    self.g.create_rectangle(x, y, x+self.size, y+self.size, fill = f)
                else:
                    self.g.create_rectangle(x, y, x+self.size, y+self.size, fill = f, outline = f)
        for key, value in self.all_doors.items():
            value.x= value.x*self.size
            value.y = value.y*self.size
            value.draw(self.g)
        
        print(self.egg.x, self.egg.y)
        self.egg.x = 6 * self.size
        self.egg.y = 5 * self.size
        print(self.egg.x, self.egg.y)
        self.egg.draw(self.g)

        
    def move(self, event):
        key = event.keysym
        # key type is 'str'
        
        def up():
            r = (self.egg.y + 7 -4)//40
            s = (self.egg.x+30)//40
            if self.list_of_rows_in_input_file[r][s] == 'x':
                return
            else:
                for key, value in self.all_doors.items():
                    if '{}{}'.format(s,r) == key:
                        if Key.count>0:
                            self.all_doors.pop(key)
                            Key.count -= 1
                            value.change_door_color()
                            value.draw(self.g)
                            self.egg.draw(self.g)
                        else:
                            return
                for key in self.all_keys:
                    key.key_near_egg(int(self.egg.x), int(self.egg.y))
                self.egg.move(0,-4)
                
        def down():
            r = (self.egg.y+33+4)//40 
            s = (self.egg.x+30)//40
            if self.list_of_rows_in_input_file[r][s] == 'k':
                self.g.create_text(300,90, text = 'HURAAAAA', fill='red', font='Arial 40 bold')
                self.g.update()
            if self.list_of_rows_in_input_file[r][s] == 'x':
                return

            else:
                for key, value in self.all_doors.items():
                    if '{}{}'.format(s,r) == key:
                        if Key.count>0:
                            self.all_doors.pop(key)
                            Key.count -= 1
                            value.change_door_color()
                            value.draw(self.g)
                            self.egg.draw(self.g)
                        else:
                            return
                for key in self.all_keys:
                    key.key_near_egg(int(self.egg.x), int(self.egg.y))
                self.egg.move(0,4)
                    
        def left():
            r = ((self.egg.y+7)//40)
            s = (self.egg.x + 10 -4)//40
            if self.list_of_rows_in_input_file[r][s] == 'x':
                return
            else:
                for key, value in self.all_doors.items():
                    if '{}{}'.format(s,r) == key:
                        if Key.count>0:
                            self.all_doors.pop(key)
                            Key.count -= 1
                            value.change_door_color()
                            value.draw(self.g)
                            self.egg.draw(self.g)
                        else:
                            return
                for key in self.all_keys:
                    key.key_near_egg(int(self.egg.x), int(self.egg.y))
                self.egg.move(-4,0)

        def right():
            r = (self.egg.y + 7)//40
            s = (self.egg.x + 30 +4)//40
            #print(Key.count)
            if self.list_of_rows_in_input_file[r][s] == 'x':
                return
            else:
                for key, value in self.all_doors.items():
                    if '{}{}'.format(s,r) == key:
                        if Key.count>0:
                            self.all_doors.pop(key)
                            Key.count -= 1
                            value.change_door_color()
                            value.draw(self.g)
                            self.egg.draw(self.g)
                        else:
                            return
                for key in self.all_keys:
                    key.key_near_egg(int(self.egg.x), int(self.egg.y))
                self.egg.move(4,0)
        
        if key == 'Up':
            up()
        if key == 'Down':
            down()
        if key == 'Left':
            left()
        if key == 'Right':
            right()
    
    def process_input_file(self):
        print(self.list_of_rows_in_input_file)
        for r in range(len(self.list_of_rows_in_input_file)):
            for s in range(len(self.list_of_rows_in_input_file[r])):
                if self.list_of_rows_in_input_file[r][s] == 'v':
                    self.egg = Egg(s,r)
                    self.list_of_rows_in_input_file[r][s] = '.'
                if self.list_of_rows_in_input_file[r][s] == 'z':
                    self.all_doors['{}{}'.format(s,r)] = Dvere(s,r)
                    self.list_of_rows_in_input_file[r][s] = '.'

if __name__ == '__main__':
    Program('labyrinth1.txt')