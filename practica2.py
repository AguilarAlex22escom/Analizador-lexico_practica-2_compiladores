from ast import pattern
from lib import expresiones_regulares
import re

# Lexemas importantes.

lexema_identificador = re.compile('[A-z]+[0-9]*[A-z]*')

lexema_estructura_selectiva = re.compile('if|else|switch|case')
lexema_estructura_repetitiva = re.compile('for|while|do')
lexema_tipo_de_dato = re.compile('void|int|float|double|char')
lexema_calificador = re.compile('short|long|signed|unsigned')
lexema_instruccion_preprocesador = re.compile('include|define')
lexema_main_return = re.compile('main|return')

lexema_numero = re.compile('[0-9]+\.?[0-9]*')

lexema_aritmetico = re.compile('\+|\-|\/|\*|\%')
lexema_logico = re.compile('&&|\|\||\!')
lexema_comparacion = re.compile('==|<|>|===|>=|<=|!=')
lexema_asignacion = re.compile('=|\+=|\-=|\*=|\/=')
lexema_incremento = re.compile('\+\+|\-\-')

lexema_simbolo_especial = re.compile('\s*\(|\)|\s*\{\w*\}|\s*\[\w*\]|\s*;|\s*,\s*|\s*\'\w*|\s*\“')

# Lexemas especiales para reconocimiento de estructuras.

multilista = []
identificadores_hallados = []
tipos_de_datos_hallados = []

i = 0

def leerArchivos():
    archivos = input("Ingrese el programa a análizar: ")
    with open(archivos, 'r') as FILE:
        for lines in FILE:
            multilista.append(lines.split())
            print(multilista[len(multilista)-1])
    FILE.close() # Cierra el archivo.

def hallar_identificadores():
    print('Identificadores: ')
    for listas in multilista:
        for cadenas in listas:
            identificadores_hallados = lexema_identificador.findall(cadenas)
            if identificadores_hallados != []:
                if identificadores_hallados != lexema_tipo_de_dato.findall(cadenas):
                    if identificadores_hallados != lexema_estructura_repetitiva.findall(cadenas) and identificadores_hallados != lexema_estructura_selectiva.findall(cadenas):
                        if identificadores_hallados != lexema_instruccion_preprocesador.findall(cadenas):
                            if identificadores_hallados != lexema_main_return.findall(cadenas):
                                for identificador in identificadores_hallados:
                                    print(identificador)
                                    SIMBOLS_FILE.write('Identificador\t|' + identificador + '\t| ' + identificador.upper() + '\n')
def hallar_estructuras_selectivas():
    print('Estructuras selectivas: ')
    for listas in multilista:
        for cadenas in listas:
            estructuras_selectivas_halladas = lexema_estructura_selectiva.findall(cadenas)
            if estructuras_selectivas_halladas != []:
                for estructura_selectiva in estructuras_selectivas_halladas:
                    print(estructura_selectiva)
                    SIMBOLS_FILE.write('Estructura selectiva\t|' + estructura_selectiva + '\t| ' + estructura_selectiva.upper() + '\n')
def hallar_estructura_repetitiva():
    print('Estructuras repetitivas: ')
    for listas in multilista:
        for cadenas in listas:
            estructuras_repetitivas_halladas = lexema_estructura_repetitiva.findall(cadenas)
            if estructuras_repetitivas_halladas!= []:
                for estructura_repetitiva in estructuras_repetitivas_halladas:
                    print(estructura_repetitiva)
                    SIMBOLS_FILE.write('Estructura repetitiva\t|' + estructura_repetitiva + '\t| ' + estructura_repetitiva.upper() + '\n')
            #     print(estructuras_repetitivas_halladas)
def hallar_tipos_de_datos():
    print('Tipos de datos: ')
    for listas in multilista:
        for cadenas in listas:
            global tipos_de_datos_hallados 
            tipos_de_datos_hallados = lexema_tipo_de_dato.findall(cadenas)
            if tipos_de_datos_hallados!= []:
                for tipo_de_dato in tipos_de_datos_hallados:
                    print(tipo_de_dato)
                    SIMBOLS_FILE.write('Tipos de datos\t|' + tipo_de_dato + '\t| ' + tipo_de_dato.upper() + '\n')
def hallar_calificadores():
    print('Calificadores: ')
    for listas in multilista:
        for cadenas in listas:
            calificadores_hallados = lexema_calificador.findall(cadenas)
            # if calificadores_hallados!= []:
            #     print(calificadores_hallados)
def hallar_instrucciones_preprocesador():
    print('Instrucciones preprocesador: ')
    for listas in multilista:
        for cadenas in listas:
            instrucciones_preprocesador_halladas = lexema_instruccion_preprocesador.findall(cadenas)
            # if instrucciones_preprocesador_halladas!= []:
            #     print(instrucciones_preprocesador_halladas)
