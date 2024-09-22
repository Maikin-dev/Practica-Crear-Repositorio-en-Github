from Features.Operaciones import sumar, restar, multiplicar, dividir
from Features.NuevasOperaciones import Potencia, RaizCuadrada

# Mostrar el menú de opciones
def menu():
    print("Selecciona la operación:")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Potencia")
    print("6. Raiz Cuadrada")


# Función principal de la calculadora
def calculadora():
    while True:
        menu()
        
        # Solicitar al usuario que elija una operación
        opcion = input("Introduce la opción (1/2/3/4/5/6 o 'salir' para terminar): ")

        if opcion.lower() == 'salir':
            print("¡Gracias por usar la calculadora!")
            break

        if opcion in ['1', '2', '3', '4','5','6']:
            
            # Solicitar los números al usuario
            numero1 = float(input("Introduce el primer número: "))
            numero2 = float(input("Introduce el segundo número: "))

            # Realizar la operación seleccionada
            if opcion == '1':
                print(f"El resultado de la suma es: {sumar(numero1, numero2)}")
            elif opcion == '2':
                print(f"El resultado de la resta es: {restar(numero1, numero2)}")
            elif opcion == '3':
                print(f"El resultado de la multiplicación es: {multiplicar(numero1, numero2)}")
            elif opcion == '4':
                print(f"El resultado de la división es: {dividir(numero1, numero2)}")
            elif opcion == '5':
                print(f"El resultado de la división es: {Potencia(numero1)}")
            elif opcion == '6':
                print(f"El resultado de la división es: {RaizCuadrada(numero1)}")
        else:
            print("Opción no válida. Inténtalo de nuevo.")

# Ejecutar la calculadora
calculadora()
