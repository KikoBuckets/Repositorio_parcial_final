lecturas_totales = int(input("Ingrese el numero total de lecturas: "))
lecturas_fuera_de_rango = sum(1 for _ in range(lecturas_totales) if not 10 <= float(input("Ingrese la lectura: ")) <= 40)

porcentaje_error = (lecturas_fuera_de_rango / lecturas_totales) * 100

print(f"Porcentaje de error: {porcentaje_error}%")
