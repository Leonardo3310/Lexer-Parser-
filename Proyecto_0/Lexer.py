#Documentacion
"""Comentarios por desarrollar"""

"""dicionario formato:
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
        elif word in "0123456789":
            result += "INT(" + word + ") "
        else:
            result += "WORD "
    return result


