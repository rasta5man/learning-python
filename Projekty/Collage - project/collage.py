import tkinter

# heigth aff all objects
heigth = 50

class Shape:                                        # base class for all shapes

    def __init__(self, x, y, color, canvas):
        self.x = x
        self.y = y
        self.color = color
        self.canvas = canvas

    def move(self, dx, dy):                         # defines movement of objects from control panel to workspace   
        self.x += dx
        self.y += dy
        canvas.move(self.id, dx, dy)
        #self.canvas.move(self.id, dx, dy)          # both of them work

    def change_color(self, color):
        self.color = color
        canvas.itemconfig(self.id, fill = color)
        #self.canvas.itemconfig(self.id, fill = color)    # both of them work


class Square(Shape):

    def __init__(self, x, y, color, canvas):
        super().__init__(x, y, color, canvas)
        self.id = canvas.create_rectangle(self.x, self.y, self.x + heigth, self.y + heigth, fill= self.color, width = 3)
        self.primaryX = self.x
        self.primaryY = self.y
    
    def is_click(self, x, y):
        if self.x <= x <=self.x+heigth and self.y <= y <= self.y+heigth:
            return True
    
    def __str__(self):
        return 'square,{},{},{}'.format(self.x, self.y, self.color)

    def shape_copy(self):
        return Square(self.x,self.y,self.color,canvas)
    
    def go_back(self):
        canvas.coords(self.id, self.primaryX, self.primaryY, self.primaryX + heigth, self.primaryY + heigth)


class Circle(Shape):

    def __init__(self, x, y, color, canvas):
        super().__init__(x, y, color, canvas)
        self.r = heigth/2
        self.primaryX = self.x
        self.primaryY = self.y
        self.id = canvas.create_oval(self.x-self.r, self.y-self.r, self.x+self.r, self.y+self.r, fill=self.color, width = 3)
    
    def __str__(self):
        return 'circle,{},{},{}'.format(self.x, self.y, self.color)

    def is_click(self,x,y):
        return (self.x - x)**2 + (self.y-y)**2 < (heigth/2)**2

    def shape_copy(self):
        return Circle(self.x, self.y, self.color, canvas)

    def go_back(self):
        canvas.coords(self.id, self.primaryX - self.r, self.primaryY - self.r, self.primaryX + self.r, self.primaryY + self.r )


class Rectangle(Shape):

    def __init__(self, x, y, width, color, canvas):
        super().__init__(x, y, color, canvas)
        self.width = width
        self.primaryX = self.x
        self.primaryY = self.y
        self.id = canvas.create_rectangle(self.x, self.y, self.x +self.width, self.y + heigth, fill = self.color, width = 3)

    def __str__(self):
        return 'rectangle,{},{},{},{}'.format(self.x, self.y, self.width, self.color) 

    def is_click(self, x, y):
        return self.x <= x <=self.x+self.width and self.y <= y <= self.y+heigth

    def go_back(self):
        canvas.coords(self.id, self.primaryX, self.primaryY, self.primaryX + self.width, self.primaryY + heigth)

    def shape_copy(self):
        return Rectangle(self.x, self.y, self.width, self.color, canvas)


class Rectangle1(Shape):

    def __init__(self, x, y, width, color, canvas):
        super().__init__(x, y, color, canvas)
        self.width = width
        self.primaryX = self.x
        self.primaryY = self.y
        self.id = canvas.create_rectangle(self.x, self.y, self.x +heigth, self.y + self.width, fill = self.color, width = 3)

    def __str__(self):
        return 'rectangle1,{},{},{},{}'.format(self.x, self.y, self.width, self.color)

    def is_click(self, x, y):
        return self.x <= x <=self.x+heigth and self.y <= y <= self.y+self.width

    def go_back(self):
        canvas.coords(self.id, self.primaryX, self.primaryY, self.primaryX + heigth, self.primaryY + self.width)

    def shape_copy(self):
        return Rectangle1(self.x, self.y, self.width, self.color, canvas)


