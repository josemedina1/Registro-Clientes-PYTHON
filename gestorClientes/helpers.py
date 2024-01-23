""" Funciones de ayuda """

import os
import platform

# Limpa la consola cada vez que se ejecuta el programa o se accede a una seccion del menu
def clear():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        #UNIX (Linux o Mac)
        os.system('clear')

# Limitar cantidad de caracteres admitidos por inputs
def input_text(min_length, max_length):
    while True:
        text = input('> ')
        if len(text) >= min_length and len(text) <= max_length:
            return text
