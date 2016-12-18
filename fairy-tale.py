import pygame
from pygame.locals import *
#import pyganim

class Path(pygame.sprite.Sprite):
	def __init__(self, width=45, height=45):
		super (Path, self).__init__()
		self.image = pygame.Surface ((width, height))
		self.image.fill((255,255,255,0))
		self.rect = self.image.get_rect()
	def set_pos(self, x, y):
		self.rect.x = x
		self.rect.y = y
	def set_image(self, filename = None):
		if filename != None:
			self.image = pygame.image.load( filename )
			self.rect = self.image.get_rect()
class RedPath(pygame.sprite.Sprite):
	def __init__(self, width=45, height=45):
		super (RedPath, self).__init__()
		self.image = pygame.Surface ((width, height))
		self.image.fill((0,225,0,0))
		self.rect = self.image.get_rect()
	def set_pos(self, x, y):
		self.rect.x = x
		self.rect.y = y
	def set_image(self, filename = None):
		if filename != None:
			self.image = pygame.image.load( filename )
			self.rect = self.image.get_rect()
class Player(pygame.sprite.Sprite):
	def __init__(self, width=45, height=45):
		super (Player, self).__init__()
		self.image = pygame.Surface ((width, height))
		self.image.fill((0,225,0,0))
		self.rect = self.image.get_rect()
	def set_pos(self, x, y):
		self.rect.x = x
		self.rect.y = y
	def set_image(self, filename = None):
		if filename != None:
			self.image = pygame.image.load( filename )
			self.rect = self.image.get_rect()
class Tree(pygame.sprite.Sprite):
	def __init__(self, width=64, height=64):
		super (Tree, self).__init__()
		self.image = pygame.Surface ((width, height))
		self.image.fill((0,225,0,0))
		self.rect = self.image.get_rect()
	def set_pos(self, x, y):
		self.rect.x = x
		self.rect.y = y
	def set_image(self, filename = None):
		if filename != None:
			self.image = pygame.image.load( filename )
			self.rect = self.image.get_rect()
					
#Groups
pathTiles = pygame.sprite.Group()
playerGroup = pygame.sprite.Group()
happyTrees = pygame.sprite.Group()
redGroup = pygame.sprite.Group()
	

#global variables
pygame.init()
width, height = 1000,750
screen=pygame.display.set_mode((width, height))
puzzleArea=pygame.Surface((700, 500))
instructions= pygame.Surface ((1000, 200))
keys = [False, False, False, False]
arrowPosy=[];
level=1
index = 0
moves= [];
moveImg=[];
count = 0
spaceBar=False
collide = True
posy=16
lilRedSpot=[];
lilRed = Player()
playerGroup.add(lilRed)
font = pygame.font.SysFont("Ariel", 30)
redStone = RedPath()
redGroup.add(redStone)

#images
vertline = pygame.image.load("resources/images/vert-line.png")
level1bg = pygame.image.load("resources/images/level1.png")
level2bg = pygame.image.load("resources/images/level2.png")
level3bg = pygame.image.load("resources/images/level3.png")
houseimg = "resources/images/house.png"
path = "resources/images/path.png"
redpathimg = "resources/images/redpath.png"
lilImage="resources/images/lilRed.png"
up = "resources/images/up.png"
down = "resources/images/down.png"
left = "resources/images/left.png"
right = "resources/images/right.png"
gameover= pygame.image.load("resources/images/gameover.png")
wolfss = "resources/images/wolfTree.png"

#wolf animation load
#wolfimg = pyganim.getImagesFromSpriteSheet(wolfss, rows=1, cols=5)
#wolfframes = list(zip(wolfimg, [50, 50, 50, 50, 50]))
#wolfanim = pyganim.PygAnimation(wolfframes)
#wolfanim.play()
#Game Layout Function Does not (!) draw lilRed
def gameSetup():
		global level
		global playerpos
		lev_str = str(level)
		pygame.display.set_caption("LEVEL "+ lev_str)
		screen.fill((245,222,179))
		screen.blit(puzzleArea, (0,0))
		pathTiles.draw(screen)
		redGroup.draw(screen)
		screen.blit(text1, (50, 550))
		screen.blit(text2, (50, 575))
		playerGroup.draw(screen)
		redGroup.draw(screen)
		screen.blit(vertline,(710,-55))
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
					#screen.blit(lilRed.image, (playerpos[0],playerpos[1]))
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
		#screen.blit(lilRed.image, (playerpos[0],playerpos[1]))
		pygame.display.flip()
