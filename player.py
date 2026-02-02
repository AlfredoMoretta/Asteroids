import pygame
from circleshape import CircleShape
from constants import (PLAYER_RADIUS, LINE_WIDTH, PLAYER_TURN_SPEED, PLAYER_SHOOT_SPEED, 
                       SHOT_RADIUS,PLAYER_SHOOT_COOLDOWN_SECONDS)
from shot import Shot 


class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shoot_timer = 0.0 
    
    def move(self, dt):
        unit_vector = pygame.Vector2(0, 1)
        rotated_vector = unit_vector.rotate(self.rotation)
        rotated_with_speed_vector = rotated_vector * PLAYER_TURN_SPEED * dt
        self.position += rotated_with_speed_vector


    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def shoot(self):
        if self.shoot_timer > 0:
            return
        shot = Shot(self.position.x, self.position.y, SHOT_RADIUS)
        direction = pygame.Vector2(0, 1).rotate(self.rotation)
        shot.velocity = direction * PLAYER_SHOOT_SPEED

        self.shoot_timer = PLAYER_SHOOT_COOLDOWN_SECONDS

    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), LINE_WIDTH)
    
    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt
    
    def update(self, dt):  # ← COMPLETATO
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:  # A = SINISTRA
            self.rotate(-dt)  # ← dt NEGATIVO = rotazione inversa
        if keys[pygame.K_d]:  # D = DESTRA
            self.rotate(dt)   # ← dt POSITIVO = rotazione normale
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:  
            self.shoot()

        self.shoot_timer = max(0, self.shoot_timer - dt)