from turtle import Screen
from snake import Snake # Importar la clase Snake
from food import Food # Importar clase food
from scoreboard import Scoreboard # Importar clase score
import time

screen = Screen()       # Ventana
screen.setup(width=600, height=600) # Tamaño de la ventana
screen.bgcolor("black")             # Color de fondo de la ventana
screen.title("Snake")       # Titulo de la ventana
screen.tracer(0)            # Sin trancision en ventana

snake = Snake()     # Clase snake
food = Food()       # Clase food
score = Scoreboard()

screen.listen()     # Movimiento de la serpiente
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True      # Activar el juego
while game_is_on:      # Mientras el juego este activado
    screen.update()    # Actualizar ventana
    time.sleep(0.1)   # Tiempo de transicion
    snake.move()       # Actualizacion de la serpiente

    # Detectar food
    if snake.head.distance(food) < 25:
        food.refresh()
        snake.extend()
        score.increase_score()
        #print("nom nom")
    
    # Detectar pared
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        score.game_over()

    # Detectar cuerpo de serpiente
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            score.game_over()

screen.exitonclick()   # Salir con un clic