# Validación nombre
while True:
    name = input("Cuál es tu nombre: ").strip()
    if name == "":
        print("El nombre no puede estar vacío.")
    else:
        break

# Validación edad
while True:
    try:
        age = int(input("Cuántos años tienes: "))
        if age <= 0:
            print("Ingrese una edad válida.")
        else:
            break
    except ValueError:
        print("Ingrese un número entero válido.")

# Validación ciudad
while True:
    city = input("En qué ciudad vives: ").strip()
    if city == "":
        print("La ciudad no puede estar vacía.")
    else:
        break

print(f"Hola {name}, tienes {age} años y vives en {city}.")