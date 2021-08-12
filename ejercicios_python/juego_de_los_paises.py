# ¡Adivina EL PAÍS!
# ---
# Ingresa una letra:
import random # 1er paso: es importar los módulos que usaremos.
import os

paises = ["ALEMANIA", "SUECIA", "HOLANDA", "CHINA", "ESPAÑA", "TURQUIA", "FRANCIA", "QATAR", "ISRAEL", "BRASIL", "EEUU", "MEXICO", "URUGUAY", "ITALIA", "IRLANDA", "SUIZA", "JAPON", "ISLANDIA", "AUSTRALIA", "DINAMARCA"] #2. se crea una lista con las palabras a descubrir.
#palabra = random.choice(paises) -> sin la palabra 'list' solo sería una cadena de caractéres.
palabra = list(random.choice(paises))#método 'choice´ del módulo random para que se elija automaticamente el país a descubrir

horca = ["      !======N",
         "             N",
         "             N",
         "             N",
         "             N",
         "             N",
         "             N",
         " ____________N"]

cuerpo = ["     !=======N",
          "     O       N",
          "    /|\      N",
          "    \|/      N",
          "    | |      N",
          "   _\ /_     N",
          "             N",]

letras_elegidas = [] # 3. Todas la letras tecleadas se guaardarán aquí para recordarle al usuario que elíja otra.
fallos = 1 #4. contador de fallos iniciando en 1 para que se dibuje la primera linea.

resultado= [] #5. Creamos una lista que contendrá tantos guiones como caracteres tenga la palabra. Funciona con este for
for i in range(len(palabra)):#con 'append' agregamos un _ por cada letra que contenga 'palabra'
  resultado.append("_")

while True: #bucle principal
  os.system("cls") #orden generada para comenzar el juego limpiando todo el dibujo de fallos
  
  #Presentamos la cabecera del juego
  print("***   JUEGO DE LOS PAISES   ***")
  print("*******************************")
  
  for i in range(fallos):#6. un for para mostrar elementos de la lista cuerpo según los fallos que se hayan cometido.
    print(cuerpo[i])
  for i in range(len(horca)-fallos): #7. otro for que mostrará el resto de espacios de la lista horca quitando tantos fallos haya habido.
    print(horca[i+fallos])#y mostramos los espacios de la lista horca + los fallos que hayamos tenido
  print()

  #8. Mostramos el resultado que se va obteniendo
  print("   ", end= " ") #esto es para que se muestren espacios luego de los caracteres elej
  for i in resultado:
    print(i, end=" ")
     
  print()
  print()

# 9. Comprobamos si se ha acertado la palara o se han terminado los intentos
  if resultado == palabra: #comprobamos
    print("***   HAS GANADO   ***") #mostramos el mensaje
    break #para salir del bucle principal

  if fallos > 4: #comprobamos
    print("La palabra era:", "".join(palabra)) #usamos 'join' para convertir 'palabra' a una lista de caracteres
    print("***   HAS PERDIDO   ***") #Mostramos mensaje
    break #para salir del bucle principal

#NOTA: el item 9 se pone incluso antes de pedir las letras porque queremos ir mostrando el resultado desde el comienzo

  #10. Bucle para que el usuario elija una letra
  while True:
    letra_usuario_sin_formato = input("Dime una letra: ") #obtenemos las letras del usuario
    letra_usuario = letra_usuario_sin_formato.upper() #las convertimos en mayusculas
    if len(letra_usuario) != 1: #si lo que ingresó el usuario es distinto de 1
      print("Introduce una letra")#mostrar este mensaje
    elif letra_usuario in letras_elegidas: #si elije una letra q ya estaba
      print("Esa letra ya la has dicho.")#mostrar este mensaje
    elif letra_usuario not in "ABCDEFGHIJKLMNOPQRSTUVWXYZ": #por si introduce una letra inválida
      print("Introduce una letra")#mostrar este mensaje
    else: # si es una letra adecuada la añadimos a 'letras todas'
      letras_elegidas.append(letra_usuario)
      break

  #Por último
  #Comprobamos si la letra está en la palabra, y si está, la mostramos y reemplazamos el _
  for i in range(len(palabra)): 
    if palabra[i] == letra_usuario: #comprobamos si lo q ingresó el usuario con coincide con algún elemento de la lista palabra
      resultado[i] = letra_usuario #le damos un nuevo valor reemplazando el guion por la letra_usuario

  if letra_usuario not in palabra: #si lo que ingresó el usuario no está en la lista palabra entonces aumentar de a 1 la variable 'fallos'.
    fallos += 1

  print()
  print()

# def run():
#   pass

#if __name__ == '__main__':
#  paises()