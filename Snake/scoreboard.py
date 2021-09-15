from turtle import Turtle, update
ALIGNMENT = "center"
FONT = ("Courier",15,"normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()            # No dibujar linea
        self.goto(0,270)        # Posicion
        self.hideturtle()   # No aparecer apuntador
        self.update_scoreboard()
    
    def update_scoreboard(self):    # Actualizar Score
        self.write(f"Score {self.score}",align=ALIGNMENT,font=FONT)

    def game_over(self):    # Juego terminado
        self.goto(0,0)
        self.write("GAME OVER",align=ALIGNMENT,font=FONT)

    def increase_score(self):   # Incrementar score
        self.score += 1
        self.clear()
        self.update_scoreboard()        
        