class Triangle(Shape):

    def __init__(self, x, y, color, canvas):
        super().__init__(x, y, color, canvas)
        self.primaryX = self.x
        self.primaryY = self.y
        self.id = canvas.create_polygon(self.x, self.y, self.x + heigth, self.y, self.x + heigth/2, self.y - heigth, self.x, self.y, fill = self.color, outline ='black',  width =3)

    def __str__(self):
        return 'triangle,{},{},{}'.format(self.x, self.y, self.color)

    def is_click(self,x,y):
        return self.x <= x <= self.x+heigth and self.y >= y > self.y-heigth

    def shape_copy(self):
        return Triangle(self.x, self.y, self.color, canvas)

    def go_back(self):
        canvas.coords(self.id, self.primaryX, self.primaryY, self.primaryX + heigth, self.primaryY, self.primaryX + heigth/2, self.primaryY - 50, self.primaryX, self.primaryY)


class Oval(Shape):

    def __init__(self, x, y, color, canvas):
        super().__init__(x, y, color, canvas)
        self.primaryX = self.x
        self.primaryY = self.y
        self.id = canvas.create_oval(self.x - heigth-15, self.y -heigth/2, self.x+heigth-15, self.y + heigth/2, fill =self.color, width = 3)

    def __str__(self):
        return 'oval,{},{},{}'.format(self.x, self.y, self.color)

    def is_click(self,x,y):
        return (self.x - x)**2 + (self.y-y)**2 < (heigth/2)**2

    def shape_copy(self):
        return Oval(self.x, self.y, self.color, canvas)

    def go_back(self):
        canvas.coords(self.id, self.primaryX - heigth - 15, self.primaryY - heigth/2, self.primaryX + heigth - 15, self.primaryY + heigth/2)


class Color_bucket(Shape):

    def __init__(self, x, y, color, canvas):
        super().__init__(x,y,color, canvas)
        self.r = 15
        self.primaryX = self.x
        self.primaryY = self.y
        self.id = canvas.create_oval(self.x - self.r, self.y - self.r, self.x+self.r, self.y+self.r, fill = self.color, width = 3)

    def is_click(self,x,y):
        return (self.x - x)**2 + (self.y-y)**2 < (self.r)**2

    def go_back(self):
        canvas.coords(self.id, self.primaryX - self.r, self.primaryY - self.r, self.primaryX + self.r, self.primaryY + self.r )


class Button(Shape):      # defines 3 buttons in control panel: write to file, read from file, delete workspace

    def __init__(self, x, y, s, color, canvas):
        super().__init__(x, y, color, canvas)
        self.width= s
        self.text = ''
        self.id = canvas.create_rectangle(self.x, self.y, self.x + self.width, self.y + heigth, fill = self.color, width = 3)
    
    def is_click(self, x, y):
        if self.x <= x <= self.x + self.width and self.y <= y <= self.y + heigth:
            return True
        
    def read_file(self, event):
        # first, I delete all objects from list, which are not supposed to be in control panel
        for unit in range(17, len(program.list_of_all_objects)):
            canvas.delete(program.list_of_all_objects[unit].id)
        program.list_of_all_objects = program.list_of_all_objects[:17]
        try:
            with open('shapes.txt', 'r') as f:
                for row in f:
                    unit = row.strip().split(',')
                    if unit[0] == 'square':
                        square = Square(int(unit[1]), int(unit[2]), unit[3], canvas)
                        program.add_shape_into_group(square)
                    elif unit[0] == 'circle':
                        circle = Circle(int(unit[1]), int(unit[2]), unit[3], canvas)
                        program.add_shape_into_group(circle)
                    elif unit[0] == 'rectangle':
                        rectangle = Rectangle(int(unit[1]), int(unit[2]), int(unit[3]), unit[4], canvas)
                        program.add_shape_into_group(rectangle)
                    elif unit[0] == 'rectangle1':
                        rectangle1 = Rectangle1(int(unit[1]), int(unit[2]), int(unit[3]), unit[4], canvas)
                        program.add_shape_into_group(rectangle1)
                    elif unit[0] == 'triangle':
                        triangle = Triangle(int(unit[1]), int(unit[2]), unit[3], canvas)
                        program.add_shape_into_group(triangle)
                    elif unit[0] == 'oval':
                        oval = Oval(int(unit[1]), int(unit[2]), unit[3], canvas)
                        program.add_shape_into_group(oval)
                f.close()
        except FileNotFoundError:
            print ('File not Found')

    def write_to_file(self, event):
        # objects are written to file from the list from 17 --> 0-16 are objects in control panel
        with open('shapes.txt', 'w') as f:
            for i in range(17, len(program.list_of_all_objects)):
                f.write(str(program.list_of_all_objects[i]))
                f.write('\n')
            print('All objects succesfully written into file')
            f.close()
            self.unit = None

    def delete_workspace(self, event):
        # first 15 objects are from control panel, thats why we iterate from number 17 to the end of list
        if program.list_of_all_objects:
            for i in range(17, len(program.list_of_all_objects)):
                canvas.delete(program.list_of_all_objects[i].id)
            program.list_of_all_objects = program.list_of_all_objects[:17]
            # it works this way too:
            # program.list_of_all_objects[:] = program.list_of_all_objects[:17]


