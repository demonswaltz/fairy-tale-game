import pygame
from pygame.locals import *

#I have class(es)
class Path(pygame.sprite.Sprite):
	def __init__(self, width=45, height=45):
		super (Path, self).__init__()
		#self.surf = pygame.Surface ((45,45))
		self.image = pygame.image.load("resources/images/path.png")
		self.rect = self.image.get_rect()
		#self.mask = pygame.mask.from_surface(self.image)
		#pygame.sprite.Sprite.__init__(self, pathTiles)
	
class Player(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.surf = pygame.Surface((45,45))
		self.image = pygame.image.load("resources/images/lilRed.png")
		self.rect = self.image.get_rect()
		self.mask = pygame.mask.from_surface(self.image)
#Groups
pathTiles = pygame.sprite.Group()

#global variables
pygame.init()
width, height = 1000,750
screen=pygame.display.set_mode((width, height))
puzzleArea=pygame.Surface((700, 500))
pathArea = pygame.Surface([700,500], pygame.SRCALPHA, 32)
pathArea = pathArea.convert_alpha()
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
lilRed = Player()

lrMask=pygame.mask.from_surface(lilRed.image)
pathMask=pygame.mask.from_surface(pathArea)
#images
vertline = pygame.image.load("resources/images/vert-line.png")
grass = pygame.image.load("resources/images/grass1.png")
shark = pygame.image.load("resources/images/shark_1.png")
path = pygame.image.load("resources/images/path.png")
#lilRed=pygame.image.load("resources/images/lilRed.png")
up = "resources/images/up.png"
down = "resources/images/down.png"
left = "resources/images/left.png"
right = "resources/images/right.png"
gameover= pygame.image.load("resources/images/gameover.png")

#Create list of tiles in path and add tiles to group pathTiles
path1 = Path()
path2 = Path()
path3 = Path()
path4 = Path()
path5 = Path()
path6 = Path()

pathTiles.add(path1, path2, path3, path4, path5, path6)

#Game Layout Function Does not (!) draw lilRed
def gameSetup():
		global level
		lev_str = str(level)
		pygame.display.set_caption("LEVEL "+ lev_str)
		screen.fill((245,222,179))
		screen.blit(puzzleArea, (0,0))
		screen.blit(pathArea, (0,0))
		screen.blit(vertline,(710,-55))
		pygame.display.flip()
		
#Draw Moves Function shows arrows on screen for keypresses
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
		screen.blit(lilRed.image, (playerpos[0],playerpos[1]))
		pygame.display.flip()
			
#Basic Input Mechanics accepts keypresses
def gamePlay():
	global arrowPosy
	global index 
	global moves
	global posy
	global spaceBar
	global playerpos
	while spaceBar == False and index < 14:
		drawMoves()
		for event in pygame.event.get():
			try:
				if event.type == pygame.KEYDOWN:
					gameSetup()
					screen.blit(lilRed.image, (playerpos[0],playerpos[1]))
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
						drawRed()
						for pos,image in zip(arrowPosy,moveImg):
							screen.blit(pygame.image.load(image), (850, pos))
							pygame.display.flip()
					elif event.key == pygame.K_SPACE:
						spaceBar = True
			except IndexError:
				index = 0
				gameSetup()
				screen.blit(lilRed.image, (playerpos[0],playerpos[1]))
				drawMoves()
				gamePlay()
		drawMoves()
	else:
		global count
		count += 1
		
def drawRed():
	screen.blit(puzzleArea, (0,0))
	######## Draw path!!!
	screen.blit(lilRed.image, (playerpos[0],playerpos[1]))
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
			drawRed()
			checkCollision()
			
						
		#down
		elif move == 274:
			print "down"
			playerpos[1] += 45
			drawRed()
			checkCollision()
			
			
		#left
		elif move == 276:
			print "left"
			playerpos[0] -= 46
			drawRed()
			checkCollision()
			
		#right
		elif move == 275:
			print "right"
			playerpos[0] += 45
			drawRed()
			checkCollision()
			
def checkCollision():
	if spritecollide(lilRed, pathTiles, dokill=False, collided = None) <= 1:
		continue
	elif index < 14:
		spaceBar = False
		gamePlay()
	else:
		moves.pop()
		moveImg.pop()
		arrowPosy.pop()
		posy -=50
		index-= 1
		gameSetup()
		drawRed()
		
		
	
def levelOne():
	global playerpos
	playerpos = [100,50]
	for x in range(width/grass.get_width()+1):
		for y in range(height/grass.get_height()+1):
			puzzleArea.blit(grass,(x*125,y*200))
	path1.set_pos (100, 50)
	path2.set_pos (100, 95)
	path3.set_pos (100, 140)
	path4.set_pos (100, 185)
	path5.set_pos (100, 230)
	path6.set_pos (100, 275)
	lilRed.set_pos (playerpos[0],playerpos[1])
	pathTiles.draw(screen)
	pygame.display.flip()

#level 1
while level == 1: 
	levelOne()
	while count == 0:
		gamePlay()
	else:
		while count == 1:
			gameRun()
			count = 0
			level += 1
		
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
	
# 8 - loop through the events
for event in pygame.event.get():
		# check if the event is the X button 
	if event.type==pygame.QUIT:
		# if it is quit the game
		pygame.quit() 
		exit(0)
