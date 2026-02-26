# ------------------- Validación subtotal
while True:
    try:
        subtotal = float(input("Ingrese el subtotal: "))
        if subtotal <= 0:
            print("Ingrese un valor mayor que cero.")
        else:
            break
    except ValueError:
        print("Ingrese un número válido.")

# ------------------- Validación tipo de cliente
while True:
    tipo = input("Tipo de cliente (vip o regular): ").lower()
    if tipo not in ("vip", "regular"):
        print("Respuesta fuera del rango.")
    else:
        break

# ------------------- Cálculo descuento
if tipo == "vip":
    descuento = subtotal * 0.15
elif tipo == "regular" and subtotal >= 100:
    descuento = subtotal * 0.05
else:
    descuento = 0

total = subtotal - descuento

print("="*45)
print(" "*15 + "TICKET")
print("="*45)

print(f"Subtotal: {subtotal:,.2f}")
print(f"Descuento aplicado: {descuento:,.2f}")
print(f"Total final: {total:,.2f}")

print("="*45)