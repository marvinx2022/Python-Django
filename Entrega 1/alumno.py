class constructor_alumno:
    def __init__(self,nombre,nota):
        self.nombre=nombre
        self.nota=int(nota)
    
    def imprimir(self):
        print(f'La nota de {self.nombre} es {self.nota}')
        
