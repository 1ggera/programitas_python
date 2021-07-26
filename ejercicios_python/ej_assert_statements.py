#Solucionaremos el error de ingresar una letra en el programa que emite los divisores.

#1. Agregamos una linea de código que contiene un método de las 'strings' que devuelve 'True' si ese string es un número y 'False' si no lo es.
#2. Pa

def divisors(num):
  divisors = []
  for i in range(1, num + 1):
    if num % i == 0:
      divisors.append(i)
  return divisors

def run():
# #num = int(input("Ingresa un número: "))
  num = input("Ingresa un número: ") #2. dejamos de combertir a entero en esta línea
  assert num.isnumeric() and int(num) > 0, "Debes ingresar un número mayor a cero" # 1. Afirmo que el dato que ingrese el usuario es numérico, sinó, mostrar el siguiente mensaje.
  print(divisors(int(num))) #3. convertimos a entero cuando enviamos ese número a la función divisors
  print("Terminó mi programa")



if __name__ == '__main__':
  run()