# Definir una clase  que se llame "Helado"
# Atributos: sabor tamano, tipo_envase
# Metodos: derretir, congelar, saborear

class Helado:

    # Definir Atributos 
    def __init__(self, sabor, tamano, tipo_envase):

        self.sabor = sabor
        self.tamano = tamano
        self.tipo_envase = tipo_envase 
        
    
    # Definir Metodos
    def derretir(self):
        print("El helado se derrite")


heladito = Helado("Chocolate", "pequeno", "cono")

heladito.derretir()

