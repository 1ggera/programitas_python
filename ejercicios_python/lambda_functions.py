# Lambda functions: son funciones anónimas. Son funciones que no tienen nombre identificaador.
print("lambda argumentos:expresión") # agregamos la expresión sin  dejar un espacio.
# Ya no usamos 'def' sino lambda.
# Pueden tener varios argumentos pero solo una linea de código. 
# No hace falta escribir la palabra 'return'. Automáticamente devuelve un resultado.

#Retomando un proyecto que evalúa si una palabra es palindromo o no
palindrome = lambda string:string == string[::-1]
print(palindrome('ana'))
# Aquí declara una variable que guarda el objeto de tipo función que retorna toda esta expresión de python.

#NOTA:
# palindrome: es una variable que tiene un nombre identificador. No es de la función. Es de la variable que va a contener el objeto de tipo función que retorna esta función anónima.
# lambda string: hace de argumento
# string == string[::-1]

#Tambien podría funcionar así:

#  def palindrome(string):
#    return string == string[::-1]

#  print(palindrome('ana'))

