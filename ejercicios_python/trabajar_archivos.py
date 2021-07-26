#Manejar archivos
#Los archivos de texto contienen bytes que solo representan letra y simbolos. Los archivos binarios tienen bytes que representan cosas mas complejas como datos de imágenes y videos.
#Los binarios solo los vamos a editar con programas específicos para ello.
#Con Python trabajaremos sobre los archivos de texto. (.xml  .json .py  .txt  .css  .js .csv).

# Modos de apertura:
# R -> Lectura.
# W -> Escritura (sobreescribir).
# A -> Escritura (Agregar al final) 'MODO APPEND'.

# Para leer, escribir y sobreescribir debemos memorizar y entender esta línea

  with open("./ruta/del/archivo.txt", "r") as f:

# with: es un manejador contextual. Controla el flujo de nuestro archivo haciendo que, si el programa se cierra o el script finaliza inesperadamente, el archivo no se rompa.

# open: abre un archivo

# ruta: es una parámetro donde está ubicado el archivo.

# r: es el modo de apretura

# as: para asignar un nombre mas sencillo a lo que estamos trabajando dentro del programa

# f: nombre asignado al archivo

