import pygame

class Path(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.surf = pygame.Surface ((45,45))
		self.image = pygame.image.load("resources/images/path.png")
		self.rect = self.image.get_rect()

class Player(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.surf = pygame.Surface((45,45))
		self.image = pygame.image.load("resources/images/lilRed.png")
		self.rect = self.image.get_rect()
		

pygame.init()
width, height = 400,400
screen=pygame.display.set_mode((width, height))
path = pygame.image.load("resources/images/path.png")
lilRed=pygame.image.load("resources/images/lilRed.png")
lilRed = Player()
path = Path()

def checkcollide():
	if pygame.sprite.collide_rect(lilRed, path):
		print "Collide"
	else: 
		print "nope"


while 1:
	screen.blit(path.image, (100,100))
	screen.blit(lilRed.image, (100,15))
	pygame.display.flip()
	checkcollide()
	



for event in pygame.event.get():
		# check if the event is the X button 
	if event.type==pygame.QUIT:
		# if it is quit the game
		pygame.quit() 
		exit(0)