class Program():
    
    def __init__(self, width, height, canvas, layout):
        self.width = width
        self.height = height
        self.layout = layout
        self.canvas = canvas
        # divide canvas into two parts
        self.canvas.create_rectangle(3, 3, self.layout + 4, self.height, width = 4, fill = 'gold')
        self.canvas.create_rectangle(self.layout + 12, 3, self.width, self.height, width = 4, fill = 'white')
        self.list_of_all_objects = []
        self.canvas.bind('<Button-1>', self.on_klik)
        
    def on_klik(self, event):
        self.unit = self.clicked_object(event)
        self.x0, self.y0 = event.x, event.y
        if self.unit == None:
            return
        elif self.unit == button1:
            self.canvas.bind('<ButtonRelease-1>', button1.read_file)
        elif self.unit == button2:
            self.canvas.bind('<ButtonRelease-1>', button2.write_to_file)
        elif self.unit == button3:
            self.canvas.bind('<ButtonRelease-1>', button3.delete_workspace)
        else:
            self.canvas.bind('<B1-Motion>', self.drag_event)
            self.canvas.bind('<ButtonRelease-1>', self.release_event)
           
    def drag_event(self, event):
        self.unit.move(event.x - self.x0, event.y - self.y0)
        self.x0 = event.x
        self.y0 = event.y
        
    def release_event(self, event):
        if isinstance(self.unit, Color_bucket):
            self.color_bucket_is_on_unit(event.x, event.y)
            self.unit.x = self.unit.primaryX
            self.unit.y = self.unit.primaryY
            self.unit.go_back()
        if self.unit.id != 9 and self.unit.id != 10 and self.unit.id !=11 and self.unit.id !=12 \
            and self.unit.id != 13 and self.unit.id !=14 and self.unit.id != 15 and self.unit.id != 16 \
            and self.unit.id != 17 and self.unit.id != 18 and self.unit.id != 19 and self.unit.id != 20 \
            and self.unit.id != 21 and self.unit.id != 22:
            if self.unit.x>780 or self.unit.x<220 or self.unit.y>580 or self.unit.y<20:
                self.canvas.delete(self.unit.id)
                self.list_of_all_objects.remove(self.unit)
        if self.unit.id == 9 or self.unit.id == 10 or self.unit.id == 11 or self.unit.id==12 or self.unit.id == 13 \
            or self.unit.id == 14:
            if 780>event.x >250 and 580>event.y>20:
                new = self.unit.shape_copy()
                self.add_shape_into_group(new)
                self.unit.x = self.unit.primaryX
                self.unit.y = self.unit.primaryY
                self.unit.go_back()
            else:
                self.unit.x = self.unit.primaryX
                self.unit.y = self.unit.primaryY
                self.unit.go_back()
        self.canvas.unbind('<B1-Motion>')
        self.canvas.unbind('<ButtonRelease-1>')
        
        # debugging
        #print(self.list_of_all_objects)
        #print(self.unit.id)
        #print(self.unit.x, self.unit.y)
        
    def clicked_object(self, event):
        # both ways are correct
        '''
        ix = len(self.list_of_all_objects)-1
        while ix >= 0 and not self.list_of_all_objects[ix].is_click(event.x, event.y):
            ix -= 1
        if ix < 0:
            return None
        else:
            return self.list_of_all_objects[ix]
        '''
        for unit in self.list_of_all_objects:
            if unit.is_click(event.x, event.y):
                return unit
        return None

    def add_shape_into_group(self, unit):
        self.list_of_all_objects.append(unit)
    
    def color_bucket_is_on_unit(self, x, y):
        for i in range(17, len(self.list_of_all_objects)):
            if isinstance(self.list_of_all_objects[i], Circle):
                if (self.list_of_all_objects[i].x - x)**2 + (self.list_of_all_objects[i].y-y)**2 < (self.list_of_all_objects[i].r)**2:
                    self.list_of_all_objects[i].change_color(self.unit.color)
            elif isinstance(self.list_of_all_objects[i], Square):
                if self.list_of_all_objects[i].x <= x <=self.list_of_all_objects[i].x+heigth and \
                    self.list_of_all_objects[i].y <= y <= self.list_of_all_objects[i].y+heigth:
                    self.list_of_all_objects[i].change_color(self.unit.color)
            elif isinstance(self.list_of_all_objects[i], Rectangle):
                if self.list_of_all_objects[i].x <= x <=self.list_of_all_objects[i].x+self.list_of_all_objects[i].width and \
                    self.list_of_all_objects[i].y <= y <= self.list_of_all_objects[i].y+heigth:
                    self.list_of_all_objects[i].change_color(self.unit.color)
            elif isinstance(self.list_of_all_objects[i], Rectangle1):
                if self.list_of_all_objects[i].x <= x <=self.list_of_all_objects[i].x+heigth and \
                    self.list_of_all_objects[i].y <= y <= self.list_of_all_objects[i].y+self.list_of_all_objects[i].width:
                    self.list_of_all_objects[i].change_color(self.unit.color)
            elif isinstance(self.list_of_all_objects[i], Triangle):
                if self.list_of_all_objects[i].x <= x <=self.list_of_all_objects[i].x+ heigth and self.list_of_all_objects[i].y >= y > self.list_of_all_objects[i].y-heigth:
                    self.list_of_all_objects[i].change_color(self.unit.color)
            elif isinstance(self.list_of_all_objects[i], Oval):
                if (self.list_of_all_objects[i].x - x)**2 + (self.list_of_all_objects[i].y-y)**2 < (heigth/2)**2:
                    self.list_of_all_objects[i].change_color(self.unit.color)