#Draw Player Moves		
def drawRed():
	print "drawRed"
	screen.blit(puzzleArea, (0,0))
	lilRed.set_image(lilImage)
	lilRed.set_pos (playerpos[0], playerpos[1])
	pathTiles.draw(screen)
	happyTrees.draw(screen)
	redGroup.draw(screen)
	playerGroup.draw(screen)
	pygame.display.flip()
	pygame.time.wait(1000)
#Basic Game
def gameRun():
	print "gameRun"
	global moves
	global playerpos
	global puzzleArea
	global collide
	collide = True
	for move in moves:
		#up
		if move == 273:
			checkCollision()
			if collide == False:
				print "No Collision"
				break
			else:	
				print "up"
				playerpos[1] -= 45
				drawRed()
				checkCollision()
		#down
		elif move == 274:
			checkCollision()
			print "down"
			playerpos[1] += 45
			drawRed()
			checkCollision()
			checkCollision()
		#left
		elif move == 276:
			checkCollision()
			if collide == False:
				print "No Collision"
				break
			else:	
				print "left"
				playerpos[0] -= 45
				drawRed()
				checkCollision()
		#right
		elif move == 275:
			checkCollision()
			playerpos[0] += 45
			drawRed()
			checkCollision()
#Name says it all... Are they colliding??  Let's check
def checkRedCol():
	global level
	global moves
	global moveImg
	global index
	while pygame.sprite.collide_rect(lilRed, redStone)  == False:
		gameRun()
	else:
		for tile in pathTiles:
			pathTiles.remove(tile)
		moves = []
		moveImg=[]
		index = 0
		level += 1
		
def checkCollision():
	print "checkCollision"
	global index
	global moves
	global moveImg
	global arrowPosy
	global posy
	global spaceBar
	global level
	global collide
	print level
	if len(pygame.sprite.spritecollide(lilRed, pathTiles, False, collided = None)) > 0:
		print "woo"
		if index < 14:
			spaceBar = False
			collide = False
			gameSetup()
			count = 0
		else:
			collide = False
			moves.pop()
			moveImg.pop()
			arrowPosy.pop()
			posy -=50
			index-= 1
			gameSetup()
			count = 0
	
		
#The very first level		
def levelOne():
	print "levelOne"
	global playerpos
	global font
	global text1
	global text2
	global count
	global spaceBar
	global redpathpos
	global moves
	#global wolfanim
	spaceBar = False
	count = 0
	playerpos = [255,77]
	puzzleArea.blit(level1bg,(0,0))
	#wolfanim.blit(puzzleArea, (355, 257))
	path1 = Path()
	path2 = Path()
	path3 = Path()
	house = Path()
	path1.set_image(path)
	path2.set_image(path)
	path3.set_image(path)
	house.set_image(houseimg)
	redStone.set_image(redpathimg)
	path1.set_pos(255,122)
	path2.set_pos (255, 167)
	path3.set_pos (255, 212)
	redStone.set_pos(255, 257)
	house.set_pos(213, 3)
	pathTiles.add(path1, path2, path3,house)
	stonePile= [path1, path2, path3]
	lilRed.set_image(lilImage)
	lilRed.set_pos (playerpos[0],playerpos[1])
	playerGroup.draw(screen)
	redGroup.draw(screen)
	text1 = font.render ("Use the arrow keys to direct Little Red down the path and into the woods.", True, (0,0,0))
	text2 = font.render("Press the space bar when you are done.", True, (0,0,0))
	#text3 = font.render("
	pygame.display.flip()
