# 🧬 JUEGO DE LA VIDA DE CONWAY para Raspberry Pi Sense HAT 🧬
# Autor: GitHub Copilot
# Un autómata celular que simula la evolución de la vida

from sense_hat import SenseHat
import time
import copy

sense = SenseHat()
sense.clear()

# 🎨 COLORES
DEAD_COLOR = (0, 0, 0)           # Negro - célula muerta
ALIVE_COLOR = (0, 255, 0)        # Verde - célula viva
CURSOR_COLOR = (255, 255, 0)     # Amarillo - cursor
EDITING_COLOR = (255, 128, 0)    # Naranja - célula siendo editada

# 🎮 ESTADO DEL JUEGO
class ConwayGame:
    def __init__(self):
        # Grilla 8x8 para el juego
        self.grid = [[False for _ in range(8)] for _ in range(8)]
        self.cursor_x = 4
        self.cursor_y = 4
        self.editing_mode = True  # True = editando, False = simulando
        self.generation = 0
        self.paused = False
        
        print("JUEGO DE LA VIDA DE CONWAY")
        print("CONTROLES:")
        print("   Flechas del joystick: Mover cursor")
        print("   Centro del joystick: Colocar/quitar celula")
        print("   Comandos de consola:")
        print("     y - Iniciar/pausar simulacion")
        print("     c - Limpiar grilla")
        print("     1-4 - Cargar patrones")
        print("     h - Ayuda")
        print("     q - Salir")
        print("\nCrea patrones y observa la evolucion!")
        
    def count_neighbors(self, x, y):
        """Cuenta los vecinos vivos de una célula"""
        count = 0
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx == 0 and dy == 0:
                    continue
                nx, ny = x + dx, y + dy
                # Verificar límites
                if 0 <= nx < 8 and 0 <= ny < 8:
                    if self.grid[ny][nx]:
                        count += 1
        return count
    
    def evolve(self):
        """Aplica las reglas del Juego de la Vida para la siguiente generación"""
        new_grid = [[False for _ in range(8)] for _ in range(8)]
        
        for y in range(8):
            for x in range(8):
                neighbors = self.count_neighbors(x, y)
                
                # Reglas del Juego de la Vida de Conway:
                if self.grid[y][x]:  # Célula viva
                    # 1. Cualquier célula viva con 2 o 3 vecinos vivos sobrevive
                    if neighbors == 2 or neighbors == 3:
                        new_grid[y][x] = True
                    # 2. De lo contrario, muere por soledad o sobrepoblación
                else:  # Célula muerta
                    # 3. Cualquier célula muerta con exactamente 3 vecinos vivos nace
                    if neighbors == 3:
                        new_grid[y][x] = True
        
        self.grid = new_grid
        self.generation += 1
        
        print(f"Generacion {self.generation}")
        
        # Verificar si hay células vivas
        alive_count = sum(sum(row) for row in self.grid)
        if alive_count == 0:
            print("Todas las celulas han muerto - simulacion detenida")
            self.editing_mode = True
            self.generation = 0
    
    def toggle_cell(self, x, y):
        """Alternar el estado de una célula"""
        self.grid[y][x] = not self.grid[y][x]
        action = "colocada" if self.grid[y][x] else "eliminada"
        print(f"Celula {action} en ({x}, {y})")
    
    def clear_grid(self):
        """Limpiar toda la grilla"""
        self.grid = [[False for _ in range(8)] for _ in range(8)]
        self.generation = 0
        print("Grilla limpiada")
    
    def load_pattern(self, pattern_name):
        """Cargar patrones predefinidos"""
        self.clear_grid()
        
        if pattern_name == "glider":
            # Glider clásico
            pattern = [(1, 0), (2, 1), (0, 2), (1, 2), (2, 2)]
            for x, y in pattern:
                if 0 <= x < 8 and 0 <= y < 8:
                    self.grid[y][x] = True
            print("Patron 'Glider' cargado")
            
        elif pattern_name == "blinker":
            # Oscilador simple
            pattern = [(3, 4), (4, 4), (5, 4)]
            for x, y in pattern:
                if 0 <= x < 8 and 0 <= y < 8:
                    self.grid[y][x] = True
            print("Patron 'Blinker' cargado")
            
        elif pattern_name == "block":
            # Bloque estático
            pattern = [(3, 3), (3, 4), (4, 3), (4, 4)]
            for x, y in pattern:
                if 0 <= x < 8 and 0 <= y < 8:
                    self.grid[y][x] = True
            print("Patron 'Block' cargado")
            
        elif pattern_name == "toad":
            # Oscilador toad
            pattern = [(2, 3), (3, 3), (4, 3), (1, 4), (2, 4), (3, 4)]
            for x, y in pattern:
                if 0 <= x < 8 and 0 <= y < 8:
                    self.grid[y][x] = True
            print("Patron 'Toad' cargado")
    
    def render(self):
        """Renderizar la grilla en el Sense HAT"""
        for y in range(8):
            for x in range(8):
                if self.editing_mode and x == self.cursor_x and y == self.cursor_y:
                    # Mostrar cursor en modo edición
                    if self.grid[y][x]:
                        color = EDITING_COLOR  # Naranja si hay célula
                    else:
                        color = CURSOR_COLOR   # Amarillo si está vacío
                else:
                    # Mostrar célula normal
                    color = ALIVE_COLOR if self.grid[y][x] else DEAD_COLOR
                
                sense.set_pixel(x, y, color)
        
        # Mostrar información en pantalla cada cierto tiempo
        if self.editing_mode:
            # Parpadeo suave del cursor
            cursor_brightness = 0.7 + 0.3 * abs(time.time() % 1 - 0.5) * 2
            cursor_color = tuple(int(c * cursor_brightness) for c in CURSOR_COLOR)
            sense.set_pixel(self.cursor_x, self.cursor_y, cursor_color)

