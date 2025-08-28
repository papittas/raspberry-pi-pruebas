# Snake para Raspberry Pi Sense HAT
# Autor: GitHub Copilot
# Este juego utiliza la pantalla LED y el joystick del Sense HAT

from sense_hat import SenseHat
from time import sleep
import random

sense = SenseHat()
sense.clear()

# Colores
SNAKE_COLOR = (0, 255, 0)
FOOD_COLOR = (255, 0, 0)
BG_COLOR = (0, 0, 0)

# Direcciones
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

direction = RIGHT
next_direction = RIGHT

# Inicializar serpiente y comida
snake = [(4, 4), (3, 4)]
food = (random.randint(0, 7), random.randint(0, 7))
while food in snake:
    food = (random.randint(0, 7), random.randint(0, 7))

def draw():
    sense.clear()
    for segment in snake:
        sense.set_pixel(segment[0], segment[1], SNAKE_COLOR)
    sense.set_pixel(food[0], food[1], FOOD_COLOR)

def move():
    global snake, food, direction
    new_head = (snake[0][0] + direction[0], snake[0][1] + direction[1])
    # Comprobar colisiones
    if (new_head[0] < 0 or new_head[0] > 7 or
        new_head[1] < 0 or new_head[1] > 7 or
        new_head in snake):
        sense.show_message('Game Over', text_colour=[255,0,0])
        sense.clear()
        exit()
    snake.insert(0, new_head)
    if new_head == food:
        # Nueva comida
        while True:
            food_pos = (random.randint(0, 7), random.randint(0, 7))
            if food_pos not in snake:
                break
        globals()['food'] = food_pos
    else:
        snake.pop()

def joystick_event(event):
    global next_direction
    if event.action != 'pressed':
        return
    if event.direction == 'up' and direction != DOWN:
        next_direction = UP
    elif event.direction == 'down' and direction != UP:
        next_direction = DOWN
    elif event.direction == 'left' and direction != RIGHT:
        next_direction = LEFT
    elif event.direction == 'right' and direction != LEFT:
        next_direction = RIGHT

sense.stick.direction_any = joystick_event

def main():
    global direction
    while True:
        direction = next_direction
        move()
        draw()
        sleep(0.3)

if __name__ == '__main__':
    main()