#The next level
def levelTwo():
	print "Level Two"
	global playerpos
	global font
	global text1
	global text2
	global count
	global spaceBar
	global redpathpos
	global moves
	spaceBar = False
	count = 0
	playerpos = [430, 0]
	puzzleArea.blit(level2bg,(0,0))
	path1 = Path()
	path2 = Path()
	path3 = Path()
	path4 = Path()
	path5 = Path()
	path6 = Path()
	path7 = Path()
	path1.set_image(path)
	path2.set_image(path)
	path3.set_image(path)
	path4.set_image(path)
	path5.set_image(path)
	path6.set_image(path)
	path7.set_image(path)
	pathTiles.add(path1, path2, path3, path4, path5, path6, path7)
	redStone.set_image(redpathimg)
	path1.set_pos(430,0)
	path2.set_pos (430, 45)
	path3.set_pos (430, 90)
	path4.set_pos (475, 90)
	path5.set_pos (520, 90)
	path6.set_pos (565, 90)
	path7.set_pos (610, 90)
	redStone.set_pos(655, 90)
	lilRed.set_image(lilImage)
	lilRed.set_pos (playerpos[0],playerpos[1])
	playerGroup.draw(screen)
	redGroup.draw(screen)
	text1 = font.render ("Use the arrow keys to direct Little Red down the path and into the woods.", True, (0,0,0))
	text2 = font.render("Press the space bar when you are done.", True, (0,0,0))
#Level THREE!!!!
def levelThree():
	print "Level Three"
	global playerpos
	global font
	global text1
	global text2
	global count
	global spaceBar
	global redpathpos
	global moves
	spaceBar = False
	count = 0
	playerpos = [0,90]
	puzzleArea.blit(level3bg,(0,0))
	path1 = Path()
	path2 = Path()
	path3 = Path()
	path4 = Path()
	path5 = Path()
	path6 = Path()
	path7 = Path()
	path8 = Path()
	path9 = Path()
	path11 = Path()
	path12 = Path()
	path13 = Path()
	path14 = Path()
	path15 = Path()
	path16 = Path()
	path17 = Path()
	path18 = Path()
	path1.set_image(path)
	path2.set_image(path)
	path3.set_image(path)
	path4.set_image(path)
	path5.set_image(path)
	path6.set_image(path)
	path7.set_image(path)
	path8.set_image(path)
	path9.set_image(path)
	path11.set_image(path)
	path12.set_image(path)
	path13.set_image(path)
	path14.set_image(path)
	path15.set_image(path)
	path16.set_image(path)
	path17.set_image(path)
	path18.set_image(path)
	pathTiles.add(path1, path2, path3, path4, path5, path6,path7, path8, path9, path11, path12, path13, path14, path15, path16, path17, path18)
	redStone.set_image(path)
	path1.set_pos(0,90)
	path2.set_pos (45, 90)
	path3.set_pos (45, 135)
	path4.set_pos (90, 135)
	path5.set_pos (135, 135)
	path6.set_pos (135, 180)
	path7.set_pos (135, 225)
	path8.set_pos (180, 225)
	path9.set_pos (225, 225)
	redStone.set_pos (270, 225)
	path11.set_pos (315, 225)
	path12.set_pos (360, 225)
	path13.set_pos (405, 225)
	path14.set_pos (450, 225)
	path15.set_pos (495, 225)
	path16.set_pos (540, 225)
	path17.set_pos (585, 225)
	path18.set_pos (630, 225)
	lilRed.set_image(lilImage)
	lilRed.set_pos (playerpos[0],playerpos[1])
	playerGroup.draw(screen)
	redGroup.draw(screen)
	text1 = font.render ("Use the arrow keys to direct Little Red down the path and into the woods.", True, (0,0,0))
	text2 = font.render("Press the space bar when you are done.", True, (0,0,0))
