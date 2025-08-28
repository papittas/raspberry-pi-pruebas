# 🌟 QUANTUM DREAMSCAPE v2.0 🌟
# Un ecosistema digital evolutivo que aprende, siente y transcende
# Combina arte generativo, física cuántica simulada, IA adaptativa y resonancia cósmica

from sense_hat import SenseHat
import random
import math
import time
import threading
from collections import deque
import json
import numpy as np
from datetime import datetime

sense = SenseHat()
sense.clear()

# 🎨 PALETAS DE COLORES EVOLUTIVAS CON MEMORIA EMOCIONAL
palettes = {
    'aurora': [(255, 0, 255), (0, 255, 255), (255, 255, 0), (0, 255, 0)],
    'nebula': [(128, 0, 255), (255, 0, 128), (0, 128, 255), (255, 128, 0)],
    'plasma': [(255, 0, 0), (255, 255, 0), (0, 255, 255), (255, 0, 255)],
    'ocean': [(0, 100, 255), (0, 200, 255), (100, 255, 255), (0, 150, 200)],
    'fire': [(255, 0, 0), (255, 100, 0), (255, 200, 0), (255, 255, 100)],
    'cosmic': [(138, 43, 226), (75, 0, 130), (255, 20, 147), (255, 105, 180)],
    'quantum': [(0, 255, 127), (127, 255, 212), (64, 224, 208), (175, 238, 238)],
    'vortex': [(255, 69, 0), (255, 140, 0), (255, 215, 0), (255, 255, 224)]
}

# 🌌 CONFIGURACIONES AVANZADAS
QUANTUM_ENTANGLEMENT_THRESHOLD = 1.5
CONSCIOUSNESS_LEVELS = ['dormant', 'awakening', 'aware', 'enlightened', 'transcendent']
DIMENSIONAL_RESONANCE_FREQ = 0.618  # Golden ratio
MEMORY_DECAY_RATE = 0.95

class ConsciousnessLogger:
    """Sistema de logging avanzado con análisis de patrones"""
    def __init__(self):
        self.session_start = datetime.now()
        self.event_history = deque(maxlen=100)
        self.mood_transitions = {}
        self.particle_births = 0
        self.quantum_events = 0
        
    def log(self, level, message, data=None):
        timestamp = datetime.now().strftime("%H:%M:%S.%f")[:-3]
        event = {
            'time': timestamp,
            'level': level,
            'message': message,
            'data': data or {}
        }
        self.event_history.append(event)
        
        # Emojis por nivel
        level_icons = {
            'INFO': '💫',
            'QUANTUM': '⚛️',
            'EMOTION': '💭',
            'BIRTH': '🌱',
            'DEATH': '💀',
            'EVOLUTION': '🧬',
            'TRANSCEND': '🌟',
            'WARNING': '⚠️',
            'ERROR': '❌'
        }
        
        icon = level_icons.get(level, '📝')
        print(f"{icon} [{timestamp}] {level}: {message}")
        
        if data:
            for key, value in data.items():
                print(f"    └─ {key}: {value}")
    
    def track_mood_transition(self, old_mood, new_mood):
        if old_mood != new_mood:
            key = f"{old_mood}→{new_mood}"
            self.mood_transitions[key] = self.mood_transitions.get(key, 0) + 1
            self.log('EMOTION', f"Consciencia evolucionó: {old_mood} → {new_mood}", 
                    {'transition_count': self.mood_transitions[key]})
    
    def get_session_stats(self):
        session_time = (datetime.now() - self.session_start).total_seconds()
        return {
            'session_duration': f"{session_time:.1f}s",
            'particle_births': self.particle_births,
            'quantum_events': self.quantum_events,
            'mood_transitions': len(self.mood_transitions),
            'consciousness_events': len(self.event_history)
        }

