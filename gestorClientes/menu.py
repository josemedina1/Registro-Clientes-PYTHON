import helpers
# Funciones del menu
import manager

def loop():
    while True:
        
        helpers.clear()

        print('===================================')
        print('BIENVENIDOS AL GESTOR DE CLIENTES')
        print('===================================')
        print('[1] Listar clientes   ')
        print('[2] Buscar cliente por RUN')
        print('[3] Añadir clientes   ')
        print('[4] Modificar clientes')
        print('[5] Borrar clientes   ')
        print('[6] Salir             ')
        print('===================================')

        option = input('> ')

        if option == '1':
            print('Listando los clientes...\n')
            manager.show_all()
        if option == '2':
            print('Mostrando un cliente...\n')
            manager.find()
        if option == '3':
            print('Añadiendo un cliente...\n')
            manager.add()
        if option == '4':
            print('Modificar un cliente...\n')
            manager.edit()
        if option == '5':
            print('Borrar un cliente...\n')
            manager.delete()
        if option == '6':
            print('Saliendo...\n')
            break

        input('\nPresione ENTER para continuar...')
    return True