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
    #Tokens Condicinales
    "(" : "POPEN",
    ")" : "PCLOSE",
    ":" : "DOSPUNTOS",
    ";" : "PYC",
    "[" : "COPEN",
    "]" : "CCLOSE",
    "{" : "KOPEN",
    "}" : "KCLOSE",
    "|" : "PALITO",
    "," : "COMA",
    #Tokens simbolos
    "=" : "EQ",
    "==": "COMPARE",
    "<=": "EQL",
    ">=": "EQM",
    #Tokens operadores logicos
    "*" : "MULTI",
    "+" : "SUMA",
    "-" : "RESTA",
    "/" : "DIV"
    #Tokens Operadores Aritmeticos
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
    text = text.replace("=", ' = ')
    text = text.replace("<=", ' <= ')
    text = text.replace(">=", ' >= ')
    text = text.replace("==", ' == ')
    text = text.replace("+", ' + ')
    text = text.replace("-", ' - ')
    text = text.replace("*", ' * ')
    text = text.replace("/", ' / ')
    
      
    return text
        
def lexer(text, tokens):
 
    words = text.split()
    result = ""
  
    for word in words:
        if word in tokens:
            result += tokens[word] + " "
        elif word.isalnum() and word[0].isalpha():
            result += "NAME "
        else:
            result += "WORD "
    return result

print(lexer(read_file_and_format("./Proyecto_0/prueba_archivo.txt"),DiccionarioTokens))

def parse(tokens):
    tokens = tokens.split()
    index = 0
    if tokens[index] != "PR":
        return False
    index += 1
    if tokens[index] == "V":
        index += 1
        while tokens[index] != "PYC":
            if tokens[index] != "NAMES":
                return False
            index += 1
            if tokens[index] == "COMA":
                index += 1
    if tokens[index] == "DP":
        index += 1
        if tokens[index] != "NAMES":
            return False
        index += 1
        if tokens[index] != "COPEN":
            return False
        index += 1
        balance = 1
        while balance != 0:
            if tokens[index] == "COPEN":
                balance += 1
            elif tokens[index] == "CCLOSE":
                balance -= 1
            index += 1
    if index != len(tokens):
        return False
    return True

            
    #procedimiento tokens
""" while i < len(tokens):
        
        if tokens[i] in ["CAT", "CGT", "CM", "CT", "CF", "CPUT",
        "CPICK", "CMTT", "CMDIR", "CJTT", "CJDIR"]:
            return f"Error: token '{tokens[i]}'"
        i += 1
        
        if i < len(tokens) and tokens[i] != "DOSPUNTOS":
            return f"Error: 'DOSPUNTOS' after '{tokens[i-1]}'"
        i += 1
    
    return "Success"""

print(parse(lexer(read_file_and_format("./Proyecto_0/prueba_archivo.txt"),DiccionarioTokens)))
