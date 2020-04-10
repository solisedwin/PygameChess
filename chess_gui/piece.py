
import pygame
import os

current_folder = os.path.dirname(__file__)
image_folder = os.path.join(current_folder, "../images")


class ChessPiece(pygame.sprite.Sprite):


	def __init__(self, name = None, color = None, position = None, is_taken = False, image = None):

		super().__init__()

		#self.image = pygame.image.load(os.path.join(image_folder,image)).convert_alpha()

		self.image_title = image
		self.image = pygame.image.load(current_folder +  '/../images/' + image).convert_alpha()


		self.rect = self.image.get_rect()
		self.rect.center = (position[0], position[1])

		#Chess attributes
		self.name = name
		self.color = color
		self.position = position
		self.is_taken = is_taken

		












