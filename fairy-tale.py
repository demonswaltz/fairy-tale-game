import pygame
from pygame.locals import *

#I got class



#Supposedly Global Variables
pygame.init()
width, height = 1000,750
screen=pygame.display.set_mode((width, height))
puzzleArea=pygame.Surface((700, 500))
redRect= pygame.Surface
keys = [False, False, False, False]
arrowPosy=[];
level=1
index = 0
moves= [];
moveImg=[];
count = 0
spaceBar=False
posy=16
lilRedSpot=[];

#images
vertline = pygame.image.load("resources/images/vert-line.png")
grass = pygame.image.load("resources/images/grass1.png")
shark = pygame.image.load("resources/images/shark_1.png")
path = pygame.image.load("resources/images/path.png")
lilRed=pygame.image.load("resources/images/lilRed.png")
up = "resources/images/up.png"
down = "resources/images/down.png"
left = "resources/images/left.png"
right = "resources/images/right.png"


#Game Layout Function
def gameSetup():
		global level
		lev_str = str(level)
		pygame.display.set_caption("LEVEL "+ lev_str)
		screen.fill((245,222,179))
		screen.blit(puzzleArea, (0,0))
		screen.blit (lilRed, (playerpos[0],playerpos[1]))
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
			screen.blit(pygame.image.load(image), (850, pos))
			pygame.display.flip()
	else:
		gameSetup()
			
#Basic Input Mechanics
def gamePlay():
	global arrowPosy
	global index 
	global moves
	global posy
	global spaceBar
	while spaceBar == False and index < 14:
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
							screen.blit(pygame.image.load(image), (850, pos))
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
def drawRed():
	global lilRedSpot
	screen.blit(puzzleArea, (0,0))
	screen.blit(lilRed, (playerpos[0], playerpos[1]))
	lilRedSpot.pop()
	lilRedSpot.pop()
	pygame.display.flip()
	pygame.time.wait(1000)		

	
		
#Basic Game
def gameRun():
	global moves
	global playerpos
	global puzzleArea
	global count
	global lilRedSpot
	for move in moves:
		#up
		if move == 273:
			print "up"
			playerpos[1] -= 45
			lilRedSpot.append(playerpos[0])
			lilRedSpot.append(playerpos[1])
			drawRed()
						
		#down
		elif move == 274:
			print "down"
			playerpos[1] += 45
			lilRedSpot.append(playerpos[0])
			lilRedSpot.append(playerpos[1])
			drawRed()
			
		#left
		elif move == 276:
			print "left"
			playerpos[0] -= 45
			lilRedSpot.append(playerpos[0])
			lilRedSpot.append(playerpos[1])
			drawRed()
		
		#right
		elif move == 275:
			print "right"
			playerpos[0] += 45
			lilRedSpot.append(playerpos[0])
			lilRedSpot.append(playerpos[1])
			drawRed()

#def checkCollide
	
	
	
			

#level 1
while level == 1: 
	playerpos = [100,5]
	for x in range(width/grass.get_width()+1):
		for y in range(height/grass.get_height()+1):
			puzzleArea.blit(grass,(x*125,y*200))
	puzzleArea.blit (path, (100, 50))
	puzzleArea.blit (path, (100, 95))
	puzzleArea.blit (path, (100, 140))
	puzzleArea.blit (path, (100, 185))
	puzzleArea.blit (path, (100, 230))
	puzzleArea.blit (path, (100, 275))
	screen.blit(lilRed, (playerpos[0],playerpos[1]))
	pygame.display.flip()
	while count < 1:
		
		gameSetup()
		gamePlay()
	else:
		while count < 2:
			gameRun()
			count += 1
		
				
				
			
#level 2
else:
	while level == 2:
		for x in range(width/grass.get_width()+1):
			for y in range(height/grass.get_height()+1):
				puzzleArea.blit(shark,(x*125,y*200))
		while count < 1:
			gameSetup()
			gamePlay()
			
		
		else:
			while True:
				gamePlay()
	else:
		while level == 3:
			while count <1:
				gameSetup()
		
# 7 - update the screen
	
# 8 - loop through the events
for event in pygame.event.get():
		# check if the event is the X button 
	if event.type==pygame.QUIT:
		# if it is quit the game
		pygame.quit() 
		exit(0)