def hallar_main_return():
    print('Main y return: ')
    for listas in multilista:
        for cadenas in listas:
            main_return_hallados = lexema_main_return.findall(cadenas)
            # if main_return_hallados!= []:
            #     print(main_return_hallados)
def hallar_numeros():
    print('Números: ')
    for listas in multilista:
        for cadenas in listas:
            numeros_hallados = lexema_numero.findall(cadenas)
            # if numeros_hallados != []:
            #     print(numeros_hallados)
def hallar_simbolos_aritmeticos():
    print('Símbolos aritmeticos: ')
    for listas in multilista:
        for cadenas in listas:
            simbolos_aritmeticos_halladas = lexema_aritmetico.findall(cadenas)
            # if simbolos_aritmeticos_halladas!= []:
            #     print(simbolos_aritmeticos_halladas)
def hallar_simbolos_logicos():
    print('Símbolos lógicos: ')
    for listas in multilista:
        for cadenas in listas:
            simbolos_logicos_hallados = lexema_logico.findall(cadenas)
            # if simbolos_logicos_hallados != []:
            #     print(simbolos_logicos_hallados)
def hallar_simbolos_comparacion():
    print('Símbolos de comparación: ')
    for listas in multilista:
        for cadenas in listas:
            simbolos_comparacion_hallados = lexema_comparacion.findall(cadenas)
            if simbolos_comparacion_hallados!= []:
                print(simbolos_comparacion_hallados)
def hallar_simbolos_asignacion():
    print('Símbolos de asignación: ')
    for listas in multilista:
        for cadenas in listas:
            simbolos_asignacion_hallados = lexema_asignacion.findall(cadenas)
            # if simbolos_asignacion_hallados != []:
            #     print(simbolos_asignacion_hallados)
def hallar_simbolos_incremento():
    print('Símbolos de incremento: ')
    for listas in multilista:
        for cadenas in listas:
            simbolos_incremento_hallados = lexema_incremento.findall(cadenas)
            # if simbolos_incremento_hallados!= []:
            #     print(simbolos_incremento_hallados)
def hallar_simbolos_especiales():
    print('Símbolos especiales: ')
    for listas in multilista:
        for cadenas in listas:
            simbolos_especiales_hallados = lexema_simbolo_especial.findall(cadenas)
            # if simbolos_especiales_hallados!= []:
            #     print(simbolos_especiales_hallados)
def enviar_lexemas(): # Elimina los lexemas que se repitan en dos o más tipos de token.
    tabla_simbolos = input("Ingrese el archivo donde se hallará la tabla de símbolos: ")
    global SIMBOLS_FILE
    with open(tabla_simbolos, 'w') as SIMBOLS_FILE:
        SIMBOLS_FILE.write('Componente Léxico\t| Lexema\t| Valor\n')
        hallar_identificadores()
        hallar_estructuras_selectivas()
        hallar_estructura_repetitiva()
        hallar_tipos_de_datos()
'''
    # Bloques de código distintos.           
    archivos = input("Ingrese el programa a análizar: ") # "el archivo donde se guardará la tabla de símbolos y el archivo donde se encontrarán los errores: ")    # En la primer versión del programa solo se trabaja para leer el programa en c.    
    FILE = open(archivos, 'r') # Apertura del archivo en modo lectura.
    print(FILE.readable()) # Indica si se puede abrir el archivo en modo lectura.
    # print(FILE.read()) # Convierte el contenido del archivo en una cadena.
    # print(FILE.readlines()) # Guarda cada línea del contenido del archivo en un índice de una lista.
    # FILE.readlines()
    
    for line in FILE:
        multilista.append(line.strip('\n'))
        print(multilista) # Imprime el programa línea por línea. 
    '''

if __name__ == '__main__':
    leerArchivos()
    print('Lexemas encontrados:')
    hallar_calificadores()
    hallar_instrucciones_preprocesador()
    hallar_numeros()
    hallar_simbolos_aritmeticos()
    hallar_simbolos_logicos()
    hallar_simbolos_comparacion()
    hallar_simbolos_asignacion()
    hallar_simbolos_incremento()
    hallar_simbolos_especiales()
    enviar_lexemas()
# Textos de referencia:

# https://www.freecodecamp.org/espanol/news/python-abre-archivo-como-leer-un-archivo-de-texto-linea-por-linea/
# https://platzi.com/blog/expresiones-regulares-python/
# https://platzi.com/contributions/entendiendo-las-expresiones-regulares-con-python/
# https://platzi.com/blog/como-funcionan-expresiones-regulares/
