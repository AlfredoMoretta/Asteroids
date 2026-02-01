import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state
from player import Player



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
    
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        updatable.update(dt)        
        
        screen.fill("black")

         # ← DRAW TUTTI gli oggetti disegnabili
        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()
        # Limita a 60 FPS e calcola delta time
        dt = clock.tick(60) / 1000  # ms → secondi
        
if __name__ == "__main__":
    main()
