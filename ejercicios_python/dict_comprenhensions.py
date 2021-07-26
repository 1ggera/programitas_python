def run():
  my_dict = {}

  print("Diccionario que eleva los primeros 100 números naturales al cubo")
  for i in range(1, 101): #a) Para cada i en el rango de 1 a 101
    if i % 3 != 0:  #c) solo si i dividido por 3 da como resultado cero
      my_dict[i] = i**3 #b) vamos a guardar la i elevada al cubo 
  print(my_dict)

  print("Diccionario que eleva los primeros 100 números naturales al cubo pero en una sola linea de código")
  my_dict2 = {i: i**3 for i in range(1, 101) if i % 3 != 0}
  print(my_dict2)
  

if __name__ == '__main__':
  run()

# NOTA: En un DICTIONARY COMPRENHENSION la condición (if) es opcional.