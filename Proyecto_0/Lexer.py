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
    "assignTo" : "CAT",
    #CAT = Comand assignTo
    "goto" : "CGT",
    #CGT = Comand goTo
    "move" : "CM",
    #CM = Comand move
    "turn" : "CT",
    #CT = Comand turn
    "while" : "WHL",
    #WHILE = Ciclo while
    "face" : "CF",
    #CF = Comand face
    "put" : "CPUT",
    #CPUT = Comand put
    "pick" : "CPICK",
    #CPICK = Comand pick
    "moveToThe" : "CMTT",
    #CMTT = Comand moveToThe
    "moveInDir" : "CMDIR",
    #CMDIR = Comand moveInDir
    "jumpToThe" : "CJTT",
    #CJTT = Comand jumpTothe
    "jumpInDir" : "CJDIR",
    #CJDIR = Comand jumpInDir
    "if" : "IF",
    "else" : "ELSE",
    "elseif" : "ELSEIF",
    "elif" : "ELSEIF",
    "then" : "THEN",
    "(" : "POPEN",
    ")" : "PCLOSE",
    ":" : "DOSPUNTOS",
    ";" : "PYC",
    "[" : "COPEN",
    "]" : "CCLOSE",
    "{" : "KOPEN",
    "}" : "KCLOSE"  

}

#FUNCIONES AUXILIARES 

def insert_char_at_index(string, char, index):
    return string[:index] + char + string[index:]

def leer_archivo_to_str(file_path):
    with open(file_path, 'r') as file:
        text = file.read()
    return text.lower()

def modificar_str(text):
    copyText = text
    centinelaPequenio = False 
    centinelaGrande = False
    posicion = 0
    
    while centinelaGrande == False and posicion <= len(copyText)-1:
        i = posicion
        while centinelaPequenio == False and posicion <= len(copyText)-1:
            if copyText[i] == "[" or copyText[i] == "]":
                if i != len(copyText)-1 and i != 0:
                    insert_char_at_index(copyText, " ",i-1)
                    insert_char_at_index(copyText, " ",i+1)
                    centinelaPequenio = True
                    posicion = i-1
            i += 1
            
    return copyText
        
    
            

            
    




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
            tokens.append((palabra, ""))
    return tokens

#Una lista de palabras y un diccionario que asigna tokens a las palabras. 
#La función itera sobre la lista de palabras y comprueba si cada palabra está en el diccionario. 
#Si la palabra está, agrega una tupla a la lista tokens que incluye la palabra y su token correspondiente. 
#Si la palabra no está, la función agrega una tupla que incluye la palabra y el token "UNKNOWN". 
#Finalmente, la función devuelve la lista de tokens.


print(open("./Proyecto_0/prueba_archivo.txt").read())

