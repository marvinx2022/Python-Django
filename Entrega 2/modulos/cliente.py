#Se genera la clase Cliente, que permite crear objetos con los valores indicados. 

class Cliente:
    
    def __init__(self,nick_name, nombre:str, apellido:str, edad:int, direccion: str , ocupacion:str,articulos_comprados:list,carro_compras:list):
        
        self.nick_name=nick_name
        self.nombre=nombre
        self.apellido=apellido
        self.edad= edad
        self.direccion=direccion
        self.ocupacion=ocupacion
        self.articulos_comprados=articulos_comprados
        self.carro_compras=carro_compras
        
    def __str__(self):  #Método mágico que muestra la info de cada instancia de la clase Cliente.
        
        return f'El cliente {self.nombre} {self.apellido} tiene {self.edad} años y vive en {self.direccion}'
    
    
    def agregar_compra(self, articulo):
        self.articulo=articulo
        self.lista_compras.append(self.articulo)
        print(f'El cliente ha comprado el artículo {self.articulo}')
        

    def agregar_al_carro(self, articulo):
        self.articulo=articulo
        self.carro_compras.append(self.articulo)
        print(f'Se ha agregado el artículo {self.articulo} al carrito')


lista_clientes=[]