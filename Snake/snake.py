from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self): # Constructor
        self.segments = []  # Partes de la serpiente
        self.create_snake() # Cuerpo de la serpiente
        self.head = self.segments[0]    # Cabeza de la serpiente

    def create_snake(self): # Asignacion de la serpiente
        for position in STARTING_POSITIONS:
            self.add_segment(position)            

    def add_segment(self, position): # Asignar segmento
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)   # Introducir parte de la serpiente a la lista

    def extend(self):   # Nuevo segmento de cuerpo
        self.add_segment(self.segments[-1].position())  # Posicion final


    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):    # La cola sigue a la cabeza ([2]->[1]->[0])
            new_x = self.segments[seg_num - 1].xcor()   # Se toma la posicion siguiente en x
            new_y = self.segments[seg_num - 1].ycor()   # Se toma la posicion siguiente en y
            self.segments[seg_num].goto(new_x, new_y)   # Nueva posición 
        self.head.forward(MOVE_DISTANCE)       # Mover cabeza

    def up(self):       #Mover hacia arriba
        if self.head.heading() != DOWN: # No puedes ir en sentido contrario
            self.head.setheading(UP)

    def down(self):     #Mover hacia abajo
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):     #Mover hacia izquierda
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):    #Mover hacia derecha
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
