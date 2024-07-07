from cliente import Cliente

from cliente import lista_clientes

 
def crear_cliente(): # Esta función requiere que se tenga una lista inicializada

    global lista_clientes

    nick_name=input('Ingresa un nombre abreviado de cliente: ')

    if nick_name in lista_clientes:

        print('Error: El usuario ya existe')
        
    else:
        
        nombre=input("Ingresa el nombre:")
        apellido=input('Ingresa el apellido:')
        edad=int(input('Ingresa la edad:'))
        direccion=input('Ingresa la dirección:')
        ocupacion=input('Ingresa la ocupación:')
        articulos_comprados=input('Ingresa los articulos comprados (lista):')
        carrito_compras=input('Ingresa los articulos del carrito de compras (lista):')
            

        nuevo_cliente=Cliente(nick_name, nombre, apellido, edad, direccion, ocupacion, articulos_comprados,carrito_compras)
        
        lista_clientes.append(nuevo_cliente.nick_name)

        print(f"Se ha creado el cliente {nuevo_cliente.nick_name}, y se ha agregado a la lista de clientes actual")
        
        

