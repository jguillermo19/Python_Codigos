import random

def formword(fw,tam):
  nword=""
  for nt in range(tam):
    nword+=fw[nt]+" "
  print("\n"+nword)


def hangman(num):
  if num==6:
    print("""
      _______
     |/      |
     |      
     |      
     |       
     |       
     |
 ____|___""")
  elif num==5:
    print("""
      _______
     |/      |
     |      (_)
     |      
     |       
     |       
     |
 ____|___""")
  elif num==4:
    print("""
      _______
     |/      |
     |      (_)
     |       |
     |       |
     |       
     |
 ____|___""")
  elif num==3:
    print("""
      _______
     |/      |
     |      (_)
     |      \|
     |       |
     |       
     |
 ____|___""")
  elif num==2:
    print("""
      _______
     |/      |
     |      (_)
     |      \|/
     |       |
     |       
     |
 ____|___""")
  elif num==1:
    print("""
      _______
     |/      |
     |      (_)
     |      \|/
     |       |
     |      / 
     |
 ____|___""")
  elif num==0:
    print("""
      _______
     |/      |
     |      (_)
     |      \|/
     |       |
     |      / \\
     |
 ____|___""")


# Palabras a adivinar
words=["cuatro", "estado", "cuenta", "pasado", "entrar", 
       "nombre","caballo", "presidente", "mentiras", "mentalidades", 
       "horizontales", "diagonales"]

tam = len(words)
word = random.choice(words)

tam_w = len(word)
print("____________JUEGO AHORCADO____________\n")
print(f"Palabra de {tam_w} letras:")

fw=[]
lw=[" "]
lwc=1

for ty in range(tam_w):
  fw.extend("_")

formword(fw,tam_w)

lives=6
ct=0
win=0
lr=0

while lives!=0:
  print(f"\nVidas: {lives}")
  letter = input("Ingresa una letra: ").lower()

  for nl in range(tam_w):
    if letter[0]==fw[nl]:
      lr=1
      print("\nLetra repetida!")
      break

  for nl in range(lwc):
    if letter[0]==lw[nl]:
      lr=1
      print("\nLetra erronea repetida!")
      break

  if lr==0:
    flat=0  
    for nl in word:
      if letter[0]==nl:
        fw[ct]=nl
        flat=1
      ct+=1
    if flat==0:
      lives-=1
      lw.extend(letter)
      lwc+=1
    ct=0
    hangman(lives)
    formword(fw,tam_w)
  lr=0

  if "_" not in fw:
    break

if lives==0:
  print("\nPerdiste!")
else:
  print("\nGanaste!")