#Reto
# 1. Imprimir los números del 1 al 100 elevandolos al cuadrado.
# 2. Guardar solo los resultados que no sean divisibles entre 3

def run():
  squares = []
  #usamos range para imprimir un rango determinado
  for i in range(1, 101):
    squares.append(i**2)  
  #usamos append para agregar un resultado a la lista q estamos imprimiendo. En este lo agregamos potenciado al cuadrado.
  print(squares)

  print()

  #Aquí usaremos una sola linea de código para decir que se impriman los números al cuadrado del rango 1 al 101 que NO son divisibles por 3
  squares2 = [i**2 for i in range(1, 101) if i % 3 != 0]
  print(squares2)

  print()

  print("ELEMENT for ELEMEMT in ITERABLE if CONDITION")
  print("Elemento para cada elemento, en el iterable, solo si: la condición")
if __name__ == '__main__':
  run()

# NOTA: En un LIST COMPRENHENSION el CICLO es obligatorio.