import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game_images = [rock, paper, scissors]

try:
    user_choice = int(input("Juego de Piedra, Papel o Tijera\n\t(0) Piedra\n\t(1) Papel\n\t(2) Tijera\nOpcion: "))
    print(game_images[user_choice])

    if user_choice != 0 or user_choice != 1 or user_choice != 2:
        computer_choice = random.randint(0, 2)
        print("\nEleccion de la computadora:")
        print(game_images[computer_choice])

        if user_choice == 0 and computer_choice == 2:
            print("Ganaste!\n")
        elif computer_choice == 0 and user_choice == 2:
            print("Perdiste\n")
        elif computer_choice > user_choice:
            print("Perdiste\n")
        elif user_choice > computer_choice:
            print("Ganaste!\n")
        elif computer_choice == user_choice:
            print("Empate!\n")
    else:
        print("\nOpción erronea!\n")
except:
    print("\nDato erroneo!\n")