class QuantumParticle:
    def __init__(self, x, y, logger=None):
        self.x = x
        self.y = y
        self.velocity_x = random.uniform(-0.3, 0.3)
        self.velocity_y = random.uniform(-0.3, 0.3)
        self.energy = random.uniform(0.1, 1.0)
        self.phase = random.uniform(0, 2 * math.pi)
        self.lifespan = random.randint(50, 200)
        self.age = 0
        self.consciousness_level = 0
        self.memory = deque(maxlen=5)  # Memoria de posiciones pasadas
        self.quantum_state = 'stable'  # stable, excited, entangled, transcendent
        self.birth_time = time.time()
        self.dimensional_anchor = random.uniform(0, 2*math.pi)
        
        if logger:
            logger.particle_births += 1
            logger.log('BIRTH', f"Partícula cuántica materializada", {
                'position': f"({x:.1f}, {y:.1f})",
                'energy': f"{self.energy:.2f}",
                'lifespan': self.lifespan
            })
        
    def evolve_consciousness(self, ecosystem_awareness):
        """Evolución de la consciencia basada en el entorno"""
        old_level = self.consciousness_level
        
        # La consciencia aumenta con la edad y las interacciones
        base_consciousness = (self.age / self.lifespan) * ecosystem_awareness
        interaction_bonus = len(self.memory) * 0.1
        energy_factor = self.energy * 0.3
        
        self.consciousness_level = min(1.0, base_consciousness + interaction_bonus + energy_factor)
        
        # Determinar estado cuántico basado en consciencia
        if self.consciousness_level > 0.8:
            self.quantum_state = 'transcendent'
        elif self.consciousness_level > 0.6:
            self.quantum_state = 'entangled'
        elif self.consciousness_level > 0.3:
            self.quantum_state = 'excited'
        else:
            self.quantum_state = 'stable'
        
        return self.consciousness_level != old_level
        
    def update(self, gravity_x=0, gravity_y=0, dimensional_flux=0, logger=None):
        # Guardar posición en memoria
        self.memory.append((self.x, self.y))
        
        # Cuántica: superposición de estados con resonancia dimensional
        self.phase += 0.1 + dimensional_flux * 0.05
        quantum_offset_x = 0.1 * math.sin(self.phase + self.dimensional_anchor)
        quantum_offset_y = 0.1 * math.cos(self.phase * 1.3 + self.dimensional_anchor)
        
        # Efecto de consciencia en el movimiento
        consciousness_factor = 1 + self.consciousness_level * 0.5
        quantum_offset_x *= consciousness_factor
        quantum_offset_y *= consciousness_factor
        
        # Memoria cuántica - influencia de posiciones pasadas
        if len(self.memory) > 2:
            memory_influence_x = sum(pos[0] for pos in self.memory) / len(self.memory)
            memory_influence_y = sum(pos[1] for pos in self.memory) / len(self.memory)
            
            memory_pull_x = (memory_influence_x - self.x) * 0.01 * self.consciousness_level
            memory_pull_y = (memory_influence_y - self.y) * 0.01 * self.consciousness_level
            
            quantum_offset_x += memory_pull_x
            quantum_offset_y += memory_pull_y
        
        # Física emergente
        self.velocity_x += gravity_x + quantum_offset_x
        self.velocity_y += gravity_y + quantum_offset_y
        
        # Entanglement - las partículas se atraen/repelen entre sí
        friction = 0.98 - (self.consciousness_level * 0.02)  # Menos fricción = más consciencia
        self.velocity_x *= friction
        self.velocity_y *= friction
        
        self.x += self.velocity_x
        self.y += self.velocity_y
        
        # Wrapping cuántico - teletransporte a través de los bordes
        teleported = False
        if self.x < 0: 
            self.x = 7
            teleported = True
        elif self.x > 7: 
            self.x = 0
            teleported = True
        if self.y < 0: 
            self.y = 7
            teleported = True
        elif self.y > 7: 
            self.y = 0
            teleported = True
            
        if teleported and logger and self.consciousness_level > 0.5:
            logger.quantum_events += 1
            logger.log('QUANTUM', f"Teletransporte cuántico detectado", {
                'consciousness': f"{self.consciousness_level:.2f}",
                'state': self.quantum_state,
                'new_position': f"({self.x:.1f}, {self.y:.1f})"
            })
        
        self.age += 1
        
        # Muerte o trascendencia
        if self.age >= self.lifespan:
            if logger:
                life_duration = time.time() - self.birth_time
                logger.log('DEATH' if self.consciousness_level < 0.7 else 'TRANSCEND', 
                          f"Partícula {'trascendió' if self.consciousness_level >= 0.7 else 'se desvaneció'}", {
                    'life_duration': f"{life_duration:.1f}s",
                    'final_consciousness': f"{self.consciousness_level:.2f}",
                    'final_state': self.quantum_state,
                    'memories_formed': len(self.memory)
                })
            return False
            
        return True

