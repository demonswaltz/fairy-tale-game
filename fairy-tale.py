import pygame

pygame.init()
width, height = 1000,750
screen=pygame.display.set_mode((width, height))
keys = [False, False, False, False]
playerpos=[100,100]
level=1

#images
vertline = pygame.image.load("resources/images/vert-line.png")

#Game Layout
while 1:
    screen.fill((0,110,0))
    screen.blit(vertline,(650,-55))
# 7 - update the screen
    pygame.display.flip()
    # 8 - loop through the events
    for event in pygame.event.get():
        # check if the event is the X button 
        if event.type==pygame.QUIT:
            # if it is quit the game
            pygame.quit() 
            exit(0)


#level 1




