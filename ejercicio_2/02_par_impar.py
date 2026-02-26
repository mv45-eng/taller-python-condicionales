while True:
    try:
        num = int(input("Escribe un número: "))
        break
    except ValueError:
        print("Ingrese un número entero válido.")

if num % 2 == 0:
    print("Tu número es par.")
else:
    print("Tu número es impar.")