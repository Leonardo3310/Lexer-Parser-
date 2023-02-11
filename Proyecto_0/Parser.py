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
            print("pyc")
            if tokens[index] != "NAME":
                return False
            index += 1
            if tokens[index] == "COMA" :
                index += 1
            elif tokens[index] == "NAME":
                index += 1
            
    index += 1
                
    if tokens[index] == "DP":
        print("C")
        index += 1
        if tokens[index] != "NAME":
            return False
        index += 1
        print("b")

        if tokens[index] != "COPEN":
                return False
        index += 1
        tokensEntreCOPENyCCLOSE = ""
        #posicion del COPEN
        while tokens[index] != "CCLOSE":
            tokensEntreCOPENyCCLOSE += " " + tokens[index]
            index += 1

        if AuxParserBetweenKeys(tokensEntreCOPENyCCLOSE) != True:
            return False
    

        

    #aqui ya tengo el indice de CCLOSE
    #insertar condigo aqui
    if index != len(tokens)-1:
        return False


    return True

def AuxParserBetweenKeys(tokens):
    print("a")
    tokens = tokens.split()
    index = 0

    if tokens[index] != "PALITO":
        return False

    index += 1

    while index < len(tokens) and tokens[index] != "PALITO":
        if tokens[index] == "NAME" and index != len(tokens)-1:
            index += 1
            print("NOMBRE DP")
            if index < len(tokens) and tokens[index] != "COMA":
                return False
            index += 1
            
        index += 1
        print("x")
    #aqui tengo palito
    print("f")
    index += 1
        
    if tokens[index] in ["CAT", "CGT", "CM", "CT",
    "CF", "CPUT", "CPICK", "CMTT", "CMDIR", "CJTT", "CJDIR", "IF", "ELSE","ELSEIF",
    "THEN", "WHL"] and \
    index < len(tokens):
        index += 1
        print("q")
        if index < len(tokens) and tokens[index] != "DOSPUNTOS":
            return False
        index += 1
        print("a")

    return True
 

#print(parse(lexer(read_file_and_format("./Proyecto_0/prueba_archivo.txt"),DiccionarioTokens)))
