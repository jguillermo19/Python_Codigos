from turtle import Turtle, Screen
import random

is_race_on = False  # Activador de la carrera
screen = Screen()   # Ventana
screen.title("Carrera de Tortugas")   # Titulo
screen.setup(width=500,height=400) # Tamaño de la ventana
# Ventana emergente
user_bet = screen.textinput(title="Hagan sus apuestas!",prompt="¿Cual tortuga ganara la carrera?\n\n"
                                  "Ingresa el color: red, orange, yellow, green, blue, purple")
#print(user_bet)
colors = ["red","orange","yellow","green","blue","purple"]  # Colores de las tortugas
y_positions = [-70,-40,-10,20,50,80]    # Posiciones iniciales de la tortugas
all_turtles = []    # Lista nueva donde se alojaran las tortugas

# Ingresar tortugas a la lista
for index in range(6):   
    new_turtle = Turtle(shape="turtle") # Forma
    new_turtle.color(colors[index])     # Color
    new_turtle.penup()                  # No dibujar linea
    new_turtle.goto(x=-230,y=y_positions[index])    # Colocar tortugas
    all_turtles.append(new_turtle)      # Ingresa objeto a la lista

if user_bet:
    is_race_on = True      # Activa la carrera

while is_race_on:          # Mientras la carrera este activada
    # Hacer mover a las tortugas
    for turtle in all_turtles:
        if turtle.xcor()>230:       # El primero que llegue a esa coordenada, termina la carrera
            is_race_on=False        # Terminar carrera
            winning_color = turtle.pencolor()   # Obtener el color de la tortuga ganadora
            if winning_color == user_bet:       # Comparacion del color
                print(f'Has ganado! La tortuga "{winning_color}" es la ganadora!')
            else:
                print(f'Has perdido! La tortuga "{winning_color}" es la ganadora!')
        rand_distance = random.randint(0,10) # Tamaño de movimiento de la tortuga
        turtle.forward(rand_distance)        # Movimiento de la tortuga

# Salir de la pantalla con un clic
screen.exitonclick()