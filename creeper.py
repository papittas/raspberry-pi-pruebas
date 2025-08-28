from sense_hat import SenseHat

sense = SenseHat()

# Definición de colores
verde = (0, 204, 0)
verde_claro = (102, 255, 102)
negro = (0, 0, 0)
blanco = (255, 255, 255)

# Matriz 8x8 basada en tu imagen
creeper = [
    verde, verde, verde, verde, verde, verde, verde, verde,
    verde, verde_claro, verde_claro, verde, verde_claro, verde_claro, verde, verde,
    verde, negro, negro, verde, verde, negro, negro, verde,
    verde, negro, negro, verde, verde, negro, negro, verde,
    verde, verde, verde, negro, negro, verde, verde, verde,
    verde, verde, negro, negro, negro, negro, verde, verde,
    verde, negro, verde, negro, negro, verde, negro, verde,
    verde, verde, negro, verde, verde, negro, verde, verde
]

sense.set_pixels(creeper)