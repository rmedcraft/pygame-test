import pygame

PLAYER_SIZE = 40
GROUND_HEIGHT = 100
JUMP_POWER = 400

def main():
    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    clock = pygame.time.Clock()
    running = True
    dt = 0
    jumpVelocity = 0
    jumping = False
    
    playerY = screen.get_height() - GROUND_HEIGHT - PLAYER_SIZE
    while running:
        for event in pygame.event.get():
            if(event.type == pygame.QUIT):
                running = False
        
        # GAME GOES HERE
        screen.fill("blue")
        ground = pygame.draw.rect(screen, "green", pygame.Rect(0, screen.get_height() - GROUND_HEIGHT, screen.get_width(), GROUND_HEIGHT))
        player = pygame.draw.rect(screen, "brown", pygame.Rect(200, playerY, PLAYER_SIZE, PLAYER_SIZE))

        keys = pygame.key.get_pressed()
        if(keys[pygame.K_SPACE] and playerY == ground.top - PLAYER_SIZE):
            jumping = True
            jumpVelocity = JUMP_POWER
            
        if(jumping):
            playerY -= jumpVelocity * dt
            jumpVelocity -= 10 # arbitrary value for gravity
            if(playerY > ground.top - PLAYER_SIZE):
                playerY = ground.top - PLAYER_SIZE
                jumpVelocity = 0
                jumping = False
        # GAME STOPS HERE
        
        # flip() the display to put your work on screen
        pygame.display.flip()

        # limits FPS to 60
        # dt is delta time in seconds since last frame, used for framerate-independent physics.
        dt = clock.tick(60) / 1000
    
    pygame.quit()
    
    
    
    
if(__name__ == "__main__"):
    main()