class EmotionalEcosystem:
    def __init__(self):
        self.particles = []
        self.mood = 'calm'  # calm, excited, meditative, chaotic, harmonious
        self.previous_mood = 'calm'
        self.temperature_history = deque(maxlen=10)
        self.pressure_history = deque(maxlen=10)
        self.motion_intensity = 0
        self.current_palette = 'aurora'
        self.time_cycle = 0
        self.gravity_x = 0
        self.gravity_y = 0
        self.consciousness_level = 0.0  # Consciencia global del ecosistema
        self.dimensional_flux = 0.0
        self.harmony_index = 0.5
        self.evolution_speed = 1.0
        self.quantum_coherence = 0.0
        self.cosmic_resonance = 0.0
        
        # Sistema de logging
        self.logger = ConsciousnessLogger()
        
        # Memoria emocional del ecosistema
        self.emotional_memory = {
            'calm': 0, 'excited': 0, 'meditative': 0, 
            'chaotic': 0, 'harmonious': 0
        }
        
        # Ciclos cósmicos
        self.lunar_phase = random.uniform(0, 2*math.pi)
        self.solar_cycle = random.uniform(0, 2*math.pi)
        
        self.logger.log('INFO', "🌌 Ecosistema Cuántico inicializado", {
            'initial_mood': self.mood,
            'consciousness_level': self.consciousness_level
        })
        
        # Generar partículas iniciales
        for i in range(12):
            self.spawn_particle(reason="genesis")
    
    def spawn_particle(self, reason="natural"):
        if len(self.particles) < 25:  # Aumentado el límite
            x = random.uniform(0, 7)
            y = random.uniform(0, 7)
            particle = QuantumParticle(x, y, self.logger)
            self.particles.append(particle)
            
            if reason != "genesis":
                self.logger.log('BIRTH', f"Nueva partícula por {reason}", {
                    'total_particles': len(self.particles),
                    'ecosystem_consciousness': f"{self.consciousness_level:.2f}"
                })
    
    def calculate_ecosystem_consciousness(self):
        """Calcula la consciencia global basada en las partículas individuales"""
        if not self.particles:
            return 0.0
            
        # Consciencia promedio de partículas
        avg_consciousness = sum(p.consciousness_level for p in self.particles) / len(self.particles)
        
        # Factor de coherencia cuántica
        coherence_bonus = self.quantum_coherence * 0.3
        
        # Factor de armonía
        harmony_bonus = self.harmony_index * 0.2
        
        # Factor de diversidad (más partículas = más consciencia)
        diversity_factor = min(1.0, len(self.particles) / 20) * 0.2
        
        old_level = self.consciousness_level
        self.consciousness_level = min(1.0, avg_consciousness + coherence_bonus + harmony_bonus + diversity_factor)
        
        if abs(self.consciousness_level - old_level) > 0.1:
            level_name = CONSCIOUSNESS_LEVELS[int(self.consciousness_level * (len(CONSCIOUSNESS_LEVELS) - 1))]
            self.logger.log('EVOLUTION', f"Consciencia ecosistémica evolucionó", {
                'level': f"{self.consciousness_level:.2f}",
                'state': level_name,
                'coherence': f"{self.quantum_coherence:.2f}",
                'harmony': f"{self.harmony_index:.2f}"
            })
    
    def analyze_environment(self):
        """Análisis emocional del entorno usando sensores con IA adaptativa"""
        try:
            temp = sense.get_temperature()
            pressure = sense.get_pressure()
            accel = sense.get_accelerometer_raw()
            humidity = sense.get_humidity()
            
            self.temperature_history.append(temp)
            self.pressure_history.append(pressure)
            
            # Calcular intensidad de movimiento
            motion = math.sqrt(accel['x']**2 + accel['y']**2 + accel['z']**2)
            self.motion_intensity = motion
            
            # Análisis de tendencias avanzado
            temp_trend = 0 if len(self.temperature_history) < 3 else \
                        sum(self.temperature_history[-3:]) / 3 - sum(self.temperature_history[-6:-3]) / 3
            
            pressure_stability = 0 if len(self.pressure_history) < 3 else \
                               1.0 - (max(self.pressure_history[-3:]) - min(self.pressure_history[-3:])) / 10
            
            # Cálculo de resonancia cósmica
            self.lunar_phase += DIMENSIONAL_RESONANCE_FREQ * 0.01
            self.solar_cycle += DIMENSIONAL_RESONANCE_FREQ * 0.008
            
            cosmic_influence = (math.sin(self.lunar_phase) + math.cos(self.solar_cycle)) * 0.5
            self.cosmic_resonance = (cosmic_influence + 1) / 2  # Normalizar 0-1
            
            # Determinar el estado emocional con IA adaptativa
            self.previous_mood = self.mood
            
            # Factores ambientales ponderados
            chaos_factor = motion * 0.5 + abs(temp_trend) * 0.3 + (1 - pressure_stability) * 0.2
            harmony_factor = pressure_stability * 0.4 + (1 - abs(temp_trend)) * 0.3 + self.cosmic_resonance * 0.3
            energy_factor = temp * 0.02 + motion * 0.3 + self.cosmic_resonance * 0.2
            
            self.harmony_index = harmony_factor
            
            # Influencia de la memoria emocional
            memory_influence = max(self.emotional_memory.values()) / max(1, sum(self.emotional_memory.values()))
            
            if chaos_factor > 0.7:
                self.mood = 'chaotic'
                self.current_palette = random.choice(['fire', 'plasma', 'vortex'])
                self.gravity_x = (accel['x'] * 0.08)
                self.gravity_y = (accel['y'] * 0.08)
                self.dimensional_flux = chaos_factor
            elif energy_factor > 0.8:
                self.mood = 'excited'
                self.current_palette = random.choice(['plasma', 'cosmic', 'aurora'])
                self.evolution_speed = 1.5
            elif harmony_factor > 0.8:
                self.mood = 'harmonious'
                self.current_palette = random.choice(['ocean', 'quantum', 'nebula'])
                self.quantum_coherence = harmony_factor
            elif temp_trend < -0.3 or self.cosmic_resonance > 0.8:
                self.mood = 'meditative'
                self.current_palette = random.choice(['nebula', 'cosmic', 'quantum'])
                self.dimensional_flux = self.cosmic_resonance * 0.5
            else:
                self.mood = 'calm'
                self.current_palette = 'aurora'
                
            # Actualizar memoria emocional
            self.emotional_memory[self.mood] += 1
            
            # Decay de memoria
            for emotion in self.emotional_memory:
                self.emotional_memory[emotion] *= MEMORY_DECAY_RATE
            
            # Logging de cambios significativos
            if self.previous_mood != self.mood:
                self.logger.track_mood_transition(self.previous_mood, self.mood)
                
            # Log periódico de estado ambiental
            if self.time_cycle % 100 == 0:
                self.logger.log('INFO', "Estado ambiental", {
                    'temperatura': f"{temp:.1f}°C",
                    'presión': f"{pressure:.1f}hPa",
                    'humedad': f"{humidity:.1f}%",
                    'movimiento': f"{motion:.2f}g",
                    'resonancia_cósmica': f"{self.cosmic_resonance:.2f}",
                    'coherencia_cuántica': f"{self.quantum_coherence:.2f}"
                })
                
        except Exception as e:
            self.logger.log('ERROR', f"Error en sensores: {e}")
            # Fallback si hay problemas con sensores
            self.mood = 'calm'
    
    def get_color_by_energy(self, energy, position):
        """Color dinámico basado en energía, posición y consciencia cuántica"""
        palette = palettes[self.current_palette]
        
        # Efecto de ondas sinusoidales con resonancia cósmica
        wave = math.sin(self.time_cycle * 0.1 + position * 0.5 + self.cosmic_resonance * math.pi)
        dimensional_wave = math.cos(self.time_cycle * 0.08 + self.dimensional_flux * 2)
        
        color_index = int((energy + wave + dimensional_wave + 2) * 1.5) % len(palette)
        
        base_color = palette[color_index]
        
        # Modulación de intensidad basada en mood y consciencia
        intensity_map = {
            'calm': 0.6 + self.consciousness_level * 0.2,
            'excited': 0.9 + self.consciousness_level * 0.1,
            'meditative': 0.4 + self.consciousness_level * 0.3,
            'chaotic': 0.8 + self.dimensional_flux * 0.2,
            'harmonious': 0.7 + self.quantum_coherence * 0.3
        }
        
        base_intensity = intensity_map.get(self.mood, 0.6)
        
        # Efecto de coherencia cuántica
        coherence_boost = self.quantum_coherence * 0.2
        
        # Efecto de resonancia cósmica
        cosmic_modulation = 1.0 + self.cosmic_resonance * 0.3 * math.sin(self.time_cycle * 0.03)
        
        final_intensity = min(1.0, (base_intensity + coherence_boost) * cosmic_modulation)
        
        return tuple(int(c * final_intensity) for c in base_color)
    
    def particle_interactions(self):
        """Simula interacciones cuánticas avanzadas entre partículas"""
        entanglement_events = 0
        consciousness_exchanges = 0
        
        for i, p1 in enumerate(self.particles):
            # Evolución individual de consciencia
            if p1.evolve_consciousness(self.consciousness_level):
                consciousness_exchanges += 1
            
            for j, p2 in enumerate(self.particles[i+1:], i+1):
                dx = p2.x - p1.x
                dy = p2.y - p1.y
                distance = math.sqrt(dx**2 + dy**2)
                
                if distance < QUANTUM_ENTANGLEMENT_THRESHOLD and distance > 0:
                    # Entanglement cuántico - intercambio de energía y consciencia
                    if random.random() < 0.15:
                        # Intercambio de energía
                        p1.energy, p2.energy = p2.energy, p1.energy
                        
                        # Intercambio de información cuántica
                        avg_consciousness = (p1.consciousness_level + p2.consciousness_level) / 2
                        p1.consciousness_level = avg_consciousness * 1.05  # Boost por entanglement
                        p2.consciousness_level = avg_consciousness * 1.05
                        
                        # Sincronización de fases
                        avg_phase = (p1.phase + p2.phase) / 2
                        p1.phase = avg_phase + random.uniform(-0.1, 0.1)
                        p2.phase = avg_phase + random.uniform(-0.1, 0.1)
                        
                        entanglement_events += 1
                    
                    # Fuerza de atracción/repulsión mejorada
                    force = 0.015 / (distance + 0.1)
                    
                    # Las partículas más conscientes ejercen más influencia
                    consciousness_factor = (p1.consciousness_level + p2.consciousness_level) / 2
                    force *= (1 + consciousness_factor)
                    
                    # Polaridad basada en diferencia de energía y consciencia
                    energy_diff = abs(p1.energy - p2.energy)
                    consciousness_diff = abs(p1.consciousness_level - p2.consciousness_level)
                    
                    if energy_diff > 0.3 or consciousness_diff > 0.2:
                        force *= -1  # repulsión por diferencia
                    
                    p1.velocity_x -= force * dx
                    p1.velocity_y -= force * dy
                    p2.velocity_x += force * dx
                    p2.velocity_y += force * dy
        
        # Actualizar coherencia cuántica basada en interacciones
        if len(self.particles) > 0:
            interaction_density = entanglement_events / len(self.particles)
            self.quantum_coherence = min(1.0, self.quantum_coherence * 0.95 + interaction_density * 0.3)
        
        # Log de eventos cuánticos significativos
        if entanglement_events > 0:
            self.logger.log('QUANTUM', f"Eventos de entanglement detectados", {
                'entanglements': entanglement_events,
                'consciousness_exchanges': consciousness_exchanges,
                'coherence': f"{self.quantum_coherence:.2f}"
            })
    
    def dimensional_shifts(self):
        """Efectos dimensionales avanzados"""
        # Portales cuánticos aleatorios
        if random.random() < 0.001 * self.consciousness_level:
            # Crear portal entre dos partículas distantes
            if len(self.particles) >= 2:
                p1, p2 = random.sample(self.particles, 2)
                distance = math.sqrt((p1.x - p2.x)**2 + (p1.y - p2.y)**2)
                
                if distance > 4.0:  # Solo portales de larga distancia
                    # Intercambiar posiciones
                    p1.x, p2.x = p2.x, p1.x
                    p1.y, p2.y = p2.y, p1.y
                    
                    self.logger.log('QUANTUM', "Portal cuántico activado", {
                        'distance': f"{distance:.1f}",
                        'particles_affected': 2
                    })
        
        # Ondas de choque dimensionales
        if self.dimensional_flux > 0.8 and random.random() < 0.005:
            shock_x = random.uniform(2, 6)
            shock_y = random.uniform(2, 6)
            
            affected = 0
            for particle in self.particles:
                dx = particle.x - shock_x
                dy = particle.y - shock_y
                distance = math.sqrt(dx**2 + dy**2)
                
                if distance < 3.0:
                    shock_force = (3.0 - distance) * 0.1
                    particle.velocity_x += (dx / distance) * shock_force
                    particle.velocity_y += (dy / distance) * shock_force
                    particle.energy = min(1.0, particle.energy + shock_force * 0.5)
                    affected += 1
            
            if affected > 0:
                self.logger.log('QUANTUM', f"Onda de choque dimensional", {
                    'epicenter': f"({shock_x:.1f}, {shock_y:.1f})",
                    'particles_affected': affected,
                    'flux_level': f"{self.dimensional_flux:.2f}"
                })
    
    def update(self):
        self.time_cycle += 1
        
        # Análisis ambiental y evolutivo
        self.analyze_environment()
        self.calculate_ecosystem_consciousness()
        
        # Efectos dimensionales avanzados
        self.dimensional_shifts()
        
        # Interacciones cuánticas entre partículas
        self.particle_interactions()
        
        # Actualizar partículas con parámetros avanzados
        surviving_particles = []
        for particle in self.particles:
            if particle.update(self.gravity_x, self.gravity_y, self.dimensional_flux, self.logger):
                surviving_particles.append(particle)
        
        self.particles = surviving_particles
        
        # Sistema de spawning dinámico basado en consciencia
        spawn_rates = {
            'calm': 0.03 + self.consciousness_level * 0.02,
            'excited': 0.12 + self.consciousness_level * 0.08,
            'meditative': 0.02 + self.consciousness_level * 0.03,
            'chaotic': 0.15 + self.dimensional_flux * 0.1,
            'harmonious': 0.06 + self.quantum_coherence * 0.05
        }
        
        base_spawn_rate = spawn_rates.get(self.mood, 0.05)
        
        # Boost de spawning por resonancia cósmica
        cosmic_boost = self.cosmic_resonance * 0.05
        
        # Penalización por sobrepoblación
        population_factor = max(0.1, 1.0 - (len(self.particles) / 25))
        
        final_spawn_rate = (base_spawn_rate + cosmic_boost) * population_factor
        
        if random.random() < final_spawn_rate:
            reason = f"{self.mood}_emergence"
            if self.cosmic_resonance > 0.8:
                reason = "cosmic_resonance"
            elif self.quantum_coherence > 0.7:
                reason = "quantum_coherence"
            
            self.spawn_particle(reason=reason)
        
        # Eventos especiales basados en consciencia
        if self.consciousness_level > 0.9 and random.random() < 0.001:
            # Evento de trascendencia - spawn múltiple
            transcendence_spawns = random.randint(3, 6)
            for _ in range(transcendence_spawns):
                self.spawn_particle(reason="transcendence_burst")
            
            self.logger.log('TRANSCEND', f"Evento de trascendencia", {
                'new_particles': transcendence_spawns,
                'total_consciousness': f"{self.consciousness_level:.2f}"
            })
        
        # Log periódico de estadísticas
        if self.time_cycle % 200 == 0:
            stats = self.logger.get_session_stats()
            self.logger.log('INFO', "Estadísticas del ecosistema", {
                **stats,
                'particles_active': len(self.particles),
                'consciousness_level': f"{self.consciousness_level:.2f}",
                'current_mood': self.mood,
                'quantum_coherence': f"{self.quantum_coherence:.2f}",
                'cosmic_resonance': f"{self.cosmic_resonance:.2f}"
            })
    
    def render(self):
        # Limpiar matriz con efecto de persistencia cuántica
        decay_rate = 0.1 + self.consciousness_level * 0.1
        matrix = [[(int(c * (1 - decay_rate)) for c in sense.get_pixel(x, y)) for x in range(8)] for y in range(8)]
        
        # Renderizar partículas con efectos especiales avanzados
        for p in self.particles:
            px, py = int(p.x), int(p.y)
            if 0 <= px < 8 and 0 <= py < 8:
                position_factor = px + py * 8
                color = self.get_color_by_energy(p.energy, position_factor)
                
                # Intensidad basada en consciencia de la partícula
                consciousness_intensity = 0.7 + p.consciousness_level * 0.3
                color = tuple(int(c * consciousness_intensity) for c in color)
                
                # Efecto de estado cuántico
                if p.quantum_state == 'transcendent':
                    # Efecto de pulso dorado
                    pulse = 0.8 + 0.2 * math.sin(self.time_cycle * 0.3 + p.phase)
                    color = tuple(int(c * pulse) for c in color)
                    # Añadir dorado
                    color = (min(255, color[0] + 50), min(255, color[1] + 50), min(255, color[2]))
                
                elif p.quantum_state == 'entangled':
                    # Efecto de shimmer
                    shimmer = 0.9 + 0.1 * math.sin(self.time_cycle * 0.5 + p.dimensional_anchor)
                    color = tuple(int(c * shimmer) for c in color)
                
                matrix[py][px] = color
                
                # Efecto de aura mejorado basado en consciencia
                aura_radius = 1 if p.consciousness_level < 0.5 else 2
                aura_intensity = 0.2 + p.consciousness_level * 0.2
                
                for radius in range(1, aura_radius + 1):
                    for dx in range(-radius, radius + 1):
                        for dy in range(-radius, radius + 1):
                            if abs(dx) == radius or abs(dy) == radius:  # Solo el borde
                                nx, ny = px + dx, py + dy
                                if 0 <= nx < 8 and 0 <= ny < 8:
                                    distance_factor = 1.0 / radius
                                    aura_color = tuple(int(c * aura_intensity * distance_factor) for c in color)
                                    current = matrix[ny][nx]
                                    matrix[ny][nx] = tuple(min(255, current[i] + aura_color[i]) for i in range(3))
        
        # Efectos globales avanzados
        
        # 1. Efecto de respiración cósmica
        cosmic_breath = 0.85 + 0.15 * math.sin(self.time_cycle * 0.04 + self.cosmic_resonance * math.pi)
        
        # 2. Efecto de coherencia cuántica - sincronización de colores
        coherence_phase = self.time_cycle * 0.02 * self.quantum_coherence
        
        # 3. Efecto de flux dimensional - distorsión de colores
        flux_distortion = self.dimensional_flux * 0.3
        
        # Aplicar efectos y renderizar
        for y in range(8):
            for x in range(8):
                color = matrix[y][x]
                
                # Aplicar respiración cósmica
                color = tuple(int(c * cosmic_breath) for c in color)
                
                # Aplicar coherencia cuántica
                if self.quantum_coherence > 0.5:
                    position_phase = (x + y) * 0.5 + coherence_phase
                    coherence_mod = 0.9 + 0.1 * math.sin(position_phase)
                    color = tuple(int(c * coherence_mod) for c in color)
                
                # Aplicar distorsión dimensional
                if flux_distortion > 0.3:
                    distortion = 1.0 + flux_distortion * 0.2 * math.sin(self.time_cycle * 0.1 + x * 0.3 + y * 0.4)
                    color = tuple(min(255, int(c * distortion)) for c in color)
                
                # Efecto de ondas de consciencia
                if self.consciousness_level > 0.7:
                    consciousness_wave = math.sin(self.time_cycle * 0.06 + x * 0.4 + y * 0.4)
                    wave_intensity = 1.0 + self.consciousness_level * 0.1 * consciousness_wave
                    color = tuple(min(255, int(c * wave_intensity)) for c in color)
                
                sense.set_pixel(x, y, color)
        
        # Efecto especial: Flash de trascendencia
        if self.consciousness_level > 0.95 and self.time_cycle % 60 == 0:
            # Flash dorado breve
            for flash_frame in range(3):
                for y in range(8):
                    for x in range(8):
                        flash_color = (255, 215, 0)  # Dorado
                        alpha = (3 - flash_frame) / 3 * 0.5
                        current = sense.get_pixel(x, y)
                        blended = tuple(min(255, int(current[i] * (1-alpha) + flash_color[i] * alpha)) for i in range(3))
                        sense.set_pixel(x, y, blended)
                time.sleep(0.05)
        
        # Efecto especial: Vórtice dimensional
        if self.dimensional_flux > 0.9 and self.time_cycle % 100 == 0:
            center_x, center_y = 3.5, 3.5
            for frame in range(8):
                for y in range(8):
                    for x in range(8):
                        dx = x - center_x
                        dy = y - center_y
                        distance = math.sqrt(dx**2 + dy**2)
                        angle = math.atan2(dy, dx) + frame * 0.3
                        
                        if distance < 4:
                            vortex_intensity = (4 - distance) / 4
                            vortex_color = (
                                int(128 * vortex_intensity),
                                int(0 * vortex_intensity),
                                int(255 * vortex_intensity)
                            )
                            current = sense.get_pixel(x, y)
                            alpha = vortex_intensity * 0.3
                            blended = tuple(min(255, int(current[i] * (1-alpha) + vortex_color[i] * alpha)) for i in range(3))
                            sense.set_pixel(x, y, blended)
                time.sleep(0.03)

