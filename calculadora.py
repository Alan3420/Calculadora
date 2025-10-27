from suma import suma
from resta import resta
from multiplicacion import multiplicacion
from division import division

def main():
    print("=== Calculadora Simple ===")
    print("Operaciones disponibles:")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    
    opcion = input("Elige una opción (1-4): ")
    a = float(input("Ingresa el primer número: "))
    b = float(input("Ingresa el segundo número: "))

    if opcion == "1":
        print(f"Resultado: {suma(a, b)}")
    elif opcion == "2":
        print(f"Resultado: {resta(a, b)}")
    elif opcion == "3":
        print(f"Resultado: {multiplicacion(a, b)}")
    elif opcion == "4":
        print(f"Resultado: {division(a, b)}")
    else:
        print("Opción no válida")

if __name__ == "__main__":
    main()

