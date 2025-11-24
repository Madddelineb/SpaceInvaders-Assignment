import pygame
pygame.init()
#
screen = pygame.display.set_mode([500,500])

player_x = 250

running = True
while running: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                print("Left arrow key pressed")
                player_x -= 5
            elif event.key == pygame.K_RIGHT:
                print("Left arrow key pressed")
                player_x += 5
    
    screen.fill([0,0,0]) # black background

    player_img = pygame.image.load("defender_player.png")
    screen.blit(player_img, (player_x, 250))
    
    pygame.draw.circle(screen,(0,255,0), [player_x, 250], 75) ## (0, 255, 0) = green
    
    pygame.display.flip()
    
pygame.quit()
