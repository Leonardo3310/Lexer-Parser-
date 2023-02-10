#CONSOLA
import Lexer as lex
import Parser as p

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
    "/" : "DIV",
    "%" : "MOD"
    #Tokens Operadores Aritmeticos
}

print(lex.read_file_and_format("./Proyecto_0/prueba_archivo.txt"))
print(lex.lexer(lex.read_file_and_format("./Proyecto_0/prueba_archivo.txt"),DiccionarioTokens))
print(p.parse(lex.lexer(lex.read_file_and_format("./Proyecto_0/prueba_archivo.txt"),DiccionarioTokens)))




