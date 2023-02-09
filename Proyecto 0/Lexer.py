"""No vamos a usar librerias, gracias:"""
"""q cabron"""

#Documentacion
"""Comentarios por desarrollar"""

"""

Completar dicionario: 
formato:

PALABRA EN MINUSCULAS = TOKEN 

"""
DiccionarioTokens = {
    "ROBOT_R" : "PR",
    #PR = Programa Robot
    "VARS" : "V",
    #V = Variables
    "PROCS" : "DP",
    #DP = Declaracion de procedimiento
    "while" : "WHILE",
    #WHL = Ciclo while
    "assignTo" : "ASSIGNTO"
    #assingTo = name donde name es el nombre de una variable y n es un número. 
    # El resultado de esta instrucción es asignar el valor del número a la variable. 
    





}


def leer_archivo(nombre_archivo):
    with open(nombre_archivo, 'r') as archivo:
        contenido = archivo.read()
        palabras = contenido.split()
        return palabras

#devuelve una lista de las palabras contenidas en el archivo.

def lexer(palabras, diccionario):
    tokens = []
    for palabra in palabras:
        if palabra in diccionario:
            tokens.append((palabra, diccionario[palabra]))
        else:
            tokens.append((palabra, 'UNKNOWN'))
    return tokens

#Una lista de palabras y un diccionario que asigna tokens a las palabras. 
#La función itera sobre la lista de palabras y comprueba si cada palabra está en el diccionario. 
#Si la palabra está, agrega una tupla a la lista tokens que incluye la palabra y su token correspondiente. 
#Si la palabra no está, la función agrega una tupla que incluye la palabra y el token "UNKNOWN". 
#Finalmente, la función devuelve la lista de tokens.


        

