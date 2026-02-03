import pygame
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from circleshape import CircleShape
from logger import log_event
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(
            screen, 
            "white", 
            self.position,  # centro del cerchio
            self.radius, 
            LINE_WIDTH
        )
    
    def update(self, dt):
        self.position += self.velocity * dt  # movimento lineare
    
    def split(self):  # ← NUOVO
        self.kill()  # sempre distruggi se stesso
        
        if self.radius <= ASTEROID_MIN_RADIUS:
            return  # asteroide piccolo = fine
    
        log_event("asteroid_split")
        
        angle = random.uniform(20, 50)  # gradi casuali 20-50
        
        # Primo nuovo asteroide
        new_velocity1 = self.velocity.rotate(angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        
        asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid1.velocity = new_velocity1 * 1.2
        
        # Secondo nuovo asteroide (direzione opposta)
        new_velocity2 = self.velocity.rotate(-angle)
        asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid2.velocity = new_velocity2 * 1.2