from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")          # Forma cuadrado
        self.color("white")           # Color blanco
        self.shapesize(stretch_wid=5,stretch_len=1)   # Tamaño de objeto
        self.penup()                  # No dibujar linea
        self.goto(position)           # Posicion inicial

    def go_up(self):                  # Movimiento hacia arriba
        new_y = self.ycor() + 20
        self.goto(self.xcor(),new_y)

    def go_down(self):                # Movimiento hacia abajo
        new_y = self.ycor() - 20
        self.goto(self.xcor(),new_y)