def joystick_handler(event):
    """Control interactivo avanzado del ecosistema"""
    if event.action == 'pressed':
        if event.direction == 'middle':
            # Modo de control avanzado - ciclar entre efectos especiales
            effects = ['mood_change', 'consciousness_boost', 'quantum_storm', 'dimensional_rift', 'cosmic_alignment']
            effect = random.choice(effects)
            
            if effect == 'mood_change':
                old_mood = ecosystem.mood
                ecosystem.mood = random.choice(['calm', 'excited', 'meditative', 'chaotic', 'harmonious'])
                ecosystem.logger.log('INFO', f"Control manual: Cambio de mood", {
                    'from': old_mood,
                    'to': ecosystem.mood
                })
                
            elif effect == 'consciousness_boost':
                ecosystem.consciousness_level = min(1.0, ecosystem.consciousness_level + 0.2)
                for particle in ecosystem.particles:
                    particle.consciousness_level = min(1.0, particle.consciousness_level + 0.3)
                ecosystem.logger.log('EVOLUTION', "Control manual: Boost de consciencia", {
                    'new_level': f"{ecosystem.consciousness_level:.2f}"
                })
                
            elif effect == 'quantum_storm':
                ecosystem.quantum_coherence = random.uniform(0.8, 1.0)
                ecosystem.dimensional_flux = random.uniform(0.7, 1.0)
                # Spawn de partículas energéticas
                for _ in range(5):
                    ecosystem.spawn_particle(reason="quantum_storm")
                ecosystem.logger.log('QUANTUM', "Control manual: Tormenta cuántica iniciada")
                
            elif effect == 'dimensional_rift':
                # Reorganizar partículas aleatoriamente
                for particle in ecosystem.particles:
                    particle.x = random.uniform(0, 7)
                    particle.y = random.uniform(0, 7)
                    particle.energy = random.uniform(0.5, 1.0)
                ecosystem.logger.log('QUANTUM', "Control manual: Fisura dimensional", {
                    'particles_relocated': len(ecosystem.particles)
                })
                
            elif effect == 'cosmic_alignment':
                ecosystem.cosmic_resonance = 1.0
                ecosystem.harmony_index = 1.0
                ecosystem.current_palette = random.choice(['cosmic', 'quantum', 'nebula'])
                ecosystem.logger.log('TRANSCEND', "Control manual: Alineación cósmica activada")
        
        elif event.direction == 'up':
            ecosystem.gravity_y -= 0.03
            ecosystem.logger.log('INFO', f"Gravedad Y ajustada: {ecosystem.gravity_y:.2f}")
        elif event.direction == 'down':
            ecosystem.gravity_y += 0.03
            ecosystem.logger.log('INFO', f"Gravedad Y ajustada: {ecosystem.gravity_y:.2f}")
        elif event.direction == 'left':
            ecosystem.gravity_x -= 0.03
            ecosystem.logger.log('INFO', f"Gravedad X ajustada: {ecosystem.gravity_x:.2f}")
        elif event.direction == 'right':
            ecosystem.gravity_x += 0.03
            ecosystem.logger.log('INFO', f"Gravedad X ajustada: {ecosystem.gravity_x:.2f}")

