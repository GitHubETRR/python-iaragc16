
def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b != 0:
        return a / b
    else:
        return "Error, división por 0"

def calculadora():
    print("Selecciona una operación:")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")

    opcion = input("Introduce el número de la operación: ")
    if opcion != '1' and opcion != '2' and opcion != '3' and opcion != '4' :
        print("Opcion no valida")

    num1 = float(input("Introduce el primer número: "))
    num2 = float(input("Introduce el segundo número: "))

    if opcion == '1':
        print("Resultado:", sumar(num1, num2))
    elif opcion == '2':
        print("Resultado:", restar(num1, num2))
    elif opcion == '3':
        print("Resultado:", multiplicar(num1, num2))
    elif opcion == '4':
        print("Resultado:", dividir(num1, num2))

calculadora()