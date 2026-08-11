# TP integrador – Repetitivas- Condicionales y Secuenciales. 
# Alejo Avendaño

# Ejercicio 1 - Caja de Kiosco

nombre = input("Ingrese el nombre del cliente: ").strip()

while not nombre.isalpha():
    print("El nombre debe contener solo letras. Intente nuevamente.")
    nombre = input("Ingrese el nombre del cliente: ").strip()

cant_productos_texto = input("Ingrese la cantidad de productos: ").strip()

while (
    not cant_productos_texto.isdigit()
    or int(cant_productos_texto) <= 0
):
    print(
        "La cantidad debe ser un número entero mayor a 0. "
        "Intente nuevamente."
    )
    cant_productos_texto = input(
        "Ingrese la cantidad de productos: "
    ).strip()

cant_productos = int(cant_productos_texto)

total_sin_descuento = 0
total_con_descuento = 0.0

print(f"\nCliente: {nombre}")
print(f"Cantidad de productos: {cant_productos}\n")


for i in range(cant_productos):

    precio_texto = input(
        f"Ingrese el precio del producto {i + 1}: "
    ).strip()

    while not precio_texto.isdigit() or int(precio_texto) <= 0:
        print(
            "El precio debe ser un número entero mayor a 0. "
            "Intente nuevamente."
        )
        precio_texto = input(
            f"Ingrese el precio del producto {i + 1}: "
        ).strip()

    precio = int(precio_texto)

    tiene_descuento = input(
        "¿El producto tiene descuento? (s/n): "
    ).strip().lower()

    while tiene_descuento not in ("s", "n"):
        print("Respuesta inválida. Ingrese 's' o 'n'.")
        tiene_descuento = input(
            "¿El producto tiene descuento? (s/n): "
        ).strip().lower()

    total_sin_descuento += precio

    if tiene_descuento == "s":
        precio_final = precio * 0.90
    else:
        precio_final = precio

    total_con_descuento += precio_final


    print(
        f"Producto {i + 1} - Precio: ${precio} "
        f"- Descuento: {tiene_descuento.upper()} "
        f"- Precio final: ${precio_final:.2f}"
    )

ahorro_total = total_sin_descuento - total_con_descuento
promedio_por_producto = total_con_descuento / cant_productos

print("\nResumen de la compra")
print(f"Total sin descuentos: ${total_sin_descuento:.2f}")
print(f"Total con descuentos: ${total_con_descuento:.2f}")
print(f"Ahorro total: ${ahorro_total:.2f}")
print(f"Promedio por producto: ${promedio_por_producto:.2f}")

# Ejercicio 2  — “Acceso al Campus y Menú Seguro”

usuario_correcto = "alumno"
clave_correcta = "python123"

intentos = 0
acceso_concedido = False

while intentos < 3 and not acceso_concedido:
    print(f"\nIntento {intentos + 1}/3")

    usuario = input("Usuario: ")
    clave = input("Clave: ")

    if usuario == usuario_correcto and clave == clave_correcta:
        acceso_concedido = True
        print("Acceso concedido.")
    else:
        intentos += 1
        print("Error: credenciales inválidas.")

if not acceso_concedido:
    print("Cuenta bloqueada.")

else:
    opcion = ""

    while opcion != "4":
        print("\n1) Ver estado de inscripción")
        print("2) Cambiar clave")
        print("3) Mostrar mensaje motivacional")
        print("4) Salir")

        opcion = input("Opción: ").strip()

        if not opcion.isdigit():
            print("Error: ingrese un número válido.")

        elif int(opcion) < 1 or int(opcion) > 4:
            print("Error: opción fuera de rango.")

        else:
            opcion_numero = int(opcion)

            if opcion_numero == 1:
                print("Inscripto")

            elif opcion_numero == 2:
                nueva_clave = input("Nueva clave: ")

                while len(nueva_clave) < 6:
                    print("Error: mínimo 6 caracteres.")
                    nueva_clave = input("Nueva clave: ")

                confirmacion = input("Confirmar nueva clave: ")

                if nueva_clave == confirmacion:
                    clave_correcta = nueva_clave
                    print("Clave modificada correctamente.")
                else:
                    print("Error: las claves no coinciden.")

            elif opcion_numero == 3:
                print("Cada error es una oportunidad para aprender.")

            elif opcion_numero == 4:
                print("Sesión finalizada.")

# Ejercicio 3 (Alta) — “Agenda de Turnos con Nombres (sin listas)”

operador = input("Ingrese el nombre del operador: ").strip()

while not operador.isalpha():
    print("Error: el nombre debe contener solo letras.")
    operador = input("Ingrese el nombre del operador: ").strip()

