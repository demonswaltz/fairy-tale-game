import pygame
from pygame.locals import *

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
grass = pygame.image.load("resources/images/grass1.png")
shark = pygame.image.load("resources/images/shark_1.png")
house = pygame.image.load("resources/images/house.png")
path = "resources/images/path.png"
redpathimg = "resources/images/redpath.png"
treeimg1 = "resources/images/tree1.png"
treeimg2 = "resources/images/tree2.png"
treeimg5 = "resources/images/tree5.png"
lilImage="resources/images/lilRed.png"
up = "resources/images/up.png"
down = "resources/images/down.png"
left = "resources/images/left.png"
right = "resources/images/right.png"
gameover= pygame.image.load("resources/images/gameover.png")

#Game Layout Function Does not (!) draw lilRed
def gameSetup():
		global level
		global playerpos
		lev_str = str(level)
		pygame.display.set_caption("LEVEL "+ lev_str)
		screen.fill((245,222,179))
		screen.blit(puzzleArea, (0,0))
		pathTiles.draw(screen)
		happyTrees.draw(screen)
		redGroup.draw(screen)
		screen.blit(text, (200, 550))
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
	while collide == True:	
		for move in moves:
				#up
				if move == 273:
					print "up"
					playerpos[1] -= 45
					drawRed()
					if collide == False:
						break
					checkCollision()
					
				#down
				elif move == 274:
					print "down"
					playerpos[1] += 45
					drawRed()
					if collide == False:
						break
					checkCollision()
					
				#left
				elif move == 276:
					print "left"
					playerpos[0] -= 45
					drawRed()
					if collide == False:
						break
					checkCollision()
					
				#right
				elif move == 275:
					print "right"
					playerpos[0] += 45
					drawRed()
					if collide == False:
						break
					checkCollision()
					
						
def levelOne():
	print "levelOne"
	global playerpos
	global font
	global text
	global count
	global spaceBar
	global redpathpos
	global moves
	print moves
	spaceBar = False
	count = 0
	playerpos = [55,50]
	for x in range(width/grass.get_width()+1):
		for y in range(height/grass.get_height()+1):
			puzzleArea.blit(grass,(x*125,y*200))
	path1 = Path()
	path2 = Path()
	path3 = Path()
	path4 = Path()
	path1.set_image(path)
	path2.set_image(path)
	path3.set_image(path)
	path4.set_image(path)
	redStone.set_image(redpathimg)
	path1.set_pos(playerpos[0],playerpos[1])
	path2.set_pos (100, 50)
	path3.set_pos (145, 50)
	path4.set_pos (145,95)
	redStone.set_pos(190, 95)
	pathTiles.add(path1, path2, path3, path4)
	stonePile= [path1, path2]
	tree1 = Tree()
	tree2 = Tree()
	tree3 = Tree()
	tree4 = Tree()
	tree5 = Tree()
	tree6 = Tree()
	tree7 = Tree()
	tree8 = Tree()
	tree9 = Tree()
	tree10 = Tree()
	tree11 = Tree()
	tree12 = Tree()
	tree1.set_image(treeimg1)
	tree2.set_image(treeimg1)
	tree3.set_image(treeimg1)
	tree4.set_image(treeimg1)
	tree5.set_image(treeimg2)
	tree6.set_image(treeimg2)
	tree7.set_image(treeimg2)
	tree8.set_image(treeimg2)
	tree9.set_image(treeimg5)
	tree10.set_image(treeimg5)
	tree11.set_image(treeimg5)
	tree12.set_image(treeimg5)
	tree1.set_pos(145, 245)
	tree2.set_pos(600, 234)
	tree3.set_pos(300, 200)
	tree4.set_pos(75, 285)
	tree5.set_pos(450, 350)
	happyTrees.add(tree1, tree2, tree3, tree4, tree5, tree6, tree7, tree8, tree9, tree10, tree11, tree12)
	pathTiles.draw(screen)
	happyTrees.draw(screen)
	lilRed.set_image(lilImage)
	lilRed.set_pos (playerpos[0],playerpos[1])
	playerGroup.draw(screen)
	redGroup.draw(screen)
	text = font.render ("Hello World", True, (0,0,0))
	screen.blit(text, (200, 700))
	pygame.display.flip()

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
	if pygame.sprite.collide_rect(lilRed, redStone)  == False:
		if len(pygame.sprite.spritecollide(lilRed, pathTiles, False, collided = None)) > 0 :
			print "Woo!"
		elif index < 14:
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
	else:
		collide = False
		level += 1
		
	
	
while level == 1: 
	levelOne()
	print count
	while count == 0:
		gamePlay()
		print count
	else:
		while count == 1:
			print "ELSE!!"
			gameRun()
			count = 0

while level == 2: 
	levelTwo()
	print count
	while count == 0:
		gamePlay()
		print count
	else:
		while count == 1:
			print "ELSE!!"
			gameRun()
			count = 0			

			
for event in pygame.event.get():
		# check if the event is the X button 
	if event.type==pygame.QUIT:
		# if it is quit the game
		pygame.quit() 
		exit(0)
