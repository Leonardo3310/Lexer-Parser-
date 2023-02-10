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
    "robot_r" : "PR",
    #PR = Programa Robot
    "vars" : "V",
    #V = Variables
    "procs" : "DP",
    #DP = Declaracion de procedimiento
    "assignto" : "CAT",
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
    "movetothe" : "CMTT",
    #CMTT = Comand moveToThe
    "moveindir" : "CMDIR",
    #CMDIR = Comand moveInDir
    "jumptothe" : "CJTT",
    #CJTT = Comand jumpTothe
    "jumpindir" : "CJDIR",
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
    "}" : "KCLOSE",
    "=" : "EQ",
    "==": "COMPARE",
    "<=": "EQL",
    ">=": "EQM",
    "|" : "PALITO",
    "," : "COMA"
    
}

#FUNCIONES AUXILIARES 

def read_file_and_format(file_path):
    with open(file_path, 'r') as file:
        text = file.read()
    text = text.lower()
    text = text.replace('(', ' ( ')
    text = text.replace(')', ' ) ')
    text = text.replace('[', ' [ ')
    text = text.replace(']', ' ] ')
    text = text.replace(':', ' : ')
    text = text.replace(';', ' ; ')
    text = text.replace("|", ' | ')
    
    return text
        
def lexer(text, tokens):

    words = text.split()
    result = []
    for word in words:
        if word in tokens:
            result.append(tokens[word])
        else:
            result.append("WORD")
    return ' '.join(result)

print(lexer(read_file_and_format("./Proyecto_0/prueba_archivo.txt"),DiccionarioTokens))

def parse(tokens_str):
    tokens = tokens_str.split()
    i = 0
    if tokens[i] != "PR":
        return "Error: First token must be 'PR'"
    i += 1

    if i < len(tokens) and tokens[i] == "V":
        i += 1
     
        while i < len(tokens) and tokens[i] == "WORD":
            i += 1
            if i < len(tokens) and tokens[i] == "COMA":
                i += 1
            else:
                break
    #procedure tokens
    while i < len(tokens):
        
        if tokens[i] not in ["CAT", "CGT", "CM", "CT", "CF", "CPUT", "CPICK", "CMTT", "CMDIR", "CJTT", "CJDIR"]:
            return f"Error: token '{tokens[i]}'"
        i += 1
        
        if i < len(tokens) and tokens[i] != "DOSPUNTOS":
            return f"Error: 'DOSPUNTOS' after '{tokens[i-1]}'"
        i += 1
    
    return "Success"

print(parse(lexer(read_file_and_format("./Proyecto_0/prueba_archivo.txt"),DiccionarioTokens)))