lunes1 = ""
lunes2 = ""
lunes3 = ""
lunes4 = ""

martes1 = ""
martes2 = ""
martes3 = ""

cerrar_sistema = False

while not cerrar_sistema:
    print("\n--- AGENDA DE TURNOS ---")
    print("1. Reservar turno")
    print("2. Cancelar turno")
    print("3. Ver agenda del día")
    print("4. Ver resumen general")
    print("5. Cerrar sistema")

    opcion = input("Opción: ").strip()

    if not opcion.isdigit():
        print("Error: ingrese un número válido.")

    elif int(opcion) < 1 or int(opcion) > 5:
        print("Error: opción fuera de rango.")

    else:
        opcion = int(opcion)

        if opcion == 1:
            dia = input("Día (1=Lunes, 2=Martes): ").strip()

            while not dia.isdigit() or int(dia) < 1 or int(dia) > 2:
                print("Error: ingrese 1 para Lunes o 2 para Martes.")
                dia = input("Día (1=Lunes, 2=Martes): ").strip()

            dia = int(dia)

            paciente = input("Nombre del paciente: ").strip()

            while not paciente.isalpha():
                print("Error: el nombre debe contener solo letras.")
                paciente = input("Nombre del paciente: ").strip()

            if dia == 1:
                repetido = (
                    paciente.lower() == lunes1.lower()
                    or paciente.lower() == lunes2.lower()
                    or paciente.lower() == lunes3.lower()
                    or paciente.lower() == lunes4.lower()
                )

                if repetido:
                    print("Error: el paciente ya tiene un turno el lunes.")

                elif lunes1 == "":
                    lunes1 = paciente
                    print("Turno reservado: Lunes, turno 1.")

                elif lunes2 == "":
                    lunes2 = paciente
                    print("Turno reservado: Lunes, turno 2.")

                elif lunes3 == "":
                    lunes3 = paciente
                    print("Turno reservado: Lunes, turno 3.")

                elif lunes4 == "":
                    lunes4 = paciente
                    print("Turno reservado: Lunes, turno 4.")

                else:
                    print("No hay turnos disponibles para el lunes.")

            else:
                repetido = (
                    paciente.lower() == martes1.lower()
                    or paciente.lower() == martes2.lower()
                    or paciente.lower() == martes3.lower()
                )

                if repetido:
                    print("Error: el paciente ya tiene un turno el martes.")

                elif martes1 == "":
                    martes1 = paciente
                    print("Turno reservado: Martes, turno 1.")

                elif martes2 == "":
                    martes2 = paciente
                    print("Turno reservado: Martes, turno 2.")

                elif martes3 == "":
                    martes3 = paciente
                    print("Turno reservado: Martes, turno 3.")

                else:
                    print("No hay turnos disponibles para el martes.")

        elif opcion == 2:
            dia = input("Día (1=Lunes, 2=Martes): ").strip()

            while not dia.isdigit() or int(dia) < 1 or int(dia) > 2:
                print("Error: ingrese 1 para Lunes o 2 para Martes.")
                dia = input("Día (1=Lunes, 2=Martes): ").strip()

            dia = int(dia)

            paciente = input("Nombre del paciente a cancelar: ").strip()

            while not paciente.isalpha():
                print("Error: el nombre debe contener solo letras.")
                paciente = input("Nombre del paciente a cancelar: ").strip()

            encontrado = False

            if dia == 1:
                if paciente.lower() == lunes1.lower():
                    lunes1 = ""
                    encontrado = True

                elif paciente.lower() == lunes2.lower():
                    lunes2 = ""
                    encontrado = True

                elif paciente.lower() == lunes3.lower():
                    lunes3 = ""
                    encontrado = True

                elif paciente.lower() == lunes4.lower():
                    lunes4 = ""
                    encontrado = True

            else:
                if paciente.lower() == martes1.lower():
                    martes1 = ""
                    encontrado = True

                elif paciente.lower() == martes2.lower():
                    martes2 = ""
                    encontrado = True

                elif paciente.lower() == martes3.lower():
                    martes3 = ""
                    encontrado = True

            if encontrado:
                print("Turno cancelado correctamente.")
            else:
                print("No se encontró un turno con ese nombre.")

        elif opcion == 3:
            dia = input("Día (1=Lunes, 2=Martes): ").strip()

            while not dia.isdigit() or int(dia) < 1 or int(dia) > 2:
                print("Error: ingrese 1 para Lunes o 2 para Martes.")
                dia = input("Día (1=Lunes, 2=Martes): ").strip()

            dia = int(dia)

            if dia == 1:
                print("\n--- AGENDA DEL LUNES ---")
                print(f"Turno 1: {lunes1 if lunes1 != '' else '(libre)'}")
                print(f"Turno 2: {lunes2 if lunes2 != '' else '(libre)'}")
                print(f"Turno 3: {lunes3 if lunes3 != '' else '(libre)'}")
                print(f"Turno 4: {lunes4 if lunes4 != '' else '(libre)'}")

            else:
                print("\n--- AGENDA DEL MARTES ---")
                print(f"Turno 1: {martes1 if martes1 != '' else '(libre)'}")
                print(f"Turno 2: {martes2 if martes2 != '' else '(libre)'}")
                print(f"Turno 3: {martes3 if martes3 != '' else '(libre)'}")

        elif opcion == 4:
            ocupados_lunes = 0
            ocupados_martes = 0

            if lunes1 != "":
                ocupados_lunes += 1

            if lunes2 != "":
                ocupados_lunes += 1

            if lunes3 != "":
                ocupados_lunes += 1

            if lunes4 != "":
                ocupados_lunes += 1

            if martes1 != "":
                ocupados_martes += 1

            if martes2 != "":
                ocupados_martes += 1

            if martes3 != "":
                ocupados_martes += 1

            disponibles_lunes = 4 - ocupados_lunes
            disponibles_martes = 3 - ocupados_martes

            print("\n--- RESUMEN GENERAL ---")
            print(f"Lunes - Ocupados: {ocupados_lunes}")
            print(f"Lunes - Disponibles: {disponibles_lunes}")
            print(f"Martes - Ocupados: {ocupados_martes}")
            print(f"Martes - Disponibles: {disponibles_martes}")

            if ocupados_lunes > ocupados_martes:
                print("Día con más turnos: Lunes.")

            elif ocupados_martes > ocupados_lunes:
                print("Día con más turnos: Martes.")

            else:
                print("Ambos días tienen la misma cantidad de turnos.")

        elif opcion == 5:
            cerrar_sistema = True
            print(f"Sistema cerrado por {operador}.")

