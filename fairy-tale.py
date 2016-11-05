import pygame
from pygame.locals import *

pygame.init()
width, height = 1000,750
screen=pygame.display.set_mode((width, height))
puzzleArea=pygame.Surface((700, 500))
keys = [False, False, False, False]
playerpos=[100,100]
level=1

#images
vertline = pygame.image.load("resources/images/vert-line.png")
grass = pygame.image.load("resources/images/grass1.png")

#Game Layout function
def gameSetup():
    screen.fill((245,222,179))
    #puzzleArea.blit(screen, (0,0))
    screen.blit(vertline,(710,-55))
    

#level 1
    while True: 
        for x in range(width/grass.get_width()+1):
                for y in range(height/grass.get_height()+1):
                    puzzleArea.blit(grass,(x*125,y*200))
		gameSetup()
# 7 - update the screen
    pygame.display.flip()
# 8 - loop through the events
    for event in pygame.event.get():
        # check if the event is the X button 
        if event.type==pygame.QUIT:
            # if it is quit the game
            pygame.quit() 
            exit(0)


