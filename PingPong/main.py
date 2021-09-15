from turtle import Screen
from paddle import Paddle           # Clase paddle
from ball import Ball               # Clase ball
from scoreboard import Scoreboard   # Clase scoreboard
import time

screen = Screen()                       # Ventana
screen.bgcolor("black")                 # Color de fondo de la ventana
screen.setup(width=800, height=600)     # Tamaño de la ventana
screen.title("Pong")                    # Titulo de la ventana
screen.tracer(0)                        # Evitar la animacion

r_paddle = Paddle((350,0))              # Objeto paddle
l_paddle = Paddle((-350,0))
ball = Ball()                           # Objeto ball
score = Scoreboard()               # Objeto score

screen.listen()     # Movimiento de Paddles
screen.onkey(r_paddle.go_up,"Up")
screen.onkey(r_paddle.go_down,"Down")
screen.onkey(l_paddle.go_up,"w")
screen.onkey(l_paddle.go_down,"s")

game_is_on = True
while game_is_on:       # Juego
    #time.sleep(ball.move_speed)
    time.sleep(0.01)
    screen.update()     # Actualizar la pantalla
    ball.move()

    # Detectar pared
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detectar paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Punto para L
    if ball.xcor() > 380:
        ball.reset_position()
        score.l_point()

    # Punto para R
    if ball.xcor() < -380:
        ball.reset_position()
        score.r_point()

screen.exitonclick()   # Salir con un clic