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
    


    if index != len(tokens):
        return False
    return True

"""if tokens[index] == "DP":
        index += 1
        if tokens[index] != "NAMES":
            return False
        index += 1
        if tokens[index] != "COPEN":
            return False
        parametros = verificationParamethersProceduredDefinition(tokens[index-1:])
        if parametros[0]:
            if auxNameComa(parametros[1]):
                index += 1"""
            
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
