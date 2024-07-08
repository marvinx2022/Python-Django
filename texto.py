cant_hobbies=int(input('Ingresa la cantidad de hobbies:'))


for i in range(cant_hobbies):
    
    i=input('Ingresa el nombre del hobbie: ')
    
    f= open('./archivo.txt', 'a', encoding='utf-8')
    
    f.write(f'{i} \n')
    
    f.close()
    
    