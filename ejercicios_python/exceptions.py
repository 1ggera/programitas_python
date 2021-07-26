# Try, except, raise y finally: los errores que python no nos avisa que están ocurriendo.

#Utilizamos el raise error, cuando queremos que dadas ciertas circustancias nuestro programa para y advierta al usuario.

# Try and except (probar y excepto qué, hacer lo siguiente)
def palindrome(string): # Definimos el nombre de la función que recibirá un string
  try: #intentamos
    if len(string) == 0: # 1. Comenzamos preguntando si la longitud del string es igual a cero
      raise ValueError("No se puede ingresar una cadena vacía") # 2. si es igual a cero entonces arroja un VE con el siguiente mensaje.
    return string == string[::-1]# 3. sino, evalúa ese string con este cálculo.
  except ValueError as ve: # 4. Si ocurre un error lo llamaremos VE 
    print(ve) # 5. Vamos a imprimir ese error
    return False 

try:
  print(palindrome(""))
except TypeError:
  print("Solo se pueden ingresar strings")


def run():
  #print(palindrome(1))con esta linea el programa imprimirá el mensaje de que solo se pueden ingresar 'strings'.
  print(palindrome(""))

if '__name__' == '__main__':
  run()

# NOTA:
#  try:
#    pass #Código a evaluar
#  except:
#    pass #Si ocurre un error, llegará a esta parte

# Finally: se usa para
#  cerrar un archivo dentro de Python.
#  cerrar una conexión a una base de datos.
#  liberar recursos externos.

