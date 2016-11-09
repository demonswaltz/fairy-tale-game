import pygame
from pygame.locals import *

#Supposedly Global Variables
pygame.init()
width, height = 1000,750
screen=pygame.display.set_mode((width, height))
puzzleArea=pygame.Surface((700, 500))
keys = [False, False, False, False]
playerpos=[100,100]
level=2
index = 0


#images
vertline = pygame.image.load("resources/images/vert-line.png")
grass = pygame.image.load("resources/images/grass1.png")
shark = pygame.image.load("resources/images/shark_1.png")
up = "resources/images/up.png"
down = "resources/images/down.png"
left = "resources/images/left.png"
right = "resources/images/right.png"

#Game Layout Function
def gameSetup(str):
	pygame.display.set_caption(str)
	screen.fill((245,222,179))
	screen.blit(puzzleArea, (0,0))
	screen.blit(vertline,(710,-55))
	pygame.display.flip()
#Basic Game Mechanics
def gamePlay():
	global index 
	moves= [];
	moveImg=[]; 
	arrowPosy=[16, 66, 116, 166, 216, 266, 316, 366, 416, 466, 516, 566, 616, 666];
	spaceBar=False
	arrowBlitPosx= 750
	while index <= 14:
		print index
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					moves.append("up")
					moveImg.append(up)
					index += 1
				elif event.key == pygame.K_DOWN:
					moves.append("down")
					moveImg.append(down)
					index += 1
				elif event.key == pygame.K_LEFT:
					moves.append("left")
					moveImg.append(left)
					index += 1
				elif event.key == pygame.K_RIGHT:
					moves.append("right")
					moveImg.append(right)
					index += 1
				elif event.key == pygame.K_BACKSPACE:
					moves.pop()
					moveImg.pop()
					index-= 1
				elif event.key == pygame.K_SPACE:
					spaceBar = True
				
		
	else:
		print moves
		print moveImg
	
#for move in moveImg:
		#	arrowPic=[];
		#	arrowPic.append(pygame.image.load(move))
		#	print arrowPic
		#	for AP in arrowPic:
		#		screen.blit(AP, (arrowBlitPosx,arrowPosy[len(moves)-1]))
		#		pygame.display.flip()
		

			

#level 1
if level == 1 and index <= 14: 
	for x in range(width/grass.get_width()+1):
		for y in range(height/grass.get_height()+1):
			puzzleArea.blit(grass,(x*125,y*200))
	gameSetup("LEVEL 1")
	gamePlay()

#level 2
elif level == 2 and index <= 14:
	for x in range(width/grass.get_width()+1):
		for y in range(height/grass.get_height()+1):
			puzzleArea.blit(shark,(x*125,y*200))
	gameSetup("LEVEL 2")
	gamePlay()
# 7 - update the screen
	
# 8 - loop through the events
for event in pygame.event.get():
		# check if the event is the X button 
	if event.type==pygame.QUIT:
		# if it is quit the game
		pygame.quit() 
		exit(0)


