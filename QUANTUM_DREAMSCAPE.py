# 🌟 QUANTUM DREAMSCAPE 🌟
# Un ecosistema digital interactivo que evoluciona con sensores ambientales
# Combina arte generativo, física cuántica simulada y respuesta emocional

from sense_hat import SenseHat
import random
import math
import time
import threading
from collections import deque

sense = SenseHat()
sense.clear()

# 🎨 PALETAS DE COLORES EVOLUTIVAS
palettes = {
    'aurora': [(255, 0, 255), (0, 255, 255), (255, 255, 0), (0, 255, 0)],
    'nebula': [(128, 0, 255), (255, 0, 128), (0, 128, 255), (255, 128, 0)],
    'plasma': [(255, 0, 0), (255, 255, 0), (0, 255, 255), (255, 0, 255)],
    'ocean': [(0, 100, 255), (0, 200, 255), (100, 255, 255), (0, 150, 200)],
    'fire': [(255, 0, 0), (255, 100, 0), (255, 200, 0), (255, 255, 100)]
}

class QuantumParticle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.velocity_x = random.uniform(-0.3, 0.3)
        self.velocity_y = random.uniform(-0.3, 0.3)
        self.energy = random.uniform(0.1, 1.0)
        self.phase = random.uniform(0, 2 * math.pi)
        self.lifespan = random.randint(50, 200)
        self.age = 0
        
    def update(self, gravity_x=0, gravity_y=0):
        # Cuántica: superposición de estados
        self.phase += 0.1
        quantum_offset_x = 0.1 * math.sin(self.phase)
        quantum_offset_y = 0.1 * math.cos(self.phase * 1.3)
        
        # Física emergente
        self.velocity_x += gravity_x + quantum_offset_x
        self.velocity_y += gravity_y + quantum_offset_y
        
        # Entanglement - las partículas se atraen/repelen entre sí
        self.velocity_x *= 0.98  # fricción cuántica
        self.velocity_y *= 0.98
        
        self.x += self.velocity_x
        self.y += self.velocity_y
        
        # Wrapping cuántico - teletransporte a través de los bordes
        if self.x < 0: self.x = 7
        elif self.x > 7: self.x = 0
        if self.y < 0: self.y = 7
        elif self.y > 7: self.y = 0
        
        self.age += 1
        return self.age < self.lifespan

