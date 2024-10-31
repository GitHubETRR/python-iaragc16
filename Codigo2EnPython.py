agenda = []

def agregar_contacto(nombre, telefono, mail):
    contacto = (nombre, telefono, mail)
    agenda.append(contacto)
    print(f"Contacto {nombre} agregado.")

def mostrar_contactos():
    if len(agenda) == 0:
        print("La agenda está vacía.")
    else:
        print("Lista de contactos:")
        for i, contacto in enumerate(agenda, 1):   #El numero del indice de cada contacto se guarda en i, la info del contacto se guarda en contacto
            nombre, telefono, mail = contacto
            print(f"{i}. Nombre: {nombre}, Teléfono: {telefono}, mail: {mail}")

def buscar_contacto(nombre):
    for contacto in agenda:
        if contacto[0].lower() == nombre.lower(): #.lower es para pasar el string a minuscula
            print(f"Contacto encontrado: Nombre: {contacto[0]}, Teléfono: {contacto[1]}, mail: {contacto[2]}")
            return
    print("Contacto no encontrado.")

def eliminar_contacto(nombre):
    for contacto in agenda:
        if contacto[0].lower() == nombre.lower():
            agenda.remove(contacto)
            print(f"Contacto {nombre} eliminado.")
            return
    print("Contacto no encontrado.")

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
            mail = input("mail: ")
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
