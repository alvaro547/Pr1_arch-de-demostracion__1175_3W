archivo=open("alumnos.txt","r")
print (archivo.readline())

archivo.close()

# Nombre del archivo
nombre_archivo = 'demofile.txt'

try:
    # Abrir el archivo en modo lectura
    with open(nombre_archivo, 'r') as archivo:
        # Leer el contenido del archivo
        contenido = archivo.read()
        # Mostrar el contenido en la consola
        print("Contenido del archivo:")
        print(contenido)
except FileNotFoundError:
    print(f"El archivo '{nombre_archivo}' no existe.")