class EmotionalEcosystem:
    def __init__(self):
        self.particles = []
        self.mood = 'calm'  # calm, excited, meditative, chaotic, harmonious
        self.temperature_history = deque(maxlen=10)
        self.pressure_history = deque(maxlen=10)
        self.motion_intensity = 0
        self.current_palette = 'aurora'
        self.time_cycle = 0
        self.gravity_x = 0
        self.gravity_y = 0
        
        # Generar partículas iniciales
        for _ in range(12):
            self.spawn_particle()
    
    def spawn_particle(self):
        if len(self.particles) < 20:
            x = random.uniform(0, 7)
            y = random.uniform(0, 7)
            self.particles.append(QuantumParticle(x, y))
    
    def analyze_environment(self):
        """Análisis emocional del entorno usando sensores"""
        try:
            temp = sense.get_temperature()
            pressure = sense.get_pressure()
            accel = sense.get_accelerometer_raw()
            
            self.temperature_history.append(temp)
            self.pressure_history.append(pressure)
            
            # Calcular intensidad de movimiento
            motion = math.sqrt(accel['x']**2 + accel['y']**2 + accel['z']**2)
            self.motion_intensity = motion
            
            # Determinar el estado emocional basado en sensores
            temp_trend = 0 if len(self.temperature_history) < 2 else \
                        self.temperature_history[-1] - self.temperature_history[-2]
            
            if motion > 1.2:
                self.mood = 'chaotic'
                self.current_palette = 'fire'
                self.gravity_x = (accel['x'] * 0.05)
                self.gravity_y = (accel['y'] * 0.05)
            elif temp > 30:
                self.mood = 'excited'
                self.current_palette = 'plasma'
            elif pressure > 1020:
                self.mood = 'harmonious'
                self.current_palette = 'ocean'
            elif temp_trend < -0.5:
                self.mood = 'meditative'
                self.current_palette = 'nebula'
            else:
                self.mood = 'calm'
                self.current_palette = 'aurora'
                
        except Exception as e:
            # Fallback si hay problemas con sensores
            self.mood = 'calm'
    
    def get_color_by_energy(self, energy, position):
        """Color dinámico basado en energía y posición"""
        palette = palettes[self.current_palette]
        
        # Efecto de ondas sinusoidales
        wave = math.sin(self.time_cycle * 0.1 + position * 0.5)
        color_index = int((energy + wave + 1) * 2) % len(palette)
        
        base_color = palette[color_index]
        
        # Modulación de intensidad basada en mood
        intensity_map = {
            'calm': 0.6,
            'excited': 1.0,
            'meditative': 0.4,
            'chaotic': 0.9,
            'harmonious': 0.7
        }
        
        intensity = intensity_map.get(self.mood, 0.6)
        return tuple(int(c * intensity) for c in base_color)
    
    def particle_interactions(self):
        """Simula interacciones cuánticas entre partículas"""
        for i, p1 in enumerate(self.particles):
            for j, p2 in enumerate(self.particles[i+1:], i+1):
                dx = p2.x - p1.x
                dy = p2.y - p1.y
                distance = math.sqrt(dx**2 + dy**2)
                
                if distance < 2.0 and distance > 0:
                    # Entanglement cuántico - intercambio de energía
                    if random.random() < 0.1:
                        p1.energy, p2.energy = p2.energy, p1.energy
                    
                    # Fuerza de atracción/repulsión
                    force = 0.01 / (distance + 0.1)
                    if p1.energy > p2.energy:
                        force *= -1  # repulsión
                    
                    p1.velocity_x -= force * dx
                    p1.velocity_y -= force * dy
                    p2.velocity_x += force * dx
                    p2.velocity_y += force * dy
    
    def update(self):
        self.time_cycle += 1
        self.analyze_environment()
        self.particle_interactions()
        
        # Actualizar partículas
        self.particles = [p for p in self.particles if p.update(self.gravity_x, self.gravity_y)]
        
        # Spawn nuevas partículas basado en el mood
        spawn_rates = {
            'calm': 0.05,
            'excited': 0.15,
            'meditative': 0.03,
            'chaotic': 0.2,
            'harmonious': 0.08
        }
        
        if random.random() < spawn_rates.get(self.mood, 0.05):
            self.spawn_particle()
    
    def render(self):
        # Limpiar matriz
        matrix = [[(0, 0, 0) for _ in range(8)] for _ in range(8)]
        
        # Renderizar partículas con efectos especiales
        for p in self.particles:
            px, py = int(p.x), int(p.y)
            if 0 <= px < 8 and 0 <= py < 8:
                position_factor = px + py * 8
                color = self.get_color_by_energy(p.energy, position_factor)
                
                # Anti-aliasing cuántico - mezcla con píxeles adyacentes
                matrix[py][px] = color
                
                # Efecto de aura
                for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
                    nx, ny = px + dx, py + dy
                    if 0 <= nx < 8 and 0 <= ny < 8:
                        aura_color = tuple(int(c * 0.3) for c in color)
                        current = matrix[ny][nx]
                        matrix[ny][nx] = tuple(min(255, current[i] + aura_color[i]) for i in range(3))
        
        # Efecto de respiración global basado en tiempo
        breath = 0.8 + 0.2 * math.sin(self.time_cycle * 0.05)
        
        # Aplicar a sense hat
        for y in range(8):
            for x in range(8):
                color = matrix[y][x]
                final_color = tuple(int(c * breath) for c in color)
                sense.set_pixel(x, y, final_color)

def joystick_handler(event):
    """Control interactivo del ecosistema"""
    if event.action == 'pressed':
        if event.direction == 'middle':
            # Cambiar modo manualmente
            ecosystem.mood = random.choice(['calm', 'excited', 'meditative', 'chaotic', 'harmonious'])
        elif event.direction == 'up':
            ecosystem.gravity_y -= 0.02
        elif event.direction == 'down':
            ecosystem.gravity_y += 0.02
        elif event.direction == 'left':
            ecosystem.gravity_x -= 0.02
        elif event.direction == 'right':
            ecosystem.gravity_x += 0.02

def startup_animation():
    """Animación de inicio épica"""
    sense.show_message("QUANTUM", text_colour=[255, 0, 255], scroll_speed=0.1)
    sense.show_message("DREAMSCAPE", text_colour=[0, 255, 255], scroll_speed=0.1)
    
    # Efecto de materialización
    for intensity in range(0, 256, 8):
        for x in range(8):
            for y in range(8):
                if random.random() < 0.3:
                    color = (intensity//3, 0, intensity)
                    sense.set_pixel(x, y, color)
        time.sleep(0.05)
    
    time.sleep(0.5)
    sense.clear()

def main():
    global ecosystem
    
    print("🌟 Inicializando Quantum Dreamscape...")
    startup_animation()
    
    ecosystem = EmotionalEcosystem()
    sense.stick.direction_any = joystick_handler
    
    print("✨ Ecosistema digital activo!")
    print("🎮 Controles:")
    print("   • Joystick: Alterar gravedad cuántica")
    print("   • Centro: Cambiar mood aleatorio")
    print("   • Los sensores influyen en el ecosistema")
    
    try:
        while True:
            ecosystem.update()
            ecosystem.render()
            time.sleep(0.08)  # ~12 FPS para fluidez
            
    except KeyboardInterrupt:
        print("\n🌙 Cerrando Quantum Dreamscape...")
        sense.show_message("BYE", text_colour=[255, 255, 0], scroll_speed=0.1)
        sense.clear()

if __name__ == "__main__":
    main()
