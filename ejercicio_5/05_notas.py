while True:
    n1 = float(input("Ingresa la 1ra nota: "))
    n2 = float(input("Ingresa la 2da nota: "))
    n3 = float(input("Ingresa la 3ra nota: "))
    if n1 < 0 or n1 > 100 or n2 < 0 or n2 > 100 or n3 < 0 or n3 > 100:
        print("Error: nota inválida")
        exit()
    else:
        promedio = (n1 + n2 + n3) / 3
        if promedio >= 90:
            clasificacion = "Excelente"
        elif promedio >= 80:
            clasificacion = "Muy bueno"
        elif promedio >= 70:
            clasificacion = "Bueno"
        elif promedio >= 60:
            clasificacion = "Supletorio"
        else:
            clasificacion = "Reprobado"
        print("Notas ingresadas:", n1, n2, n3)
        print("Promedio:", promedio)
        print("Clasificación final:", clasificacion)
        break 