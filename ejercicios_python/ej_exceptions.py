#Intentamos resolver los bugs de un programa que regresa los divisores de un número en particular.
def divisors(num):
  try:  # intentar devolver los divisores 
    if num <= 0: # pero si el número ingresado es menor a cero entonces 
      raise ValueError("No se puede jugar con números negativos") # elevar un VE con este mensaje
    divisors = []
    for i in range(1, num + 1):
      if num % i == 0:
        divisors.append(i)
    return divisors
  except ValueError as ve:
    return ve

def run():
#    num = int(input("Ingresa un número: "))
#    print(divisors(num))
#    print("Terminó mi programa")
#Si dejamos el programa así arrojará un traceback. Nos dirá que hay algo inválido para la funcion 'int'.
#Se debe a que intentamos convertir a entero la letra que ingresó el usuario.
#Para evitar ese error envolvemos con 'try' y 'except' el contenido de la función 'run'. y quedaría así:
  try:
    num = int(input("Ingresa un número: "))
    print(divisors(num))
    print("Terminó el programa")
  except ValueError:
    print("Debes ingresar un número")

if __name__ == '__main__':
  run()


#NOTA:
# try:
#     pass #Código a evaluar
# except:
#     pass #Si ocurre un error, llegará a esta parte