#Another one
def levelFour():
	print "Level Four"
	global playerpos
	global font
	global text1
	global text2
	global count
	global spaceBar
	global moves
	print playerpos
	spaceBar = False
	count = 0
	puzzleArea.blit(level3bg,(0,0))
	path1 = Path()
	path2 = Path()
	path3 = Path()
	path4 = Path()
	path5 = Path()
	path6 = Path()
	path7 = Path()
	path8 = Path()
	path9 = Path()
	path10 = Path()
	path11 = Path()
	path12 = Path()
	path13 = Path()
	path14 = Path()
	path15 = Path()
	path16 = Path()
	path17 = Path()
	path18 = Path()
	path1.set_image(path)
	path2.set_image(path)
	path3.set_image(path)
	path4.set_image(path)
	path5.set_image(path)
	path6.set_image(path)
	path7.set_image(path)
	path8.set_image(path)
	path9.set_image(path)
	path10.set_image(path)
	path11.set_image(path)
	path12.set_image(path)
	path13.set_image(path)
	path14.set_image(path)
	path15.set_image(path)
	path16.set_image(path)
	path17.set_image(path)
	pathTiles.add(path1, path2, path3, path4, path5, path6,path7, path8, path9, path10, path11, path12, path13, path14, path15, path16, path17, path18)
	redStone.set_image(redpathimg)
	path1.set_pos(0,90)
	path2.set_pos (45, 90)
	path3.set_pos (45, 135)
	path4.set_pos (90, 135)
	path5.set_pos (135, 135)
	path6.set_pos (135, 180)
	path7.set_pos (135, 225)
	path8.set_pos (180, 225)
	path9.set_pos (225, 225)
	path10.set_pos (270, 225)
	path11.set_pos (315, 225)
	path12.set_pos (360, 225)
	path13.set_pos (405, 225)
	path14.set_pos (450, 225)
	path15.set_pos (495, 225)
	path16.set_pos (540, 225)
	path17.set_pos (585, 225)
	redStone.set_pos (630, 225)
	lilRed.set_image(lilImage)
	lilRed.set_pos (playerpos[0],playerpos[1])
	playerGroup.draw(screen)
	redGroup.draw(screen)
	text1 = font.render ("Use the arrow keys to direct Little Red down the path and into the woods.", True, (0,0,0))
	text2 = font.render("Press the space bar when you are done.", True, (0,0,0))	
while level == 1: 
	levelOne()
	gameSetup()
	while count == 0:
		gamePlay()
	else:
		while count == 1:
			checkRedCol()
			count = 0

while level == 2: 
	levelTwo()
	gameSetup()
	while count == 0:
		gamePlay()
	else:
		while count == 1:
			checkRedCol()
			count = 0			

while level == 3: 
	levelThree()
	gameSetup()
	while count == 0:
		gamePlay()
	else:
		while count == 1:
			checkRedCol()
			count = 0	

while level == 4: 
	levelFour()
	gameSetup()
	while count == 0:
		gamePlay()
	else:
		while count == 1:
			checkRedCol()
			count = 0	
			
while level == 5: 
	levelFive()
	gameSetup()
	while count == 0:
		gamePlay()
	else:
		while count == 1:
			checkRedCol()
			count = 0

while level == 6: 
	levelSix()
	gameSetup()
	while count == 0:
		gamePlay()
	else:
		while count == 1:
			gameRun()
			count = 0
			
while level == 7: 
	levelSeven()
	gameSetup()
	while count == 0:
		gamePlay()
	else:
		while count == 1:
			gameRun()
			count = 0
			
while level == 8 : 
	levelEight()
	gameSetup()
	while count == 0:
		gamePlay()
	else:
		while count == 1:
			gameRun()
			count = 0							

while level == 9: 
	levelNine()
	gameSetup()
	while count == 0:
		gamePlay()
	else:
		while count == 1:
			gameRun()
			count = 0	

while level == 10 : 
	levelTen()
	gameSetup()
	while count == 0:
		gamePlay()
	else:
		while count == 1:
			gameRun()
			count = 0	

for event in pygame.event.get():
		# check if the event is the X button 
	if event.type==pygame.QUIT:
		# if it is quit the game
		pygame.quit() 
		exit(0)
