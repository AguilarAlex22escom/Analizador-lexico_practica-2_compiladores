from ast import pattern
from lib import expresiones_regulares
import re

def leerArchivos():
    archivos = input("Ingrese el programa a análizar: ") # "el archivo donde se guardará la tabla de símbolos y el archivo donde se encontrarán los errores: ")    # En la primer versión del programa solo se trabaja para leer el programa en c.    
    FILE = open(archivos, 'r') # Apertura del archivo en modo lectura.
    print(FILE.readable()) # Indica si se puede abrir el archivo en modo lectura.
    # print(FILE.read()) # Convierte el contenido del archivo en una cadena.
    # print(FILE.readlines()) # Guarda cada línea del contenido del archivo en un índice de una lista.
    for line in FILE:
        print(line) # Imprime el programa línea por línea.
    FILE.close() # Cierra el archivo.

leerArchivos()



# Textos de referencia:

# https://www.freecodecamp.org/espanol/news/python-abre-archivo-como-leer-un-archivo-de-texto-linea-por-linea/
# https://platzi.com/blog/expresiones-regulares-python/
# https://platzi.com/contributions/entendiendo-las-expresiones-regulares-con-python/
# https://platzi.com/blog/como-funcionan-expresiones-regulares/
