
import pygame
import os

current_folder = os.path.dirname(__file__)
image_folder = os.path.join(current_folder, "../images")


class ChessPiece(pygame.sprite.Sprite):

	def __init__(self, name = None, color = None, position = None, is_taken = False, 
		image = None , board_position = None):

		super().__init__()

		#self.image = pygame.image.load(os.path.join(image_folder,image)).convert_alpha()

		self.image_title = image
		self.image = pygame.image.load(current_folder +  '/../images/' + image).convert_alpha()
		self.image = pygame.transform.scale(self.image , (21,21))
		self.rect = self.image.get_rect()
		self.rect.center = (position[0], position[1])

		#Chess attributes
		self.name = name	
		self.color = color
		self.position = position
		self.is_taken = is_taken

		self.board_position = board_position

	"""
	Draw green circle once player clicks on piece, 
	when about to move piece
	"""
	def draw_red_border(self, screen):
		RED = (255, 0, 0)
		pygame.draw.rect(screen, RED, self.rect, 2)


class EmptySpace(pygame.sprite.Sprite):

	def __init__ (self, name = 'Empty', surface_pos = None  , board_position = None):
		super().__init__() 

		self.image = pygame.Surface( (100 , 100) , pygame.SRCALPHA, 32).convert_alpha()
		
		#Rect((left, top), (width, height)) -> Rect
		self.rect  = pygame.Rect(surface_pos[0] , surface_pos[1] , 21, 19)
		self.name = name
		self.board_position = board_position


	def draw_green_border(self, screen):
		GREEN = (0, 255, 0)
		pygame.draw.rect(screen, GREEN, self.rect, 2)


