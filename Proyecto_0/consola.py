#CONSOLA
import Lexer as lex
import Parser as p
import sys

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
    "facing" : "FACE",
    "canput" : "CNPUT",
    "canpick" : "CNPCK",
    "canmoveindir" : "CMIDIR",
    "canjumpindir" : "CJIDIR",
    "canmovetothe" : "CMTT",
    "canjumptothe" : "CJTT",
    "not" : "NOT",
    #Especial Conditions
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






def print_menu():
    print("--------------------------------------------------------------------")
    print("Bienvenido a nuestro lexer y parser")
    print("Seleccione alguna de las siguientes opciones:")
    print("Las 4 primeras opciones son bajo el codigo ejemplo. Para otro archivo de texto, use opcion 5. ")
    print("1. Iniciar Programa")
    print("2. Mostrar codigo original")
    print("3. Mostrar Tokens")
    print("4. Mostrar resultado del parser")
    print("5. Programa con diferente archivo")
    print("9. Salir")

while True:
    print_menu()
    inputs = input("Seleccione una opcion: ")

    if int(inputs[0]) == 1:

        print("--------------------------------------------------------------------")

        print("Mostrando Codigo Original")

        print(lex.read_file_and_format("./Proyecto_0/prueba_archivo.txt"))

        print("Mostrando Tokens")

        print(lex.lexer(lex.read_file_and_format("./Proyecto_0/prueba_archivo.txt"),DiccionarioTokens))

        print("El resultador del parser es ", p.parse(lex.lexer(lex.read_file_and_format("./Proyecto_0/prueba_archivo.txt"),DiccionarioTokens)))

    elif int(inputs[0]) == 2:

        print("--------------------------------------------------------------------")

        print("Mostrando Codigo Original")

        print(lex.read_file_and_format("./Proyecto_0/prueba_archivo.txt"))

    elif int(inputs[0]) == 3:

        print("--------------------------------------------------------------------")

        print("Mostrando Tokens")

        print(lex.lexer(lex.read_file_and_format("./Proyecto_0/prueba_archivo.txt"),DiccionarioTokens))

    elif int(inputs[0]) == 4:

        print("--------------------------------------------------------------------")

        print("Mostrando Resultado Parser")

        print("El resultador del parser es ", p.parse(lex.lexer(lex.read_file_and_format("./Proyecto_0/prueba_archivo.txt"),DiccionarioTokens))) 

    elif int(inputs[0]) == 5:

        print("--------------------------------------------------------------------")

        file = input("Coloque el nombre del archivo. (Debe estar en la carpeta del proyecto). ")

        print("Mostrando Codigo Original")

        print(lex.read_file_and_format("./Proyecto_0/"+file))

        print("Mostrando Tokens")

        print(lex.lexer(lex.read_file_and_format("./Proyecto_0/"+file),DiccionarioTokens))

        print("El resultador del parser es ", p.parse(lex.lexer(lex.read_file_and_format("./Proyecto_0/"+file),DiccionarioTokens)))

    else:
        sys.exit(0)
