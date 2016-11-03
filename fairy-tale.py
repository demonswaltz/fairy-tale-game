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
    screen.fill(1000)
    screen.blit(vertline,(500,1000))



#level 1




