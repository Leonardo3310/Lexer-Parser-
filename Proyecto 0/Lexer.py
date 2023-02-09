"No vamos a usar librerias, gracias:)"

def leer_archivo(nombre_archivo):
    with open(nombre_archivo, 'r') as archivo:
        contenido = archivo.read()
        palabras = contenido.split()
        return palabras

        