root = tkinter.Tk()
canvas = tkinter.Canvas(root, height = 600, width = 800)
root.title('TK paint')
canvas.pack()
    
program = Program(800, 600, canvas, 200)
    
button1 = Button(20,20,160, 'red', canvas)
button1.text = canvas.create_text(100,46, text = 'Read from file', font = 'arial 11')
button2= Button(20,80,160, 'blue',canvas)
button2.text = canvas.create_text(100,106, text='Save workspace', font = 'arial 11')
button3 = Button(20,140,160, 'green',canvas)
button3.text = canvas.create_text(100,166, text='Delete workspace', font = 'arial 11')

square = Square(148,260, 'blue', canvas)
circle = Circle(118, 285, 'blue', canvas)
rectangle = Rectangle(8,260,80,'blue', canvas)
rectangle1 = Rectangle1(8, 320, 80, 'blue', canvas )
triangle = Triangle(64, 402, 'blue', canvas)
oval = Oval(163, 344, 'blue', canvas)
color_bucket_red = Color_bucket(25, 490, 'red', canvas)
color_bucket_green = Color_bucket(75, 490, 'green', canvas)
color_bucket_blue = Color_bucket(125, 490, 'blue', canvas)
color_bucket_yellow = Color_bucket(175, 490, 'yellow', canvas)
color_bucket_brown = Color_bucket(25, 530, 'brown', canvas)
color_bucket_black = Color_bucket(75,530, 'black', canvas)
color_bucket_white = Color_bucket(125,530,'white', canvas)
color_bucket_gray = Color_bucket(175,530,'gray', canvas)

program.add_shape_into_group(square)
program.add_shape_into_group(circle)
program.add_shape_into_group(button1)
program.add_shape_into_group(button2)
program.add_shape_into_group(button3)
program.add_shape_into_group(rectangle)
program.add_shape_into_group(rectangle1)
program.add_shape_into_group(triangle)
program.add_shape_into_group(oval)
program.add_shape_into_group(color_bucket_red)
program.add_shape_into_group(color_bucket_green)
program.add_shape_into_group(color_bucket_blue)
program.add_shape_into_group(color_bucket_yellow)
program.add_shape_into_group(color_bucket_brown)
program.add_shape_into_group(color_bucket_black)
program.add_shape_into_group(color_bucket_white)
program.add_shape_into_group(color_bucket_gray)

canvas.mainloop()