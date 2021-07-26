#Crearemos dos funciones para probar el manejo de archivos.
#  read: leerá un archivo que tiene los números del 1 al 10 y convertiremos cada una de las líneas de ese archivo de texto en una lista para usarlas en algún proyecto o programa. Para eso creamo la carpeta 'archivos'.
# write: 

#1. Cargamos la función 'read' en 'run'
#2. En 'read' creamos una lista vacía que es donde irán los números de nuestro archivo.
#3. Abrimos el archivo con 'with' indicando los parámetros donde está ubicado.
# NOTA: agregamos ENCODING para manejar caracteres especiales.

def read():
  numbers = [] #2
  with open("./archivos/numbers.txt", "r", encoding="utf-8") as f: #3
    for line in f: #con un ciclo for vamos a leer cada linea de un archivo
      numbers.append(int(line)) #convertimos lo que está en la lista a un número
  print(numbers)

# NOTA
# El 2do parámetro define el modo en el que trabajamos con el archivo.

def write():
  pass

def run():
  read() #1

if __name__ == '__main__':
  run()