import pygame

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
PLAYER_SIZE = 40
GROUND_HEIGHT = 100
PLAYER_STARTYPOS = SCREEN_HEIGHT - GROUND_HEIGHT - PLAYER_SIZE
JUMP_POWER = 400
MOVE_SPEED = 250
OBSTACLE_START = SCREEN_WIDTH + 100 # leftmost position of the obstacle when it starts

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    running = True
    dt = 0
    jumpVelocity = 0
    jumping = False
    
    playerY = PLAYER_STARTYPOS
    
    obstacleLeft = OBSTACLE_START
    obstacleRight = OBSTACLE_START + 50    
    # obstacleLeft = 100
    # obstacleRight = 150
    
    while running:
        for event in pygame.event.get():
            if(event.type == pygame.QUIT):
                running = False
        
        # GAME GOES HERE
        screen.fill("blue")
        ground = pygame.draw.rect(screen, "green", pygame.Rect(0, SCREEN_HEIGHT - GROUND_HEIGHT, SCREEN_WIDTH, GROUND_HEIGHT))
        player = pygame.draw.rect(screen, "brown", pygame.Rect(200, playerY, PLAYER_SIZE, PLAYER_SIZE))

        keys = pygame.key.get_pressed()
        if((keys[pygame.K_SPACE] or keys[pygame.K_UP] or keys[pygame.K_w]) and playerY == ground.top - PLAYER_SIZE):
            jumping = True
            jumpVelocity = JUMP_POWER
            
        if(jumping):
            playerY -= jumpVelocity * dt
            jumpVelocity -= 10 # arbitrary value for gravity
            
            # if the player is on the ground
            if(playerY > ground.top - PLAYER_SIZE):
                playerY = ground.top - PLAYER_SIZE
                jumpVelocity = 0
                jumping = False
                
        # generate obstacles 
        obstacleTop = ground.top - 50
        
        
        obstacle = pygame.draw.polygon(screen, "black", [[obstacleLeft, ground.top], [obstacleRight, ground.top], [(obstacleRight + obstacleLeft) / 2, obstacleTop]])
        obstacleLeft -= MOVE_SPEED * dt
        obstacleRight = obstacleLeft + 50
        
        if(obstacleRight < 0):
            obstacleLeft = OBSTACLE_START
            obstacleRight = obstacleLeft + 50
        # GAME STOPS HERE
        
        # flip() the display to put your work on screen
        pygame.display.flip()

        # limits FPS to 60
        # dt is delta time in seconds since last frame, used for framerate-independent physics.
        dt = clock.tick(60) / 1000
    
    pygame.quit()
    
    
    
    
if(__name__ == "__main__"):
    main()