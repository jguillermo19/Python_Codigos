alfabeto=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","r","s","t","u","v","w","x","y","z"]

def posicion(letra,key,tipo):
  posicion=0
  nletra = letra
  if tipo == "C":
    for i in alfabeto:
      if letra == i:
        posicion+=key
        while posicion>26:
          posicion-=26
        nletra = alfabeto[posicion]
      posicion+=1
  if tipo == "D":
    for i in alfabeto:
      if letra == i:
        posicion-=key
        while posicion<0:
          posicion+=26
        nletra = alfabeto[posicion]
      posicion+=1
  return nletra


try:
  tipo=input("Cifrado Cesar:\n\t(C) Codificar\n\t(D) Decodificar\nOpcion: ")
  text = input("\nIngresa el mensaje: ").lower()
  key = int(input("Clave(Numero Entero): "))
  if tipo == "C" or tipo == "D":
    tam=len(text)
    ntext = ""
    for i in range(tam):
        ntext += posicion(text[i],key,tipo)
    print(f"\nMensaje: {ntext}")
  else:
    print("\nOpción erronea!")

except:
  print("\nError en datos!")
