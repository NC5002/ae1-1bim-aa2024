import mysql.connector


def conectar():
    # Configuración de conexión
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="123456789",  # Cambia según tu configuración
        database="gestion_lugares"
    )


def agregar_datos_clinica():
    conexion = conectar()
    cursor = conexion.cursor()

    # Solicitar datos al usuario
    nombre = input("Ingresa el nombre de la clínica: ")
    direccion = input("Ingresa la dirección de la clínica: ")
    especialidades = input(
        "Ingresa las especialidades (separadas por comas): ")
    capacidad = int(input("Ingresa la capacidad de la clínica: "))

    # Insertar los datos en la tabla clinicas
    query = "INSERT INTO clinicas (nombre, direccion, especialidades, capacidad) VALUES (%s, %s, %s, %s)"
    cursor.execute(query, (nombre, direccion, especialidades, capacidad))

    conexion.commit()
    print("Clínica agregada exitosamente.")

    cursor.close()
    conexion.close()


def agregar_datos_parque():
    conexion = conectar()
    cursor = conexion.cursor()

    # Solicitar datos al usuario
    nombre = input("Ingresa el nombre del parque: ")
    ubicacion = input("Ingresa la ubicación del parque: ")
    precio_entrada = float(input("Ingresa el precio de entrada: "))
    actividades = input(
        "Ingresa las actividades disponibles (separadas por comas): ")

    # Insertar los datos en la tabla parques
    query = "INSERT INTO parques (nombre, ubicacion, precio_entrada, actividades) VALUES (%s, %s, %s, %s)"
    cursor.execute(query, (nombre, ubicacion, precio_entrada, actividades))

    conexion.commit()
    print("Parque agregado exitosamente.")

    cursor.close()
    conexion.close()

# Función para buscar clínicas con capacidad aproximada


def buscar_clinicas_por_capacidad():
    conexion = conectar()
    cursor = conexion.cursor()

    # Solicitar la capacidad aproximada al usuario
    capacidad = int(
        input("Ingresa la capacidad aproximada de la clínica que buscas: "))

    # Consultar las clínicas con capacidad cercana (dentro de un rango de ±10)
    rango = 10
    query = """
        SELECT nombre, direccion, capacidad
        FROM clinicas
        WHERE capacidad BETWEEN %s AND %s;
    """
    cursor.execute(query, (capacidad - rango, capacidad + rango))
    resultados = cursor.fetchall()

    if resultados:
        print("\nClínicas encontradas:")
        for clinica in resultados:
            print(
                f"- {clinica[0]} (Dirección: {clinica[1]}, Capacidad: {clinica[2]})")
    else:
        print("No se encontró ninguna clínica con una capacidad aproximada a la ingresada.")

    cursor.close()
    conexion.close()

# Función para buscar parques con precio de entrada aproximado


def buscar_parques_por_precio():
    conexion = conectar()
    cursor = conexion.cursor()

    # Solicitar el precio aproximado al usuario
    precio = float(
        input("Ingresa el precio aproximado de entrada del parque que buscas: "))

    # Consultar los parques con precio cercano (dentro de un rango de ±1)
    rango = 1
    query = """
        SELECT nombre, ubicacion, precio_entrada
        FROM parques
        WHERE precio_entrada BETWEEN %s AND %s;
    """
    cursor.execute(query, (precio - rango, precio + rango))
    resultados = cursor.fetchall()

    if resultados:
        print("\nParques encontrados:")
        for parque in resultados:
            print(f"- {parque[0]} (Ubicación: {parque[1]
                                               }, Precio de entrada: {parque[2]})")
    else:
        print("No se encontró ningún parque con un precio aproximado al ingresado.")

    cursor.close()
    conexion.close()


def listar_tabla(tabla):
    conexion = conectar()
    cursor = conexion.cursor()

    query = f"SELECT nombre FROM {tabla};"
    cursor.execute(query)
    resultados = cursor.fetchall()

    print(f"\nLista de {tabla}:")
    for row in resultados:
        print(f"- {row[0]}")

    cursor.close()
    conexion.close()


def menu():
    while True:
        print("\nOpciones:")
        print("1. Agregar una clínica")
        print("2. Agregar un parque")
        print("3. Listar todas las clínicas")
        print("4. Listar todos los parques")
        print("5. Buscar clínicas por capacidad aproximada")
        print("6. Buscar parques por precio aproximado")
        print("7. Salir")

        opcion = input("Selecciona una opción: ")
        if opcion == "1":
            agregar_datos_clinica()
        elif opcion == "2":
            agregar_datos_parque()
        elif opcion == "3":
            listar_tabla("clinicas")
        elif opcion == "4":
            listar_tabla("parques")
        elif opcion == "5":
            buscar_clinicas_por_capacidad()
        elif opcion == "6":
            buscar_parques_por_precio()
        elif opcion == "7":
            print(
                "Saliendo del programa. Gracias por usar nustros sistena. Vuelve pronto")
            break
        else:
            print("Opción no válida, intenta de nuevo.")


if __name__ == "__main__":
    print("Inicializando programa...")
    menu()  # Lanza el menú interactivo


# git add .
# git commit -m "Added non-relational database implementation"
# git push origin ramados
