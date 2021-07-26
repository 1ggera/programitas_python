#List comprenhensions es una estructura de Python que se usa para crear nuevas listas.
# reto 3: elevar al cuadrado los primeros 100 números naturales.
def run():
  lista = [] #creamos
  for i in range(1, 101): #El RANGE en un FOR tiene su último parámetro de manera no inclusiva.
    lista.append(i**2) #el atributo 'append' es para agregar cosas a nuestra lista.

  print("100 números elevados al duadrado")
  print(lista)
  print()

  lista2 = []
  for i in range(1, 101):
    if i % 3 != 0:
      lista2.append(i**2)

  
  lista2_ = [i**2 for i in range(1, 101) if i % 3 != 0]
  print("100 números elevados a cuadrado que no sean divisibles por 3")
  print(lista2)
  print("Misma lista pero escrita en una sola línea de código")
  print()
  print(lista2_)


  print()
  print("Lista del 1 al 100000 con números elevados al cuadrado divisibles por 4, 6 y 9.")

  lista3 = [i**2 for i in range(1, 100000) if i % 4 != 0 and i % 6 != 0 and i % 9 != 0]
  print(lista3)

if __name__ == '__main__':
  run()