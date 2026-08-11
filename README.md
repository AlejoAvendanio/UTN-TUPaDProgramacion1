# UTN-TUPaDProgramacion1

Trabajos prácticos de **Programación 1** — Tecnicatura Universitaria en Programación a Distancia (TUPaD), UTN.

Repositorio personal donde subo las resoluciones de los TP de la materia. Todo está hecho en Python, sin librerías externas, usando únicamente los contenidos vistos en clase.

## Contenido

### TP Integrador — Secuenciales, Condicionales y Repetitivas

Archivo: `# TP integrador – Repetitivas- Condicion.py`

Cinco ejercicios que combinan entrada de datos por consola, validación de lo que ingresa el usuario, condicionales anidados, bucles `while` / `for` y acumuladores y contadores:

1. **Caja de Kiosco** — carga de N productos con precio y descuento opcional del 10%, y resumen final con total sin descuento, total con descuento, ahorro y promedio por producto.
2. **Acceso al Campus y Menú Seguro** — login con máximo de 3 intentos y bloqueo de cuenta, más un menú interactivo con cambio de clave (mínimo 6 caracteres y confirmación).
3. **Agenda de Turnos** — reserva, cancelación y consulta de turnos para lunes y martes, sin usar listas: cada turno es una variable independiente. Incluye control de pacientes repetidos y resumen general de ocupación.
4. **Escape Room: La Bóveda** — juego por turnos con energía, tiempo y alarma. El agente puede forzar cerraduras, hackear el panel o descansar, con reglas anti-spam y varias condiciones de victoria y derrota.
5. **La Arena del Gladiador** — combate por turnos contra un enemigo, con ataque pesado (golpe crítico si el enemigo está debilitado), ráfaga de golpes y pociones de curación limitadas.

Todos los ejercicios validan los datos ingresados: no aceptan texto donde va un número, ni valores fuera de rango, ni opciones inválidas de menú.

## Cómo ejecutarlo

Requiere Python 3.

```bash
python "# TP integrador – Repetitivas- Condicion.py"
```

Los programas son interactivos: se van pidiendo los datos por consola a medida que corren. Al ser un único archivo, los cinco ejercicios se ejecutan uno tras otro.

## Autor

Alejo Avendaño — TUPaD, UTN.
