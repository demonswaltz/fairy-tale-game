import pygame
from pygame.locals import *

#Supposedly Global Variables
pygame.init()
width, height = 1000,750
screen=pygame.display.set_mode((width, height))
puzzleArea=pygame.Surface((700, 500))
keys = [False, False, False, False]
arrowPosy=[];
playerpos=[100,100]
level=2
index = 0
moves= [];
moveImg=[];
count = 0

#images
vertline = pygame.image.load("resources/images/vert-line.png")
grass = pygame.image.load("resources/images/grass1.png")
shark = pygame.image.load("resources/images/shark_1.png")
up = "resources/images/up.png"
down = "resources/images/down.png"
left = "resources/images/left.png"
right = "resources/images/right.png"

#Game Layout Function
def gameSetup():
		global level
		str(level)
		pygame.display.set_caption("LEVEL ")
		screen.fill((245,222,179))
		screen.blit(puzzleArea, (0,0))
		screen.blit(vertline,(710,-55))
		pygame.display.flip()
#Draw Moves Function
def drawMoves():
	global arrowPosy
	global moveImg
	global moves
	imageLoad=[]
	if len(moves) > 0:
		for pos,image in zip(arrowPosy,moveImg):
			pygame.time.wait(10)
			screen.blit(pygame.image.load(image), (750, pos))
			pygame.display.flip()
	else:
		gameSetup()
			
#Basic Game Mechanics
def gamePlay():
	global arrowPosy
	global index 
	global moves
	posy=16
	spaceBar=False
	while spaceBar == False and index < 14:
		print arrowPosy
		print moveImg
		drawMoves()
		for event in pygame.event.get():
			try:
				if event.type == pygame.KEYDOWN:
					gameSetup()
					drawMoves()
					if event.key == pygame.K_UP:
						moves.append(pygame.K_UP)
						moveImg.append(up)
						arrowPosy.append(posy)
						posy += 50
						index += 1
					elif event.key == pygame.K_DOWN:
						moves.append(pygame.K_DOWN)
						moveImg.append(down)
						arrowPosy.append(posy)
						posy += 50
						index += 1
					elif event.key == pygame.K_LEFT:
						moves.append(pygame.K_LEFT)
						moveImg.append(left)
						arrowPosy.append(posy)
						posy += 50
						index += 1
					elif event.key == pygame.K_RIGHT:
						moves.append(pygame.K_RIGHT)
						moveImg.append(right)
						arrowPosy.append(posy)
						posy += 50
						index += 1
					elif event.key == pygame.K_BACKSPACE:
						moves.pop()
						moveImg.pop()
						arrowPosy.pop()
						posy -=50
						index-= 1
						gameSetup()
						for pos,image in zip(arrowPosy,moveImg):
							screen.blit(pygame.image.load(image), (750, pos))
							pygame.display.flip()
					elif event.key == pygame.K_SPACE:
						spaceBar = True
			except IndexError:
				index = 0
				gameSetup()
				drawMoves()
				gamePlay()
		drawMoves()
		
		
	else:
		global count
		print moveImg
		print index
		print moveImg
		count += 1
		
#for move in moveImg:
		#	arrowPic=[];
		#	arrowPic.append(pygame.image.load(move))
		#	print arrowPic
		#	for AP in arrowPic:
		#		screen.blit(AP, (arrowBlitPosx,arrowPosy[len(moves)-1]))
		#		pygame.display.flip()
		

			

#level 1
if level == 1: 
	for x in range(width/grass.get_width()+1):
		for y in range(height/grass.get_height()+1):
			puzzleArea.blit(grass,(x*125,y*200))
	while count < 1:
		gameSetup()
		gamePlay()
	else:
		while True:
			gameSetup()
#level 2
elif level == 2:
	for x in range(width/grass.get_width()+1):
		for y in range(height/grass.get_height()+1):
			puzzleArea.blit(shark,(x*125,y*200))
	while count < 1:
		gameSetup()
		gamePlay()
		
		
	else:
		while True:
			gamePlay()
# 7 - update the screen
	
# 8 - loop through the events
for event in pygame.event.get():
		# check if the event is the X button 
	if event.type==pygame.QUIT:
		# if it is quit the game
		pygame.quit() 
		exit(0)