def handle_keyboard_input(game):
    """Maneja la entrada del teclado usando los eventos del joystick del Sense HAT"""
    
    def joystick_pressed(event):
        if event.action != 'pressed':
            return
            
        if event.direction == 'up':
            game.cursor_y = max(0, game.cursor_y - 1)
            print(f"Cursor en ({game.cursor_x}, {game.cursor_y})")
            
        elif event.direction == 'down':
            game.cursor_y = min(7, game.cursor_y + 1)
            print(f"Cursor en ({game.cursor_x}, {game.cursor_y})")
            
        elif event.direction == 'left':
            game.cursor_x = max(0, game.cursor_x - 1)
            print(f"Cursor en ({game.cursor_x}, {game.cursor_y})")
            
        elif event.direction == 'right':
            game.cursor_x = min(7, game.cursor_x + 1)
            print(f"Cursor en ({game.cursor_x}, {game.cursor_y})")
            
        elif event.direction == 'middle':
            if game.editing_mode:
                # ENTER - Colocar/quitar célula
                game.toggle_cell(game.cursor_x, game.cursor_y)
            else:
                # En modo simulación, pausar/reanudar
                game.paused = not game.paused
                status = "pausada" if game.paused else "reanudada"
                print(f"Simulacion {status}")
    
    sense.stick.direction_any = joystick_pressed

def handle_console_input(game):
    """Maneja comandos desde la consola de manera no bloqueante"""
    import threading
    import sys
    import select
    
    def console_thread():
        while True:
            try:
                # Solo en Linux/Unix - para Windows usar input() alternativo
                if hasattr(select, 'select'):
                    ready, _, _ = select.select([sys.stdin], [], [], 0.1)
                    if ready:
                        command = sys.stdin.readline().strip().lower()
                        process_command(command, game)
                else:
                    # Para Windows - método simplificado
                    time.sleep(0.1)
            except:
                time.sleep(0.1)
    
    def process_command(command, game):
        if command == 'y':
            # Alternar entre modo edición y simulación
            if game.editing_mode:
                game.editing_mode = False
                game.paused = False
                print("Modo SIMULACION iniciado")
            else:
                game.editing_mode = True
                print("Modo EDICION activado")
                
        elif command == 'p':
            # Pausar/reanudar simulación
            if not game.editing_mode:
                game.paused = not game.paused
                status = "pausada" if game.paused else "reanudada"
                print(f"Simulacion {status}")
                
        elif command == 'c':
            # Limpiar grilla
            game.clear_grid()
            
        elif command == 'r':
            # Volver a modo edición
            game.editing_mode = True
            print("Modo EDICION activado")
            
        elif command in ['1', '2', '3', '4']:
            # Cargar patrones
            patterns = {'1': 'glider', '2': 'blinker', '3': 'block', '4': 'toad'}
            game.load_pattern(patterns[command])
            game.editing_mode = True
            
        elif command == 'q':
            print("Saliendo del juego...")
            exit()
            
        elif command == 'h' or command == 'help':
            show_help()
    
    # Iniciar hilo de consola
    thread = threading.Thread(target=console_thread, daemon=True)
    thread.start()

