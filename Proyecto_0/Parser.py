def parse(tokens):

    tokens = tokens.split()
    index = 0

    if tokens[index] != "PR":
        return False
    index += 1

    if tokens[index] == "V":
        index += 1

        while tokens[index] != "PYC":

            if tokens[index] != "NAME":
                return False
            index += 1

            if tokens[index] == "COMA" :
                index += 1

            elif tokens[index] == "NAME":
                index += 1
                
    if tokens[index] == "DP":
        index += 1

        if tokens[index] != "NAME":
            return False
        index += 1

        if tokens[index] != "COPEN":
            return False
        index += 1
        tokensEntreCOPENyCCLOSE = ""
        
        while tokens[index] != "CCLOSE":
            tokensEntreCOPENyCCLOSE += " " + tokens[index]
            index += 1

        if AuxParserBetweenKeys(tokensEntreCOPENyCCLOSE) != True:
            return False
        index+=1

        if AuxAfter(tokens[index:]) != False:
            return False
        else:
            return True

    return True


def AuxParserBetweenKeys(tokens):
 
    tokens = tokens.split()
    index = 0

    if tokens[index] != "PALITO":
        return False

    index += 1

    while index < len(tokens) and tokens[index] != "PALITO":

        if tokens[index] == "NAME" and index != len(tokens)-1:
            index += 1
            
            if index < len(tokens) and tokens[index] != "COMA":
                return False
            index += 1
            
        index += 1
    
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

 
def AuxAfter(tokens):
    
    i = 0
    while i < len(tokens):
        if tokens[i] in ["CAT", "CGT", "CM", "CT",
    "CF", "CPUT", "CPICK", "CMTT", "CMDIR", "CJTT", "CJDIR", "IF", "ELSE","ELSEIF",    
   "THEN", "WHL"]:
            
            i += 1
            if i >= len(tokens) or tokens[i] != "DOSPUNTOS":
                return False
            
        elif tokens[i] == "CCLOSE":
            return i == len(tokens) - 1
        
        elif tokens[i] == "NAME":
            i += 1

            if i >= len(tokens) or tokens[i] != "COPEN":
                return False
            
        elif tokens[i] in ["CNPUT", "CNPCK", "CMIDIR", "CJIDIR", "CMTT"]:
            i += 1

            if i >= len(tokens) or tokens[i] != "DOSPUNTOS":
                return False
            
        else:
            return False
        i += 1

    return False