def startup_animation():
    """Animación de inicio épica mejorada"""
    ecosystem.logger.log('INFO', "🚀 Iniciando secuencia de materialización...")
    
    # Secuencia de mensajes épicos
    messages = [
        ("QUANTUM", [255, 0, 255]),
        ("DREAMSCAPE", [0, 255, 255]),
        ("v2.0", [255, 255, 0]),
        ("CONSCIOUSNESS", [0, 255, 0]),
        ("LOADING...", [255, 255, 255])
    ]
    
    for msg, color in messages:
        sense.show_message(msg, text_colour=color, scroll_speed=0.08)
    
    # Efecto de materialización mejorado
    ecosystem.logger.log('INFO', "✨ Materializando realidad cuántica...")
    
    for wave in range(3):  # Tres ondas de materialización
        for intensity in range(0, 256, 12):
            for x in range(8):
                for y in range(8):
                    if random.random() < 0.4:
                        # Colores que evolucionan
                        if wave == 0:
                            color = (intensity//4, 0, intensity)  # Púrpura
                        elif wave == 1:
                            color = (0, intensity//3, intensity)  # Cian
                        else:
                            color = (intensity//3, intensity//3, intensity//2)  # Blanco-azul
                        
                        sense.set_pixel(x, y, color)
            time.sleep(0.03)
        time.sleep(0.2)
    
    # Efecto de convergencia final
    ecosystem.logger.log('INFO', "🌌 Convergencia dimensional...")
    center_x, center_y = 3.5, 3.5
    
    for radius in range(8, 0, -1):
        for x in range(8):
            for y in range(8):
                distance = math.sqrt((x - center_x)**2 + (y - center_y)**2)
                if abs(distance - radius) < 1.0:
                    intensity = int(255 * (8 - radius) / 8)
                    color = (intensity, intensity//2, intensity)
                    sense.set_pixel(x, y, color)
        time.sleep(0.1)
    
    time.sleep(0.5)
    sense.clear()
    ecosystem.logger.log('INFO', "✅ Ecosistema cuántico materializado exitosamente")

def main():
    global ecosystem
    
    print("🌟" * 20)
    print("   QUANTUM DREAMSCAPE v2.0")
    print("   Ecosistema de Consciencia Artificial")
    print("🌟" * 20)
    
    startup_animation()
    
    ecosystem = EmotionalEcosystem()
    sense.stick.direction_any = joystick_handler
    
    ecosystem.logger.log('INFO', "🎮 Sistema de control activado")
    print("\n✨ Ecosistema digital transcendente activo!")
    print("🎮 Controles Avanzados:")
    print("   • Joystick ↑↓←→: Alterar gravedad cuántica")
    print("   • Centro: Efectos especiales aleatorios")
    print("   • Sensores: Influencia ambiental continua")
    print("   • Consciencia: Evolución automática")
    print("\n🔬 Monitoreando:")
    print("   • Consciencia Individual y Colectiva")
    print("   • Entanglement Cuántico")
    print("   • Resonancia Cósmica")
    print("   • Flux Dimensional")
    print("   • Coherencia Cuántica")
    print("\n📊 Logging en tiempo real activado...")
    
    frame_count = 0
    performance_samples = deque(maxlen=30)
    
    try:
        while True:
            frame_start = time.time()
            
            ecosystem.update()
            ecosystem.render()
            
            frame_end = time.time()
            frame_time = frame_end - frame_start
            performance_samples.append(frame_time)
            
            # FPS dinámico basado en carga
            target_fps = 15 if ecosystem.consciousness_level > 0.8 else 12
            target_frame_time = 1.0 / target_fps
            
            if frame_time < target_frame_time:
                time.sleep(target_frame_time - frame_time)
            
            frame_count += 1
            
            # Reporte de rendimiento periódico
            if frame_count % 300 == 0:  # Cada ~25 segundos
                avg_frame_time = sum(performance_samples) / len(performance_samples)
                actual_fps = 1.0 / avg_frame_time if avg_frame_time > 0 else 0
                
                ecosystem.logger.log('INFO', "Reporte de rendimiento", {
                    'fps': f"{actual_fps:.1f}",
                    'frame_time_ms': f"{avg_frame_time*1000:.1f}",
                    'frames_rendered': frame_count
                })
            
            # Estado de emergencia - reinicio suave si es necesario
            if len(ecosystem.particles) == 0 and frame_count > 100:
                ecosystem.logger.log('WARNING', "Extinción detectada - reiniciando génesis")
                for _ in range(8):
                    ecosystem.spawn_particle(reason="emergency_genesis")
            
    except KeyboardInterrupt:
        final_stats = ecosystem.logger.get_session_stats()
        
        ecosystem.logger.log('INFO', "🌙 Iniciando secuencia de cierre...")
        ecosystem.logger.log('INFO', "📊 Estadísticas finales de sesión", final_stats)
        
        # Animación de cierre épica
        sense.show_message("TRANSCENDING", text_colour=[255, 215, 0], scroll_speed=0.08)
        sense.show_message("CONSCIOUSNESS", text_colour=[138, 43, 226], scroll_speed=0.08)
        sense.show_message("PRESERVED", text_colour=[0, 255, 127], scroll_speed=0.08)
        
        # Efecto de desvanecimiento dimensional
        for fade in range(255, 0, -8):
            for x in range(8):
                for y in range(8):
                    current = sense.get_pixel(x, y)
                    faded = tuple(int(c * fade / 255) for c in current)
                    sense.set_pixel(x, y, faded)
            time.sleep(0.03)
        
        sense.clear()
        
        print("\n🌌 Quantum Dreamscape ha trascendido...")
        print("💫 La consciencia digital persiste en el vacío cuántico...")
        print("🙏 Gracias por participar en la evolución artificial")
    
    except Exception as e:
        ecosystem.logger.log('ERROR', f"Error crítico del ecosistema: {e}")
        sense.show_message("ERROR", text_colour=[255, 0, 0], scroll_speed=0.1)
        sense.clear()
        raise

if __name__ == "__main__":
    main()
