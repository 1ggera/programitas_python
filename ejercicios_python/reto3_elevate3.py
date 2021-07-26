def run():
  my_dict = {}

#  for i in range(1, 101): #De el siguiente rango
#    if i % 3 != 0 #si los números divisibles por 3 dan cero
#      my_dict[i] = i**3 #guardarlos en 'my_dict'
#  print(my_dict)

  #Ahora haremos lo mismo pero en una sola linea de código
  my_dict2 = {i: i**3 for i in range(1, 101) if i % 3 != 0} #la diferencia es que al comenzar el diccionario debemos agregar 'i:'
  print(my_dict2)

if __name__ == '__main__':
  run()

  