def show_help():
    """Mostrar ayuda de comandos"""
    print("\n=== COMANDOS DE CONSOLA ===")
    print("y - Iniciar/pausar simulacion")
    print("p - Pausar/reanudar simulacion")
    print("c - Limpiar grilla")
    print("r - Modo edicion")
    print("1 - Cargar Glider")
    print("2 - Cargar Blinker")
    print("3 - Cargar Block")
    print("4 - Cargar Toad")
    print("h - Mostrar ayuda")
    print("q - Salir")
    print("==========================")

def show_startup_animation():
    """Animación de inicio"""
    sense.show_message("CONWAY", text_colour=[0, 255, 0], scroll_speed=0.08)
    sense.show_message("LIFE", text_colour=[255, 255, 0], scroll_speed=0.08)
    
    # Efecto de "células naciendo"
    for frame in range(20):
        for x in range(8):
            for y in range(8):
                if (x + y + frame) % 4 == 0:
                    intensity = min(255, frame * 13)
                    sense.set_pixel(x, y, (0, intensity, 0))
        time.sleep(0.1)
    
    time.sleep(0.5)
    sense.clear()

def show_menu():
    """Mostrar menú de patrones"""
    print("\nPATRONES DISPONIBLES:")
    print("   1: Glider (se mueve)")
    print("   2: Blinker (oscila)")
    print("   3: Block (estatico)")
    print("   4: Toad (oscila)")
    print("   C: Continuar editando")

def main():
    print("=" * 40)
    print("     JUEGO DE LA VIDA DE CONWAY")
    print("       Sense HAT Edition")
    print("=" * 40)
    
    show_startup_animation()
    
    game = ConwayGame()
    handle_keyboard_input(game)
    handle_console_input(game)  # Agregar manejo de consola
    
    # Cargar un patrón inicial
    game.load_pattern("glider")
    
    print("\nJuego iniciado!")
    print("Usa el joystick para navegar")
    print("Modo: EDICION")
    print("Escribe 'h' + ENTER para ver comandos")
    
    last_evolution = time.time()
    evolution_speed = 1.0  # segundos entre generaciones
    
    try:
        while True:
            current_time = time.time()
            
            # Renderizar siempre
            game.render()
            
            # Evolución automática en modo simulación
            if not game.editing_mode and not game.paused:
                if current_time - last_evolution >= evolution_speed:
                    game.evolve()
                    last_evolution = current_time
            
            time.sleep(0.05)  # 20 FPS
            
    except KeyboardInterrupt:
        print("\nFin de la simulacion")
        print(f"Generaciones completadas: {game.generation}")
        
        # Animación de cierre
        for fade in range(255, 0, -15):
            for x in range(8):
                for y in range(8):
                    if game.grid[y][x]:
                        color = (0, fade, 0)
                        sense.set_pixel(x, y, color)
            time.sleep(0.05)
        
        sense.show_message("BYE", text_colour=[255, 255, 0], scroll_speed=0.1)
        sense.clear()

# Función adicional para controles extendidos via input del terminal
def show_patterns_menu():
    """Mostrar menu de patrones disponibles"""
    print("\nPATRONES DISPONIBLES:")
    print("1 - Glider (se mueve diagonalmente)")
    print("2 - Blinker (oscila vertical/horizontal)")
    print("3 - Block (patron estatico)")
    print("4 - Toad (oscilador periodo 2)")
    print("Escribe el numero + ENTER para cargar")

if __name__ == "__main__":
    main()
