#Una lista puede guardar diccionarios y los diccionarios pueden guardar listas.

#creamos nuestra función principal
def run():
  my_list = [1, "Hello", True, 4.5]
  my_dict = {"firstname": "Gerard", "lastname": "García"}

  super_list = [
    {"firstname": "Gerard", "lastname": "García"},
    {"firstname": "Alberto", "lastname": "Sputnikandez"},
    {"firstname": "Confinamiento", "lastname": "Confinatorio"},
    {"firstname": "Nomelacon", "lastname": "Tactoextraterrestre"},
    {"firstname": "Nomela ", "lastname": "Concordia"}
  ]

  super_dict = {
    "natural_nums": [1, 2, 3, 4, 5],
    "integer_nums": [-1, -2, 0, 1, 2],
    "floating_nums": [1.1, 4.5, 6.45]
  }

  #este ciclo recorrera las laves y valores con el método .items()
  for key, value in super_dict.items(): #items nos permite recorrer las llaves y valores al mismo tiempo de un diccionario en un ciclo.
    print(key, "-", value)
  
  print()
  
  for item in super_list:
    print(item["firstname"] , "-", item["lastname"])
  
if __name__ == '__main__':
  run()