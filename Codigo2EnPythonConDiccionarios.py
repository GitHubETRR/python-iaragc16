agenda = {}

def agregar_contacto(nombre, telefono, mail):
    if nombre in agenda:
        print(f"El contacto '{nombre}' ya existe.")
    else:
        agenda[nombre] = (nombre, telefono, mail)
        print(f"Contacto '{nombre}' agregado.")
        

def mostrar_contactos():
    if not agenda:  # Si el diccionario está vacío
        print("La agenda está vacía.")
    else:
        print("Lista de contactos:")
        for i, info in agenda.items(): 
            nombre, telefono, mail = info
            print(f"Nombre: {nombre}, Teléfono: {telefono}, mail: {mail}")


def buscar_contacto(nombre):
    nombre = nombre.lower()  
    encontrados = []

    for clave, contacto in agenda.items():
        if nombre in clave.lower(): 
            encontrados.append(contacto)
            
    if encontrados:
        for contacto in encontrados: 
            print(f"Nombre: {contacto[0]}, Telefono: {contacto[1]}, Mail: {contacto[2]}")
    else:
        print(f"El contacto '{nombre}' no se encuentra en la agenda.")
        
        
def eliminar_contacto(nombre):
    if nombre in agenda:
        del agenda[nombre]  
        print(f"Contacto '{nombre}' eliminado.")
    else:
        print(f"Contacto '{nombre}' no encontrado.")
        

def menu():
    while True:
        print("\n--- Agenda de Contactos ---")
        print("1. Agregar contacto")
        print("2. Mostrar contactos")
        print("3. Buscar contacto")
        print("4. Eliminar contacto")
        print("5. Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            nombre = input("Nombre: ")
            telefono = input("Teléfono: ")
            mail = input("Mail: ")
            agregar_contacto(nombre, telefono, mail)
        elif opcion == "2":
            mostrar_contactos()
        elif opcion == "3":
            nombre = input("Nombre del contacto a buscar: ")
            buscar_contacto(nombre)
        elif opcion == "4":
            nombre = input("Nombre del contacto a eliminar: ")
            eliminar_contacto(nombre)
        elif opcion == "5":
            print("Saliendo de la agenda.")
            break
        else:
            print("Opción no válida, intenta de nuevo.")

menu()
