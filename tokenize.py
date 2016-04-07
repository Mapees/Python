# Dado un archivo tokeniza su contenido y lo muestra en la consola
# Modo de uso: python3 tokenize.py <file_input>

# Librerias
import re
import sys


# Reglas tokenizar
fechas = "(\d{2}(/|-)\d{2}((/|-)\d{4})?)"
simbolos = "(\(|\)|\.\.\.|\.|\,|\'|\"|\?|\¿|\!|\¡|\,|;|:|\%)"
numeros = "\d*[.,\/]\d+"
horas = "\d+[:]\d*"
webs = "(http://)[/.~\w+]+[/~\w+]+"
email = "(\w+[.|\w])*@(\w+[.])*\w+"
texto = "\w+(\-\w+)*"


reglas = fechas + "|" + simbolos  + "|" + numeros + "|" + horas + "|" + email + "|" + webs + "|" + texto
    
# Argumentos de entrada
if len(sys.argv) >= 2:
        file_name = sys.argv[1]
else:
        print ("El uso del programa es tokenize.py <fichero_entrada>");

# Función de tokenizar

def tokenize(line):
    result = re.compile( reglas , re.U | re.I)
    matches = re.finditer(result, line)
    print (line)
    for i in matches:
        print (line[i.start():i.end()])

# Leer fichero
try:
    with open (file_name, 'r') as f:
        for line in f:
            tokenize(line)
except EnvironmentError:
    print ('Archivo no encontrado.')
  
