"""Administrador de Clientes """
import helpers

clients = []

# Añadimos datos de prueba
nombretest = {'nombre':'Jose', 'apellido': 'Medina', 'run': '12345678-k'}
clients.append(nombretest)

# FUNCIONES:

# Mostrar clientes
def show(client):
    print(f"run: {client['run']} | Nombre: {client['nombre']} | Apellido:  {client['apellido']}")

def show_all():
    for client in clients:
        show(client)

# Buscar un cliente
def find():
    run = input('Introduce el RUN del cliente\n-> ')

    for client in clients:
        if client['run'] == run:
            show(client)
            return client
    
    print(f'No se ha encontrado un cliente con el RUN {run}')

# Agregar cliente
def add():
    client = dict()

    print('Introduce el nombre (de 2 a 30 caracteres)')
    client['nombre'] = helpers.input_text(2, 30)

    print('Introduce el apellido (de 2 a 30 caracteres)')
    client['apellido'] = helpers.input_text(2, 30)

    print('Introduce el RUN (de 3 caracteres, 2 numero y una letra mayuscula)')
    client['run'] = helpers.input_text(3, 3)

    clients.append(client)
    return client

# Modificar cliente
def edit():
    run = input('Introduzca el RUN del Clienten\n-> ')
    for client in clients:
        if client['run'] == run:
            print(f"Introduce un nuevo nombre ({client['nombre']})")
            client['nombre'] = helpers.input_text(2, 30)
            print(f"Introduce un nuevo apellido ({client['apellido']})")
            client['apellido'] = helpers.input_text(2, 30)
            return True
    print('Run no encontrado')
    return False

# Borrar cliente
def delete():
    run = input('Introduzca el RUN del Clienten\n-> ')
    for i, client in enumerate(clients):
        if client['run'] == run:
            client = clients.pop(i) #POP ocupa indice para borrar un elemento
            #del(clients['run'])
            show(client)
            return True
    print('Run no encontrado')
    return False
