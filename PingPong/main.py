from turtle import Screen
import time

screen = Screen()       # Ventana
screen.setup(width=600, height=600) # Tamaño de la ventana
screen.bgcolor("black")             # Color de fondo de la ventana
screen.title("Snake")       # Titulo de la ventana
screen.tracer(0)            # Sin trancision en ventana

screen.exitonclick()   # Salir con un clic