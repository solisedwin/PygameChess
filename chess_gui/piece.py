
import pygame
import os

current_folder = os.path.dirname(__file__)
image_folder = os.path.join(current_folder, "../images")


class ChessPiece(pygame.sprite.Sprite):
	"""docstring for ChessPiece"""
	def __init__(self, name = None, color = None, position = None, is_taken = False, 
		image = None , board_position = None):
		
		super().__init__()

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
		
		
	def draw_red_border(self, screen):
		RED = (255, 0, 0)
		pygame.draw.rect(screen, RED, self.rect, 2)	


class Pawn(ChessPiece):
	"""docstring for Pawn"""
	def __init__(self , **kwargs):
		super(Pawn, self).__init__(**kwargs)
		self.moves = 0


	def valid_moves(self, chess_board, destination_space):

		piece_xpos , piece_ypos = self.board_position[0] ,self.board_position[1]
		destination_xpos , destination_ypos = destination_space.board_position[0] , destination_space.board_position[1]


		#If its the first time we move a pawn, then we can move it once or twice. 
		if self.moves == 0:
			if piece_ypos + 1 == destination_xpos or piece_ypos + 2 == destination_ypos:
				self.position = destination_space.rect

		elif self.destination_ypos == self.piece_ypos + 1:
			self.position = destination_space.rect

		elif self.piece_ypos == 7 and self.destination_ypos == 8:
			print('*** Time to promote the pawn to a Queen ***')
		else:
			print('Not a valid move for the pawn !!!!')



class Rook(ChessPiece):
	"""docstring for Rook"""
	def __init__(self , **kwargs):
		super(Rook, self).__init__(**kwargs)
	
		
	def valid_moves(self, chess_board):
		pass


class Knight(ChessPiece):
	"""docstring for Knight"""
	def __init__(self , **kwargs):
		super(Knight, self).__init__(**kwargs)
		
		

class Bishop(ChessPiece):
	"""docstring for Bishop"""
	def __init__(self , **kwargs):
		super(Bishop, self).__init__(**kwargs)	


class King(ChessPiece):
	"""docstring for King """
	def __init__(self , **kwargs):
		super(King, self).__init__(**kwargs)
	
		
class Queen(ChessPiece):
	"""docstring for Queen"""
	def __init__(self , **kwargs):
		super(Queen, self).__init__(**kwargs)

	
class Rook(ChessPiece):
	"""docstring for Rook """
	def __init__(self , **kwargs):
		super(Rook, self).__init__(**kwargs)


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