# Ejercicio 4  — “Escape Room: La Bóveda” 

energia = 100
tiempo = 12
cerraduras_abiertas = 0
alarma = False
codigo_parcial = ""

forzadas_seguidas = 0
bloqueado = False

agente = input("Ingrese el nombre del agente: ").strip()

while not agente.isalpha():
    print("Error: el nombre debe contener solo letras.")
    agente = input("Ingrese el nombre del agente: ").strip()


print(f"\nBienvenido, agente {agente}.")
print("Tu misión es abrir las tres cerraduras de la bóveda.")

while (
    energia > 0
    and tiempo > 0
    and cerraduras_abiertas < 3
    and not bloqueado
):
    print("\n--- ESTADO ACTUAL ---")
    print(f"Energía: {energia}")
    print(f"Tiempo: {tiempo}")
    print(f"Cerraduras abiertas: {cerraduras_abiertas}/3")
    print(f"Alarma: {'ACTIVADA' if alarma else 'Desactivada'}")
    print(f"Código parcial: {codigo_parcial}")

    print("\n--- ACCIONES ---")
    print("1. Forzar cerradura")
    print("2. Hackear panel")
    print("3. Descansar")

    opcion = input("Seleccione una opción: ").strip()

    while (
        not opcion.isdigit()
        or int(opcion) < 1
        or int(opcion) > 3
    ):
        print("Error: debe ingresar un número entre 1 y 3.")
        opcion = input("Seleccione una opción: ").strip()

    opcion = int(opcion)

    if opcion == 1:
        forzadas_seguidas += 1

        energia -= 20
        tiempo -= 2

        print("\nIntentás forzar la cerradura.")
        print("Perdés 20 puntos de energía y 2 de tiempo.")

        # Regla anti-spam
        if forzadas_seguidas == 3:
            alarma = True
            forzadas_seguidas = 0

            print("La cerradura se trabó.")
            print("La alarma se activó.")
            print("No se abrió ninguna cerradura.")

        else:
            if energia < 40 and not alarma:
                print("Tenés menos de 40 puntos de energía.")
                print("Existe riesgo de activar la alarma.")

                numero_riesgo = input(
                    "Elegí un número entre 1 y 3: "
                ).strip()

                while (
                    not numero_riesgo.isdigit()
                    or int(numero_riesgo) < 1
                    or int(numero_riesgo) > 3
                ):
                    print("Error: ingrese un número entre 1 y 3.")
                    numero_riesgo = input(
                        "Elegí un número entre 1 y 3: "
                    ).strip()

                numero_riesgo = int(numero_riesgo)

                if numero_riesgo == 3:
                    alarma = True
                    print("Elegiste 3. La alarma se activó.")

            if not alarma:
                cerraduras_abiertas += 1
                print("¡Cerradura abierta!")

            else:
                print("No se pudo abrir la cerradura por la alarma.")

    elif opcion == 2:
        forzadas_seguidas = 0

        energia -= 10
        tiempo -= 3

        print("\nIniciando hackeo...")
        print("Perdés 10 puntos de energía y 3 de tiempo.")

        for paso in range(1, 5):
            codigo_parcial += "A"

            print(
                f"Paso {paso}/4 completado. "
                f"Código parcial: {codigo_parcial}"
            )

        if len(codigo_parcial) >= 8:
            if cerraduras_abiertas < 3:
                cerraduras_abiertas += 1
                print("Código completado.")
                print("¡Se abrió una cerradura automáticamente!")

                codigo_parcial = ""

    elif opcion == 3:
        forzadas_seguidas = 0

        energia += 15
        tiempo -= 1

        if energia > 100:
            energia = 100

        print("\nDescansaste.")
        print("Recuperás 15 puntos de energía.")
        print("Perdés 1 punto de tiempo.")

        if alarma:
            energia -= 10
            print("La alarma está activa.")
            print("Perdés 10 puntos adicionales de energía.")

    if alarma and tiempo <= 3 and cerraduras_abiertas < 3:
        bloqueado = True

