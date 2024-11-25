import pymongo

# Conexión a MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["gestion_lugares_no_relacional"]

# Crear colecciones
clinicas = db["clinicas"]
parques = db["parques"]

def ingresar_datos_clinica():
    nombre = input("Ingrese el nombre de la clínica: ")
    direccion = input("Ingrese la dirección de la clínica: ")
    capacidad = int(input("Ingrese la capacidad de la clínica: "))
    especialidades = input("Ingrese las especialidades de la clínica separadas por comas: ").split(",")
    
    clinica = {
        "nombre": nombre,
        "direccion": direccion,
        "capacidad": capacidad,
        "especialidades": especialidades
    }
    
    clinicas.insert_one(clinica)
    print("Datos de la clínica guardados exitosamente.\n")

def ingresar_datos_parque():
    nombre = input("Ingrese el nombre del parque: ")
    ubicacion = input("Ingrese la ubicación del parque: ")
    precio_entrada = float(input("Ingrese el precio de entrada al parque: "))
    actividades = input("Ingrese las actividades disponibles en el parque separadas por comas: ").split(",")
    
    parque = {
        "nombre": nombre,
        "ubicacion": ubicacion,
        "precio_entrada": precio_entrada,
        "actividades": actividades
    }
    
    parques.insert_one(parque)
    print("Datos del parque guardados exitosamente.\n")

def listar_clinicas():
    print("Listado de clínicas:")
    for clinica in clinicas.find():
        print(clinica["nombre"])

def listar_parques():
    print("Listado de parques:")
    for parque in parques.find():
        print(parque["nombre"])

# Menú para interactuar con el usuario
while True:
    print("\n--- Menú ---")
    print("1. Ingresar datos de una clínica")
    print("2. Ingresar datos de un parque")
    print("3. Listar todas las clínicas")
    print("4. Listar todos los parques")
    print("5. Salir")
    
    opcion = input("Seleccione una opción (1-5): ")
    
    if opcion == "1":
        ingresar_datos_clinica()
    elif opcion == "2":
        ingresar_datos_parque()
    elif opcion == "3":
        listar_clinicas()
    elif opcion == "4":
        listar_parques()
    elif opcion == "5":
        print("Saliendo del programa.")
        break
    else:
        print("Opción no válida. Intente de nuevo.")