import json
from usuario import Usuario

try:
    with open('usuarios.txt', 'r') as archivo:
        usuarios = []  # Lista para almacenar las instancias de Usuario
        for linea in archivo:
            try:
                # Convierte la línea de JSON a un diccionario y crea una instancia de Usuario
                datos_usuario = json.loads(linea)
                usuario = Usuario(**datos_usuario)
                usuarios.append(usuario)
            except Exception as e:
                # Si ocurre un error al crear una instancia, registra el error en error.log
                with open('error.log', 'a') as log:
                    log.write(f'Error al procesar los datos de un usuario: {e}\n')
except Exception as e:
    # Si ocurre un error al intentar abrir el archivo, registra el error en error.log
    with open('error.log', 'a') as log:
        log.write(f'Error al abrir el archivo usuarios.txt: {e}\n')
