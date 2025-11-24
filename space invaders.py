#testttt
import pygame
import sys
import numpy as np
pygame.init()
#


SCREEN_HEIGHT = 500
SCREEN_WIDTH = 500

screen = pygame.display.set_mode([SCREEN_HEIGHT, SCREEN_WIDTH])
clock = pygame.time.Clock() # to slow down the speed of movement
FPS = 30 # to slow down the speed of movement

player_img = pygame.image.load(r"C:\Users\22513062\OneDrive - Buckinghamshire New University\defender.png") #load in the image
player_img = pygame.transform.scale(player_img, (35, 30)) # change the scale

invader_img = pygame.image.load(r"C:\Users\22513062\OneDrive - Buckinghamshire New University\invader1.png")
invader_img = pygame.transform.scale(invader_img, (30, 30))


invader_startrow = 100
invader_endrow = 300
invader_startcol = 100
invader_endcol = 400 

#boolean for direction
move_right = True
edge_hit = False

bullet_x = 250
bullet_y = 500

player_x = 250
player_y = 10




def draw_invaders():
    for row in range(invader_startrow, invader_endrow, 30): # intervals of 30 
        for col in range(invader_startcol, invader_endcol, 30):
            screen.blit(invader_img, (col, row))

def move_invaders():
    global invader_startcol, invader_endcol, invader_startrow, invader_endrow, move_right
    # start moving right 
    if move_right == True:
        invader_startcol += 1
        invader_endcol += 1
        edge_hit = False
    else: # otherwise move left
        invader_startcol -= 1
        invader_endcol -= 1
        edge_hit = False
    
    # detect edge of screen
    if invader_endcol > SCREEN_WIDTH or invader_startcol < 0:
        edge_hit = True
        invader_startrow += 20
        invader_endrow += 20
    
    # immediately reset edge_hit to prevent getting stuck! 
    if edge_hit == True:
        edge_hit == False
        if move_right == True:
            move_right = False
        else:
            move_right = True


running = True
while running: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.display.quit()
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_x -= 5
            elif event.key == pygame.K_RIGHT:
                player_x += 5
            elif event.key == pygame.K_ESCAPE or event.key == pygame.WINDOWCLOSE: # TO QUIT
                running = False
                #pygame.display.quit()
                #pygame.QUIT()
                #sys.exit()
    
    screen.fill([0,0,0]) # black background
    
    move_invaders()
    
    draw_invaders()
     
    screen.blit(player_img, (player_x, 450)) # draw player
    
    pygame.display.flip()
    
    clock.tick(FPS)
    
#pygame.display.quit()
#pygame.quit()
sys.exit(0)
