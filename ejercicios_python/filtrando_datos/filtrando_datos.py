#La lista está compuesta por diccionarios anidados. Cada diccionario se llamará 'worker'


DATA = [ ## <-- DATA es una constante. Cuando usamos una variable en mayusculas significa que no esperamos modificarla.
    {
        'name': 'Facundo',
        'age': 72,
        'organization': 'Platzi',
        'position': 'Technical Coach',
        'language': 'python',
    },
    {
        'name': 'Luisana',
        'age': 33,
        'organization': 'Globant',
        'position': 'UX Designer',
        'language': 'javascript',
    },
    {
        'name': 'Héctor',
        'age': 19,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'ruby',
    },
    {
        'name': 'Gabriel',
        'age': 20,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'javascript',
    },
    {
        'name': 'Isabella',
        'age': 30,
        'organization': 'Platzi',
        'position': 'QA Manager',
        'language': 'java',
    },
    {
        'name': 'Karo',
        'age': 23,
        'organization': 'Everis',
        'position': 'Backend Developer',
        'language': 'python',
    },
    {
        'name': 'Ariel',
        'age': 32,
        'organization': 'Rappi',
        'position': 'Support',
        'language': '',
    },
    {
        'name': 'Juan',
        'age': 17,
        'organization': '',
        'position': 'Student',
        'language': 'go',
    },
    {
        'name': 'Pablo',
        'age': 32,
        'organization': 'Master',
        'position': 'Human Resources Manager',
        'language': 'python',
    },
    {
        'name': 'Lorena',
        'age': 56,
        'organization': 'Python Organization',
        'position': 'Language Maker',
        'language': 'python',
    },
]

#Vamos a filtrar los datos de las personas que cumplan con determinada caracteristica. Puede ser los que tengan X años, los que sepan Python, o que trabajen en X lugar. 

#Primero creamos una lista. Que contendrá los nombres de los trabajadores.
#Definimos que los diccionarios de DATA se llaman worker.

def run():
  all_python_devs = [worker["name"] for worker in DATA if worker["language"] == "Python"]
  #así definimos que para todos los diccionarios de la lista DATA, vamos a guardar solo el contenido de la llave nombre, solo sí worker["languaje"] == "python"
  #Es decir, de todos los trabajadores de DATA, voy a guardar el nombre, solo si domina Python.
  
  all_Platzi_Workers = [worker["name"] for worker in DATA if worker ["organization"] == "Platzi"]
  #así nos llevamos los 'name' de los 'worker' de DATA de las personas que trabajan en Platzi.

  adults = list(filter(lambda worker: worker["age"] > 18 , DATA))
  #Acá hacemos una lista con los nombre de todos los adultos mayores de 18 años usando 'filter'. Combinamos HIGH ORDER FUNCTIONS CON FUNCIONES ANÓNIMAS. NOTA: Si dejamos este bloque así nos imprimirá el diccionario completo.
  adults = list(map(lambda worker: worker["name"], adults))
  #hacemos esto para llevarnos el 'name' la variable 'adults'

  #Ahora crearemos una nueva lista de diccionarios que tenga una llave más que indique si la persona es mayor a 70 años o menor indicando TRUE o FALSE.
  old_people = list(map(lambda worker: worker | {"old": worker["age"] > 70}, DATA))
  
  # RETO
  #1. CREAR lista all_python_devs Y all_Platzi_Workers COMBINANDO FILTER y MAP.
  #2. CREAR lista old_people Y adults aplicando LIST COMPREHENSIONS.

 # 1 Lista que imprime el diccionario completo
  all_python_devs2 = list(filter(lambda worker: worker["language"] == "python", DATA))
#Lista que imprime solo los nombres de los devs
  python_devs = list(map(lambda worker: worker["name"], all_python_devs2))

 # 2 Imprime los diccionarios completos de los mayores a 60
  adults2 = [worker for worker in DATA if worker ["age"] > 60]
#Imprime los diccionarios + el 'worker old' y si es mayor a 30 entonces es TRUE sino será FALSE
#Caso 1: con ** ** y eliminando el IF
  old_people2 = [{**worker, **{'old': worker['age'] > 30}} for worker in DATA]
#Caso 2: con | (pipe) y eliminando el IF. Verifica con TRUE o FALSE si es mayor a 70
  old_people3 = [worker | { "old": worker["age"] > 70} for worker in DATA]

#Ahora creamos un ciclo para ver el resultado
  for worker in old_people2:
    print(worker)

if __name__ == '__main__':
  run()
