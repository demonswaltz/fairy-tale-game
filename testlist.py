import pygame
from pygame.locals import *

stones = [1,2,3,4,5]
stonePile=[]
pathStones= pygame.sprite.Group()

class Path(pygame.sprite.Sprite):
	def __init__(self):
		super (Path, self).__init__()
		self.surf = pygame.Surface((45,45))
		self.surf = pygame.image.load("resources/images/path.png")
		self.rect = self.surf.get_rect()

for stone in stones:
	itemstr= str(stone)
	stoneID = "path" + itemstr
	stonePile.append(stoneID)
for ID in stoneID:
	ID = Path()
	pathStones.add(ID)
	print pathStones.sprites
	print stonePile
		
	
	
