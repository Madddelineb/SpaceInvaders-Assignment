#IMPORTING LIBRARIES
import pygame 
import numpy as np
import time

pygame.init()

SCREEN_HEIGHT = 500
SCREEN_WIDTH = 500


#SET SCREEN SIZE
screen = pygame.display.set_mode([500,500])

#STARTING POSITION OF PLAYER
x = 220
y = 430

#STARTING STATES OF PLAYER BULLETS
fired = False  
fired2 = False

#STARTING LOCATIONS OF PLAYER BULLETS
bullety = 398
bulletx = 0
bullety2 = 398
bulletx2 = 0

#STARTING STATES OF DEATH VARIABLES
alienplayercollision = False
lives = 3

#Invader rows
invader_startrow = 100
invader_endrow = 300
invader_startcol = 100
invader_endcol = 400 

#LOAD AND SCALE BULLET SPRITE
bullet_img = pygame.image.load("spacegame\_bullet.png")
bullet_img = pygame.transform.scale(bullet_img, (3, 33)) 

#LOAD DEATH SPRITE
deathscreen = pygame.image.load("spacegame\_deathscreen.png")

#LOAD AND SCALE PLAYER SPRITE
player_img = pygame.image.load("spacegame\defender.png") 
player_img = pygame.transform.scale(player_img, (44, 32))

#LOAD AND SCALE LIVES SPRITES
threelives = pygame.image.load("spacegame\_3lives.png")
threelives = pygame.transform.scale(threelives, (110, 30)) 

twolives = pygame.image.load("spacegame\_2lives.png")
twolives = pygame.transform.scale(twolives, (110, 30)) 

onelives = pygame.image.load("spacegame\_1lives.png")
onelives = pygame.transform.scale(onelives, (110, 30)) 

zerolives = pygame.image.load("spacegame\_0lives.png")
zerolives = pygame.transform.scale(zerolives, (110, 30)) 


invader_img = pygame.image.load("spacegame\_invader1.png")
invader_img = pygame.transform.scale(invader_img, (30, 30))



#boolean for direction
move_right = True
edge_hit = False


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


#START MAIN GAME LOOP, EACH RUN OF THIS LOOP IS A FRAME OF THE GAME
running = True
while running:

    #FILL THE WINDOW WITH A BLACK BACKGROUND
    #THIS IS DONE AT THE START OF THE GAME LOOP TO ENSURE EVERYTHING WE WANT TO SHOW ON THE SCREEN IS DRAWN ON TOP OF THE BACKGROUND
    screen.fill([0,0,0])

    move_invaders()
    
    draw_invaders()

    #LIFE CHECKER
    #THIS PART CHECKS THE AMOUNT OF LIVES THE PLAYER HAS EVERY FRAME AND UPDATES THE LIVES ICONS TO MATCH THEIR AMOUNT OF LIVES
    if lives == 3: 
            screen.blit(threelives, (5, 5))
    elif lives == 2:
            screen.blit(twolives, (5, 5))
    elif lives == 1:
            screen.blit(onelives, (5, 5))
    elif lives == 0:
            screen.blit(zerolives, (5, 5))
            #EXITS THE MAIN GAME LOOP
            break


    #HANDLING FOR ALL EVENTS
    for event in pygame.event.get():

        #WINDOW CLOSING FUNCTIONALITY
        if event.type == pygame.QUIT:
            running = False

        #HANDLING OF ALL KEYPRESS EVENTS
        elif event.type == pygame.KEYDOWN:

            #LEFT ARROW KEY DETECTOR
            if event.key == pygame.K_LEFT:
                print("Left arrow key pressed")
                #MOVING THE PLAYER LEFT IF THEY ARE WITHIN BOUNDS
                if x > 10:
                    print(x)
                    x += -10

            #RIGHT ARROW KEY DETECTOR
            if event.key == pygame.K_RIGHT:
                print("Right arrow key pressed")
                #MOVING THE PLAYER RIGHT IF THEY ARE WITHIN BOUNDS
                if x < 450:
                    print(x)
                    x += 10

            #J KEY DETECTOR
            if event.key == pygame.K_j:
                print("J pressed")
                #TRIGGERING PLAYER DAMAGE IF J IS PRESSED
                alienplayercollision = True
            
            #SPACE KEY DETECTOR
            if event.key == pygame.K_SPACE and fired == False:
                print("Space key pressed")
                #DRAWING BULLET IF SPACE IS PRESSED AND BULLET IS UNFIRED
                screen.blit(bullet_img, (bulletx, bullety))
                fired = True
                bulletx = x + 20
            elif event.key == pygame.K_SPACE and fired == True and fired2 == False:
                print("Space key pressed")
                #DRAWING BULLET 2 IF SPACE IS PRESSED AND BULLET 1 IS FIRED AND BULLET 2 IS UNFIRED
                screen.blit(bullet_img, (bulletx2, bullety2))
                fired2 = True
                bulletx2 = x + 20

    #BULLET TRAVELING LOGIC
    if fired == True:
        #DRAWING BULLET
        screen.blit(bullet_img, (bulletx, bullety))
        #UPDATING BULLET POSITION
        bullety -= 10
        print (bullety)
        #RESETING BULLET IF ITS OUT OF BOUNDS
        if bullety < -50:
            fired = False
            bullety = 398
    
    #EXACT SAME THING BUT WITH SECOND BULLET
    if fired2 == True:
        screen.blit(bullet_img, (bulletx2, bullety2))
        bullety2 -= 10
        print (bullety2)
        if bullety2 < -50:
            fired2 = False
            bullety2 = 398
    

    #DRAWING PLAYER SPRITE
    screen.blit(player_img, (x, y)) 
    

    #DEATH FUNCTION
    #IF THE VARIABLE IS TRUE, LIVES ARE DECREASED BY 1, THE PLAYER IS RESET TO THE MIDDLE OF THE SCREEN AND THE VARIABLE IS SET BACK TO FALSE
    if alienplayercollision == True:
        alienplayercollision = False
        x = 220
        y = 430
        lives -= 1

    # COLLISIONS - Due to circumstances we never finished the alien's functionality, and so theres nothing for the player to collide with and take damage from and therefore this part of code is unused in the final product but exists as a simple way to enable collision if the aliens were programmed
    # 
    #bulletrect = pygame.Rect(bulletx, bullety, 3, 33)
    #invaderrect = pygame.Rect(invaderx, invadery, invaderxsize, invaderysize)
    #if bulletrect.colliderect(invaderrect):
    #   Code for aliens dying here
    #
    #alienbulletrect = pygame.Rect(alienbulletx, alienbullety, alienbulletxsize, alienbulletysize)
    #playerrect = pygame.Rect(x, y, 44, 32)
    #if alienbulletrect.colliderect(playerrect):
    #   alienplayercollision = True


    #UPDATES SCREEN
    #VERY VERY VERY IMPORTANT THAT THIS IS THE LAST THING IN THE GAME LOOP
    pygame.display.flip()
    #KEEPS THE GAME AT A REASONABLE FRAMERATE
    time.sleep(0.032)

#PUTS DEATHSCREEN ON THE SCREEN
screen.blit(deathscreen, (0, 0))
#UPDATES THE SCREEN
pygame.display.flip()
#WAITS 1 SECOND
time.sleep(1)

#CLOSES THE WINDOW
pygame.quit()
pygame.display.quit()

