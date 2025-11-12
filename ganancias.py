# Sistema de registro de ganancias de Uber y Didi
from datetime import date

archivo = "registro.csv"

while True:
    print("\n=== Registro de ganancias ===")
    print("1 - Registrar día")
    print("2 - Ver historial")
    print("3 - Salir")
    opcion = input("Ingrese una opción (1-3): ")

    if opcion == "1":
        fecha = input("Ingrese la fecha (YYYY-MM-DD) o deje vacío para hoy: ")
        if not fecha:
            fecha = str(date.today())

        uber = float(input("Ingrese la ganancia de Uber: "))
        didi = float(input("Ingrese la ganancia de Didi: "))
        total = uber + didi

        gastos = input("Ingrese los gastos del día (opcional): ")
        if gastos == "":
            gastos = 0
        else:
            gastos = float(gastos)

        ganancia_neta = total - gastos

        print(f"\nGanancia bruta del día {fecha}: ${total:.2f}")
        print(f"Gastos: ${gastos:.2f}")
        print(f"Ganancia neta: ${ganancia_neta:.2f}")

        with open(archivo, "a") as f:
            f.write(f"{fecha},{uber},{didi},{total},{gastos},{ganancia_neta}\n")
            print("Registro guardado ✅")

    elif opcion == "2":
        try:
            with open(archivo, "r") as f:
                lineas = f.readlines()

            if not lineas:
                print("No hay registros todavía.")
            else:
                total_general = 0
                dias = 0
                max_ganancia = 0
                dia_max = ""

                print("\n=== Historial de ganancias ===")
                for linea in lineas:
                    datos = linea.strip().split(",")
                    if len(datos) < 6:
                        continue  # por si hay líneas viejas sin gastos
                    fecha, uber, didi, total, gastos, ganancia_neta = datos
                    total = float(total)
                    print(f"{fecha} | Uber: ${uber} | Didi: ${didi} | Total: ${total:.2f} | Gastos: ${gastos} | Neta: ${ganancia_neta}")

                    total_general += total
                    dias += 1

                    if total > max_ganancia:
                        max_ganancia = total
                        dia_max = fecha

                promedio = total_general / dias
                print("\n📈 Resumen:")
                print(f"Total acumulado: ${total_general:.2f}")
                print(f"Promedio diario: ${promedio:.2f}")
                print(f"Mayor ganancia: ${max_ganancia:.2f} el día {dia_max}\n")

        except FileNotFoundError:
            print("Aún no existe el archivo de registros. Registra un día primero.\n")

    elif opcion == "3":
        print("Hasta luego 👋")
        break

    else:
        print("Opción no válida, intentá nuevamente.")
