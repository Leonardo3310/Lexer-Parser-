"""Parser"""





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
        if tokens[index] != "COPEN":
                return False
        index += 1
        tokensEntreCOPENyCCLOSE = ""
        #posicion del COPEN
        while tokens[index] != "CCLOSE":
            tokensEntreCOPENyCCLOSE += " " + tokens[index]
            index += 1
        
        ##if llamar a verificar dentro de []

    #aqui ya tengo el indice de CCLOSE


    #INSERTAR CODIGO AQUI

    if index != len(tokens):
        return False
    return True

def AuxParserBetweenKeys(tokens):
    tokens = tokens.split
    index = 0

    if tokens[index] != "PALITO":
        return False

    index += 1

    while index < len(tokens) and tokens[index] != "PALITO":
        if tokens[index] == "NOMBRE" and index != len(tokens)-1:
            index += 1
            if index < len(tokens) and tokens[index] == "COMA":
                index += 1
            elif index == len(tokens):
                break
        index += 1
    #aqui tengo palito

    index += 1
        
    if tokens[index] in ["CAT", "CGT", "CM", "CT",
    "CF", "CPUT", "CPICK", "CMTT", "CMDIR", "CJTT", "CJDIR", "IF", "ELSE","ELSEIF",
    "THEN", "WHL"] and \
    index < len(tokens):
        index += 1
        if index < len(tokens) and tokens[index] != "DOSPUNTOS":
            return False
        index += 1

    return True
 
#mi plan es como si existe DP, llamar la funcion aux y guardar la posicion hasta el siguiente CCLOSE, 
#para que se evalue recursivamente, y avanzar con la posicion 

#nota mental
#entre palos puede no haber paramatros 
#
    
    





            
    #procedimiento tokens de instruccion
    #Agregar operadores logicos como instruccion y tambien while codigo
    
""" while i < len(tokens):
        
        if tokens[i] in ["CAT", "CGT", "CM", "CT", "CF", "CPUT",
        "CPICK", "CMTT", "CMDIR", "CJTT", "CJDIR"]:
            return f"Error: token '{tokens[i]}'"
        i += 1
        
        if i < len(tokens) and tokens[i] != "DOSPUNTOS":
            return f"Error: 'DOSPUNTOS' after '{tokens[i-1]}'"
        i += 1
    
    return "Success"""

#print(parse(lexer(read_file_and_format("./Proyecto_0/prueba_archivo.txt"),DiccionarioTokens)))
