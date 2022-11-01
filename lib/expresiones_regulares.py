import re 

lexema_identificador = re.compile('.+')
lexema_tipoDeDato = re.compile('void\s.+|int\s.+|float\s.+|double\s.+|char\s.+')
lexema_comparacion = re.compile('=|==|<|>|===')
lexema_comparacion_estructuras = re.compile('==|!=|<=|>=')
lexema_funcion = re.compile('void\s+.+\(.*\)\s*\{?|int\s+.+\(.*\)\s*\{?|float\s+.+\(.*\)\s*\{?|double\s+.+\(.*\)\s*\{?|char\s+.+\(.*\)\s*\{?')
# lexema_while = re.compile('while\s*\(\w+=\w+|\w+==\w+|\w+!=\w+|\w+<\w+|\w+>\w+|\w+<=\w+|\w+>=\w+|\w+===\w+\)\s*\{?')

funcion_prueba = 'int main() {'
bucle_prueba = 'while(x <= y) {'
print(lexema_funcion.findall(funcion_prueba)) # Aceptado por el patrón.
print(lexema_comparacion_estructuras.findall(bucle_prueba))

# Datos.

# lexema_identificador = re.compile('(\w)+(\w)*?')
# lexema_numerico = re.compile('([0-9])+(".")?([0-9])*?')
# lexema_booleano = re.compile('true|false')
# lexema_caracter = re.compile("'(lexema_identificador{1})?'|' '")
# lexema_cadena = re.compile('"lexema_identificador{2,}"')

# # Operadores.

# lexema_comparacion = re.compile('=|==|!=|<|>|<=|>=|===')
# lexema_incremento = re.compile('(lexema_identificador)(++|--)')
# lexema_matematico = re.compile('+|-|"*"|"**"|/|%')
# lexema_logico = re.compile('&&|"||"|!')
# lexema_asignacion = re.compile('+=|-=|*=|/=')

# # Palabras reservadas.

# lexema_tipoDeDato = re.compile('void|int|float|double|char')
# lexema_calificador = re.compile('short|long|signed|unsigned')
# # lexema_tipoDeDato = re.compile('(void|int|float|double|char) lexema_identificador (=" *"?(lexema_cadena|lexema_numerico))?')
# lexema_if = re.compile('if" *"?(((lexema_identificador)(==|<|>|<=|>=|===|!=)(lexema_identificador))|(lexema_numerico))')
# lexema_else = re.compile('else" *"?(lexema_if)?')
# lexema_for = re.compile('for" *"?(((lexema_identificador)=(lexema_identificador))?;((lexema_identificador)(<|>|<=|>=|===|!=)(lexema_identificador))?;((lexema_incremento)))')
# lexema_while = re.compile('while" *"?(((lexema_identificador)(lexema_comparacion)(lexema_identificador))|(lexema_numerico))')
# lexema_switch = re.compile('switch" *"?(lexema_identificador)')

# Símbolos especiales
