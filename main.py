import pygame
from asteroid import Asteroid
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state, log_event
from player import Player
from asteroidfield import AsteroidField 
import sys
from shot import Shot 


def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
 # ← NUOVI GRUPPI
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    
    # ← Player si aggiunge AUTOMATICAMENTE ai gruppi
    Player.containers = (updatable, drawable)
    
    # Crea player (si aggiunge ai gruppi automaticamente)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
     # ← NUOVO: Asteroids group
    asteroids = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)
    
    # ← NUOVO: AsteroidField
    AsteroidField.containers = (updatable,)  # solo updatable!
    asteroidfield = AsteroidField()

    shots = pygame.sprite.Group()  # ← NUOVO
    Shot.containers = (shots, updatable, drawable)  # ← NUOVO

    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        updatable.update(dt)        
        
        for asteroid in asteroids:
            if player.collides_with(asteroid):
                log_event("player_hit")
                print("Game over!")
                sys.exit()
        screen.fill("black")

         # ← DRAW TUTTI gli oggetti disegnabili
        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()
        # Limita a 60 FPS e calcola delta time
        dt = clock.tick(60) / 1000  # ms → secondi
        
if __name__ == "__main__":
    main()
