# Creacion de mas Metodos
class Helado:

    # Definir Atributos 
    def __init__(self, sabor, tamano, tipo_envase):

        self.sabor = sabor
        self.tamano = tamano
        self.tipo_envase = tipo_envase 
        
    
    # Definir Metodos
    def derretir(self):
        print(f"El helado de {self.sabor} de tamaño {self.tamano} y tipo de envase {self.tipo_envase} se derrite")

    def congelar(self):
        print(f"El helado de {self.sabor} de tamaño {self.tamano} y tipo de envase {self.tipo_envase} se congela")

    def saborear(self):
        print(f"Yo saboreo el helado de {self.sabor} de tamaño {self.tamano} y tipo de envase {self.tipo_envase}")

heladito = Helado("Chocolate", "pequeno", "cono")
helado1 = Helado("Fresa", "grande", "vasito")

heladito.saborear()
helado1.saborear()

