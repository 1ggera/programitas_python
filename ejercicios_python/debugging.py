#El DEBUGGING está hecho para resolver las fallas del código cuando Python no nos avisa que nos equivocamos.

#Crearemos una función que recibe un n° como parámetro y retorna una lista con todos los divisores de ese número.

def divisors(num): #1) creamos la función que al ingresar un número retorne un resultado.
  divisors = [] #2) creamos una lista vacía
  for i in range(1, num + 1): #3) decimos que para el rango que va del 1 al mismo número, se escribe así porque el último parámetro no es inclusivo.
    if num % i == 0: #4) si el resto de la división es igual a 1
      divisors.append(i)  #5) vamos a agregar ese número a la lista de divisores
  return divisors #6) por último retornamos esos divisores.

#7) Luego en run() le pedimos el número al usuario
def run():
  num = int(input("Ingresa un número: ")) #usamos int para obtener un número entero. 
  print(divisors(num))# Este será procesado por la función 'divisors' e imprimiremos ese resultado
  print("Terminó mi programa")


if __name__ == '__main__':
  run()
#Este programa está hecho para que funcione mal.

#Entonces nos queda revisarlo línea por línea hasta encontrar el error usando DEBUGGING.
  #Run and Debug > Python File
  #Ahora tendremos habilitados los botones de Pause, Play, Saltar al paso siguiente, ingresar, salír, reiniciar y detener.
  #Luego de ingresar el número vamos a pulsar PAUSE. Esto permite ir paso por paso inspeccionando el código.
  #Para solucionar este programa debemos ingresar a la función 'divisors', cuando el debugger llegue a esa linea vamos pulsar 'ingresar' y al ver que se generó una lista vacía pulsamos otra vez 'paso siguiente'.
  #Cuando lleguemos al 'if' veremos que i:1 y num:5, entonces pulsamos 'paso siguiente' y veremos que no hay nada dentro de la lista.
  #Entonces nos damos cuenta que el error está en preguntar si el 'num % i == 1'.
  #Deberiamos preguntar si el 'num % i == 0' porque un número es divisor de otro número si la división es igual a cero.

#Breakpoints: puntos de quiebre. Nos sirven para pausar el debugging en una línea específica. 
  #Para crear un breakpoint colocamos un punto en la linea izquierda (el punto rojo).
  #Cuando python se ejecute, si en algún momento llega a ese breakpoint se detendrá.



#Solución en list comprehensions

# def divisors(num):
#    divisors = [i for i in range(1, num +1) if num % i == 0]
#    return divisors

# def run():
#    num = int(input('Ingresa un numero: '))
#    print(divisors(num))
#    print("Termino")

# if __name__ == '__main__':
#    run()


# # Manejo de errores
# Cuando python no emite mensaje de error entonces es que se programó mal.
# En un paso del algoritmo está fallando.
# Revisar el error de lógica. Una de las técnicas es debbuging.

# Cuando nos devuelve un TRACEBACK:

# Sintax error.
#   son los typos. Errores de escritura.
#   Estos detienen el programa y no se ejecuta ni siquiera la primer linea.
#   El motor de Python ve todas lineas de prinncipio a fin del código y si detecta error no corre el programa.

# Exceptions
#   Sí suceden en algún punto del programa y detecta toda la lógica.
#   IMPORTANTE:
#     Verificar en documentación todos los tipos de exceptions que existen.
#   Estos son algunos:
    
#     Keyboard interrupt:. Cuando pulsamos por error CTRL+C cortamos el proceso de python y todo se cierra. Entonces Python eleva una excepción desde dentro del programa hacia afuera.

#     Keyerror: cuando intentamos acceder a una llave en un diccionario inexistente.
#       ej: tenemos una llave con
#         first name
#         last name
#         age
#           pero intentamos acceder a la llave 'job' python nos arrojará un key error porque esa llave no existe.
    
#     IndexError: cuando estamos trabajando con listas e intentamos acceder a un índice que no existe.
#       ej: tenemos una lista con 5 elementos e intentamos acceder al elemento n°7.

#     FileNotFoundError: cuando intentamos abrir un archivo que no existe.

#     ZeroDivisionError: cuando intentamos dividir un número entre cero.

#     ImportError: cuando intentamos importar un módulo.

# Python muestra una exception mediante un TRACEBACK
  
#   Los TRACEBACK se leen desde atrás hacia adelante. En la última linea nos explica el error.

#   En la penúltima linea nos dice el archivo en el que sucedió ese error, la línea y el módulo en el que ocurrió.

#   Finalmente, en la primer línea nos dice con qué nos encontramos, un tracebak, y de donde parte el error. (most recent call last)
#     LA LLAMADA MAS RECIENTE ESTÁ AL FINAL.

#   Si el error ocurriese en una función interna pero no es solucionado, python elevaría ese error hasta la función 'run()'. Y si no es solucionado allí entonces detendría el programa.