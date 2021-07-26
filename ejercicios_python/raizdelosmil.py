#Reto: Crear un diccionario con la raiz cuadrada de los primeros 1000 números naturales.

import math # 1. Primero importamos la librería 'math' que nos dará las raices cuadradas

def run(): # 2. Luego definimos nuestra función principal
  my_raiz = {i: math.sqrt(i) for i in range(1, 1001)} # 3. Así armamos el diccionario con las raices cuadradas de los primeros 1000 números naturales.
  print(my_raiz)


if __name__ == '__main__': # 2a. este tambien es un paso fundamental
  run()

# NOTA: Aquí vemos como en un DICTIONARY COMPRENHESION la condición es opcional.

