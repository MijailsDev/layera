# Funciones

def operacion(a, b, c, d):
    
    # Definir operacion
    x = a + b - c + d

    return x


def suma(x, y):
    
    # Sumar parametros x e y 
    z = x + y

    return z


def volumen_esfera(radio):
    volumen =  4*3.14159265*(radio^3)
    return volumen

print(volumen_esfera(2))