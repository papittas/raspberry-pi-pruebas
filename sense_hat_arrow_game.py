# sense_hat_arrow_game.py
"""
Juego de reflejos con Sense HAT para Raspberry Pi
- Muestra una flecha en una dirección aleatoria (arriba, abajo, izquierda, derecha)
- El jugador debe inclinar la Raspberry Pi en la dirección de la flecha
- Mide el tiempo de reacción
- Al final muestra el promedio de reflejos y una tabla de clasificación local
"""
import time
import random
import os
from sense_hat import SenseHat

# Configuración
DIRECCIONES = ['arriba', 'abajo', 'izquierda', 'derecha']
FLECHAS = {
    'arriba': [
        [0,0,0,0,1,0,0,0],
        [0,0,0,1,1,0,0,0],
        [0,0,1,0,1,0,0,0],
        [0,1,0,0,1,0,0,0],
        [1,1,1,1,1,1,1,0],
        [0,0,0,0,1,0,0,0],
        [0,0,0,0,1,0,0,0],
        [0,0,0,0,1,0,0,0],
    ],
    'abajo': [
        [0,0,0,0,1,0,0,0],
        [0,0,0,0,1,0,0,0],
        [0,0,0,0,1,0,0,0],
        [1,1,1,1,1,1,1,0],
        [0,1,0,0,1,0,0,0],
        [0,0,1,0,1,0,0,0],
        [0,0,0,1,1,0,0,0],
        [0,0,0,0,1,0,0,0],
    ],
    'izquierda': [
        [0,0,0,0,1,0,0,0],
        [0,0,0,1,1,0,0,0],
        [0,0,1,0,1,0,0,0],
        [0,1,0,0,1,0,0,0],
        [1,1,1,1,1,1,1,0],
        [0,1,0,0,1,0,0,0],
        [0,0,1,0,1,0,0,0],
        [0,0,0,1,1,0,0,0],
    ],
    'derecha': [
        [0,0,0,1,0,0,0,0],
        [0,0,1,1,0,0,0,0],
        [0,1,0,1,0,0,0,0],
        [0,1,0,0,0,0,0,0],
        [1,1,1,1,1,1,1,0],
        [0,1,0,0,0,0,0,0],
        [0,1,0,1,0,0,0,0],
        [0,0,1,1,0,0,0,0],
    ],
}
COLOR = (0, 255, 0)
FONDO = (0, 0, 0)
CLASIFICACION_FILE = 'clasificacion.txt'

sense = SenseHat()

def mostrar_flecha(direccion):
    matriz = FLECHAS[direccion]
    pixels = [COLOR if cell else FONDO for row in matriz for cell in row]
    sense.set_pixels(pixels)

def leer_inclinacion():
    orientation = sense.get_orientation_degrees()
    pitch = orientation['pitch']
    roll = orientation['roll']
    # print(f"Pitch: {pitch}, Roll: {roll}")
    if pitch < 45 or pitch > 315:
        return 'arriba'
    elif 135 < pitch < 225:
        return 'abajo'
    elif roll > 45 and roll < 135:
        return 'izquierda'
    elif roll > 225 and roll < 315:
        return 'derecha'
    return None

def jugar_ronda():
    direccion = random.choice(DIRECCIONES)
    mostrar_flecha(direccion)
    tiempo_inicio = time.time()
    while True:
        respuesta = leer_inclinacion()
        if respuesta == direccion:
            break
        time.sleep(0.05)
    tiempo_reaccion = time.time() - tiempo_inicio
    sense.clear()
    return tiempo_reaccion, direccion

def pedir_nombre():
    nombre = input("Ingresa tu nombre: ")
    return nombre.strip()[:10]

def guardar_clasificacion(nombre, promedio):
    linea = f"{nombre},{promedio:.3f}\n"
    with open(CLASIFICACION_FILE, 'a') as f:
        f.write(linea)

def cargar_clasificacion():
    if not os.path.exists(CLASIFICACION_FILE):
        return []
    with open(CLASIFICACION_FILE, 'r') as f:
        lineas = f.readlines()
    clasif = []
    for l in lineas:
        try:
            n, p = l.strip().split(',')
            clasif.append((n, float(p)))
        except:
            continue
    clasif.sort(key=lambda x: x[1])
    return clasif[:5]

def mostrar_tabla(clasif):
    print("\n--- TABLA DE CLASIFICACIÓN ---")
    print("Pos | Nombre     | Promedio (s)")
    for i, (n, p) in enumerate(clasif, 1):
        print(f"{i:>3} | {n:<10} | {p:.3f}")

def main():
    print("\n¡Bienvenido al juego de reflejos con Sense HAT!")
    nombre = pedir_nombre()
    rondas = 5
    tiempos = []
    for i in range(rondas):
        print(f"Ronda {i+1}/{rondas}... ¡Prepárate!")
        time.sleep(random.uniform(1, 2.5))
        t, d = jugar_ronda()
        print(f"¡Correcto! Tiempo de reacción: {t:.3f} s (Dirección: {d})")
        tiempos.append(t)
        time.sleep(0.7)
    promedio = sum(tiempos) / len(tiempos)
    print(f"\nTu tiempo promedio de reflejo fue: {promedio:.3f} segundos")
    guardar_clasificacion(nombre, promedio)
    clasif = cargar_clasificacion()
    mostrar_tabla(clasif)
    print("\n¡Gracias por jugar!")
    sense.show_message("Fin!", text_colour=COLOR)
    sense.clear()

if __name__ == "__main__":
    main()
