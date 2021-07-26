#Assert statements (afirmaciones):

# assert condición, mensaje de error
# afirmo qué la condición X es verdadera, sinó, imprime este mensaje de error.

# Son expresiones que combinan variables con operadores.
# Son otra forma de manejar los errores. 

# código > Assert statement > si se cumple    > ejecuta el código
#                             si no se cumple > emite un error: "AssertionError"

# Probamos aplicarlo en el ejemplo del palíndromo
def palindrome(string):
  assert len(string) > 0, "No se puede ingresar una cadena vacía" #aquí decimos: afirmo qué el 'string' tiene más de cero caracteres, sinó, emite el siguiente mensaje 
  return string == string[::-1]
  #así programado nos imprimirá AssertionError
print(palindrome(""))
