import os

CARPETA = 'contactos/' # Esta en mayuscula porque es una constante
EXTENSION = '.txt' # Extension de archivos

# Contactos
class Contacto:
    def __init__(self, nombre, telefono, categoria):
        self.nombre = nombre
        self.telefono = telefono
        self.categoria = categoria


def app():
    # Revisa si la carpeta existe o no
    crear_directorio()
    mostrar_menu()

    # Preguntar al usuario que desea realizar
    preguntar = True
    while preguntar:
        opcion = int(input('Selecione una opcion: \r\n'))

        # Ejecutar las opciones
        if opcion == 1:
            agregar_contacto()
            preguntar = False
        elif opcion == 2:
            editar_contacto()
            preguntar = False
        elif opcion == 3:
            mostrar_contactos()
            preguntar = False
        elif opcion == 4:
            buscar_contacto()
            preguntar = False
        elif opcion == 5:
            eliminar_contacto()
            preguntar = False
        else:
            print('Opcion no valida, intente de nuevo')

def eliminar_contacto():
    nombre = input('Seleccione el contacto que desea eliminar' + '\r\n')

    try:
        os.remove(CARPETA + nombre + EXTENSION)
        print('\r\n Eliminado correctamente \r\n')
    except:
        print('\r\n No existe ese contacto \r\n')

    # Reiniciar la app
    app()

def buscar_contacto():
    nombre = input('Seleccione el contacto que desea buscar' + '\r\n')

    try:
        with open(CARPETA + nombre + EXTENSION) as contacto:
            print('\r\n Informacion del contacto: \r\n')
            for linea in contacto:
                print(linea.rstrip())
            print('\r\n')
    except IOError:
        print('El archivo no existe')
        print(IOError)
        print('\r\n')

    # Reiniciar la app
    app()

def mostrar_contactos():
    archivos = os.listdir(CARPETA)

    archivos_txt = [i for i in archivos if i.endswith(EXTENSION)]

    for archivo in archivos_txt:
        with open(CARPETA +  archivo) as contacto:
            for linea in contacto:
                # Imprime el contenido de la carpeta
                print(linea.rstrip())
            print('\r\n')

    # Reiniciar la app
    app()

def editar_contacto():
    print('Escribe el nombre de contacto para editar')
    nombre_anterior = input('Nombre del contacto que desea editar:' + '\r\n')

    # Revisar si el archivo ya existe antes de editarlo
    existe = existe_contacto(nombre_anterior)

    if existe:
        print('Puedes editar')
        with open(CARPETA + nombre_anterior + EXTENSION, 'w') as archivo:

            # Resto de los campos
            nombre_contacto = input('Agrega el nuevo nombre:' + '\r\n')
            telefono_contacto = input('Agrega el nuevo telefono:' + '\r\n')
            categoria_contacto = input('Agrega la nueva categoria:' + '\r\n')

            # Instanciar
            contacto = Contacto(nombre_contacto, telefono_contacto, categoria_contacto)

            # Escribir en el archivo
            archivo.write('Nombre: ' + contacto.nombre + '\r\n')
            archivo.write('Telefono: ' + contacto.telefono + '\r\n')
            archivo.write('Categoria: ' + contacto.categoria + '\r\n')

            # Renombrar el archivo
            os.rename(CARPETA + nombre_anterior + EXTENSION, CARPETA + nombre_contacto + EXTENSION)

            # Mostrar un mensaje de exito
            print('\r\n Contacto editado correctamente \r\n')
    else:
        print('Ese contacto no existe')

    # Reiniciar la app
    app()    

def agregar_contacto():
    print('Escribe los datos para agregar el nuevo contacto')
    nombre_contacto = input('Nombre del contacto:' + '\r\n')

    # Revisar si el archivo ya existe antes de crearlo
    existe = existe_contacto(nombre_contacto)

    if not existe:

        with open(CARPETA + nombre_contacto + EXTENSION, 'w') as archivo:

            telefono_contacto = input('Agrega el telefono:' + '\r\n')
            categoria_contacto = input('Categoria contacto:' + '\r\n')

            # Instanciar la clase
            contacto = Contacto(nombre_contacto, telefono_contacto, categoria_contacto)

            # Escribir en el archivo
            archivo.write('Nombre: ' + contacto.nombre + '\r\n')
            archivo.write('Telefono: ' + contacto.telefono + '\r\n')
            archivo.write('Categoria: ' + contacto.categoria + '\r\n')

            # Mostrar un mensaje de exito
            print('\r\n Contacto creado correctamente \r\n')

    else:
        print('Ese contacto ya existe')

    # Reiniciar la app
    app()

# Mostrar el menu de opciones
def mostrar_menu():
    print('Seleccione del menu lo que desea hacer:')
    print('1) Agregar Nuevo Contacto')
    print('2) Editar Contacto')
    print('3) Ver Contactos')
    print('4) Buscar Contactos')
    print('5) Eliminar Contactos')

def crear_directorio():
    if not os.path.exists(CARPETA):
        # Crear la carpeta
        os.makedirs(CARPETA)
    else:
        print('La carpeta ya existe')

def existe_contacto(nombre):
    return os.path.isfile(CARPETA + nombre + EXTENSION)

app()