print("\n==============================")
print("       RESULTADO FINAL")
print("==============================")

if cerraduras_abiertas == 3:
    print(f"VICTORIA, agente {agente}.")
    print("Lograste abrir la bóveda.")

elif bloqueado:
    print("DERROTA.")
    print("La alarma bloqueó definitivamente el sistema.")

elif energia <= 0:
    print("DERROTA.")
    print("Te quedaste sin energía.")

elif tiempo <= 0:
    print("DERROTA.")
    print("Te quedaste sin tiempo.")

# Ejercicio 5 - Escape Room: La Arena del Gladiador

print("--- BIENVENIDO A LA ARENA ---")

nombre = input("Nombre del Gladiador: ").strip()

while not nombre.isalpha():
    print("Error: Solo se permiten letras.")
    nombre = input("Nombre del Gladiador: ").strip()

vida_gladiador = 100
vida_enemigo = 100
pociones = 3

danio_ataque_pesado = 15
danio_enemigo = 12

turno_gladiador = True
juego_activo = True

print("\n=== INICIO DEL COMBATE ===")

while juego_activo and vida_gladiador > 0 and vida_enemigo > 0:

    if turno_gladiador:
        print(
            f"\n{nombre} (HP: {vida_gladiador:g}) "
            f"vs Enemigo (HP: {vida_enemigo:g}) "
            f"| Pociones: {pociones}"
        )

        print("\nElige acción:")
        print("1. Ataque Pesado")
        print("2. Ráfaga Veloz")
        print("3. Curar")

        opcion = input("Opción: ").strip()

        while (
            not opcion.isdigit()
            or int(opcion) < 1
            or int(opcion) > 3
        ):
            if not opcion.isdigit():
                print("Error: Ingrese un número válido.")
            else:
                print("Error: La opción debe estar entre 1 y 3.")

            opcion = input("Opción: ").strip()

        opcion = int(opcion)

        if opcion == 1:
            danio_final = float(danio_ataque_pesado)

            if vida_enemigo < 20:
                danio_final *= 1.5
                print("\n¡GOLPE CRÍTICO!")

            vida_enemigo -= danio_final

            print(
                f"¡Atacaste al enemigo por "
                f"{danio_final:g} puntos de daño!"
            )

        elif opcion == 2:
            print("\n>> ¡Inicias una ráfaga de golpes!")

            for golpe in range(3):
                vida_enemigo -= 5
                print("> Golpe conectado por 5 de daño")

        elif opcion == 3:
            if pociones > 0:
                vida_gladiador += 30
                pociones -= 1

                print("\n¡Usaste una poción!")
                print("Recuperaste 30 puntos de vida.")
                print(f"Pociones restantes: {pociones}")

            else:
                print("\n¡No quedan pociones!")
                print("Perdiste el turno.")

        if vida_enemigo > 0:
            turno_gladiador = False
        else:
            juego_activo = False

    else:
        vida_gladiador -= danio_enemigo

        print(
            f"\n>> ¡El enemigo contraataca por "
            f"{danio_enemigo} puntos!"
        )

        if vida_gladiador > 0:
            turno_gladiador = True
            print("\n=== NUEVO TURNO ===")
        else:
            juego_activo = False

print("\n============================")
print("       FIN DEL COMBATE")
print("============================")

if vida_gladiador > 0:
    print(f"¡VICTORIA! {nombre} ha ganado la batalla.")
else:
    print("DERROTA. Has caído en combate.")