from random import randint

logo = """
  / _ \_   _  ___  ___ ___  /__   \ |__   ___    /\ \ \_   _ _ __ ___ | |__   ___ _ __ 
 / /_\/ | | |/ _ \/ __/ __|   / /\/ '_ \ / _ \  /  \/ / | | | '_ ` _ \| '_ \ / _ \ '__|
/ /_\\| |_| |  __/\__ \__ \  / /  | | | |  __/ / /\  /| |_| | | | | | | |_) |  __/ |   
\____/ \__,_|\___||___/___/  \/   |_| |_|\___| \_\ \/  \__,_|_| |_| |_|_.__/ \___|_|  
"""

Facil = 10
Dificil = 5

def check_answer(guess, answer, turns):
  if guess > answer:
    print("\nMuy alto")
    return turns - 1
  elif guess < answer:
    print("\nMuy bajo")
    return turns - 1
  else:
    print(f"\nLo adivinaste, numero es {answer}\n")

#Make function to set difficulty.
def dificultad():
  level = input("Escoge la dificultad\n\t(1) Facil\n\t(2) Dificil\nOpcion: ")
  if level == "1":
    return Facil
  else:
    return Dificil

def game():
  print(logo)
  print("Adivina un numero entre el 1 y el 100.")
  answer = randint(1, 100)
  #print(f"El numero correcto es {answer}") 
  
  turns = dificultad()
  guess = 0
  while guess != answer:
    print(f"\nOportunidades para adivinar: {turns}")
    try:
        guess = int(input("Numero: "))
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("Se te acabaron las oportunidades, perdiste!")
            return
        elif guess != answer:
            print("Intenta de nuevo!")
    except:
        print("\nDato erroneo!")

game()

