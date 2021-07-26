# Una función de orden superior es una función que recibe como parámetro a otra función.

def saludo(func):
  func()

def hola():
  print("Hola!!")

def adios():
  print("Adios!!!")

saludo(hola)
saludo(adios)
print()
# Existen 3 ordenes de orden superior que son muy importantes en muchos lenguajes de programación. FILTER, MAP, REDUCE.

# FILTER
# De una lista de números aleatorios debemos obtener solo los números impares.
# Vamos a declarar la lista 

#resuelto con 'list comprenhension'
my_list_1 = [1, 2, 3, 4, 6, 8, 9, 11, 15, 19, 21]
odd1 = [i for i in my_list_1 if i % 2 != 0] 
print(odd1)
print()

#resuelto con 'filter'
#En este caso la lista2 es tomada como parametro2, es procesada por el parámetro1 (una función lambda) que filtra los resultados a mostrar y los tiene listos para mostrar.
#Finalmente los imprime con 'list'
my_list2 = [1, 4, 5, 6, 9, 11, 15, 19, 21, 23, 25]
odd2 = list(filter(lambda x: x%2 != 0, my_list2)) 
print(odd2)
#Filter recibe dos parámetros. Una función (puede ser una lambda) y un iterable (cualquier elementos que pueda recorrerse).

#1er parámetro: 'lambda x: x%2 !=0' solo recibe un número y si es par devuelve un True o False.
#2do parámetro: my_list2. Es un iterable. En Python un iterable es cualquier elemento que puede recorrerse. 
#De todas formas así como está armada nos devuelve un iterador. Un tipo de objeto especial.
#Para obetener nuestra lista colocamos la función 'list' envolviendo a 'filter'.

#MAP
#Vamos elevar al cuadrado los números de una lista.

#Resuelto con 'list comprenhensions'
list = [1, 5, 8, 7, 11]
squares = [i**2 for i in my_list]
print(squares)

#Resuelto con Map
lista1 = [1, 8, 9, 15, 22]
squares = list(map(lambda x: x**2, lista1))
print(squares)
#Entonces tenemos a nuestra lista original
#colocamos 'list' envolviendo a todo, map envolviendo nuestra función como 1er parámetro y a nuestra lista como 2do parámetro
#la función lambda recibe el parámetro X y retorna el resultado de X elevado al cuadrado.
#Este código va a recorrer los elementos de la lista, los elevará al cuadrado y los guardará en una nueva lista llamada 'squares'

#REDUCE
#Para reducir los valores de una lista a un único valor.

#Resuelto con FOR
lista1 = [2, 2, 2, 2, 2]
all_multiplied = 1
for i in my list:
  all_multiplied = all_multiplied * i
print(all_multiplied)
#En esta operación recorre cada elemento con un FOR cada elemento de la lista.
#En cada iteración guarda el número multiplicado por i

#Resuelto con REDUCE
#Para resolver con REDUCE debemos importar la función REDUCE del módulo FUNCTOOLS
from functools import reduce
lista2 = [2, 2, 2, 2, 2]
all_multiplied = reduce(lambda a, b: a * b, lista2)
print(all_multiplied)
#Aquí el resultado será 32
#Los parámetro a y b hacen de 1er y 2do parámetro. Los multiplica y guarda el 1er resultado en a y luego agarra el siguiente elemento de la lista, lo guarda en b y lo multiplica por a. Y así hasta agotar todos los elementos de la lista.
#La función REDUCE devuelve un elemento único.

