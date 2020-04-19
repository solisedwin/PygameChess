
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


	def valid_moves(self, chess_board,  destination_piece):

		piece_xpos , piece_ypos = self.board_position[0] ,self.board_position[1]
		destination_xpos , destination_ypos = destination_piece.board_position[0] , destination_piece.board_position[1]

	
		#If its the first time we move a pawn, then we can move it once or twice. 
		if self.moves == 0:
			if piece_xpos - 1 == destination_xpos or piece_xpos - 2 == destination_xpos:
				#self.position = destination_space.rect
				self.board_position = [destination_xpos , destination_ypos]
				self.moves += 1
				return True

		elif piece_xpos - 1 == destination_xpos:
			#self.position = destination_space.rect
			self.board_position = [destination_xpos , destination_ypos]
			return True

		elif piece_xpos == 1 and destination_xpos == 0:
			return True
		else:
			return False


class Rook(ChessPiece):
	"""docstring for Rook"""
	def __init__(self , **kwargs):
		super(Rook, self).__init__(**kwargs)
	

	def valid_moves(self, chess_board , destination_piece):

		piece_xpos , piece_ypos = self.board_position[0] ,self.board_position[1]
		destination_xpos , destination_ypos = destination_piece.board_position[0] , destination_piece.board_position[1]

		# Moving about the column  or row.
		if piece_ypos  == destination_ypos or piece_xpos == destination_xpos:
			print('Valid move for Rook')
		else:
			print('Not a valid move for the Rook !')
	


class Knight(ChessPiece):
	"""docstring for Knight"""
	def __init__(self , **kwargs):
		super(Knight, self).__init__(**kwargs)
		
	def valid_moves(self, chess_board , destination_xpos , destination_ypos):
		piece_xpos , piece_ypos = self.board_position[0] ,self.board_position[1]





class Bishop(ChessPiece):
	"""docstring for Bishop"""
	def __init__(self , **kwargs):
		super(Bishop, self).__init__(**kwargs)


	def valid_moves(self, chess_board , destination_piece):

		piece_xpos , piece_ypos = self.board_position[0] ,self.board_position[1]
		destination_xpos , destination_ypos = destination_piece.board_position[0] , destination_piece.board_position[1]		
		board_size = len(chess_board)



class King(ChessPiece):
	"""docstring for King """
	def __init__(self , **kwargs):
		super(King, self).__init__(**kwargs)
	
	def valid_moves(self, chess_board , destination_piece):
		
		piece_xpos , piece_ypos = self.board_position[0] ,self.board_position[1]
		destination_xpos , destination_ypos = destination_piece.board_position[0] , destination_piece.board_position[1]

		if piece_xpos + 1 == destination_xpos or piece_xpos - 1 == destination_xpos or piece_ypos + 1 == destination_ypos or piece_ypos - 1 == destination_ypos:
			print('Valid Move for King. Moving one vertically or horizontally')  
			return True
		
		#Upper left
		elif ( piece_xpos -1 == destination_xpos and piece_ypos - 1 == destination_ypos ):
			print('Valid King move diagonally. Upper left')
			return True

		 #Upper Right
		elif ( piece_xpos + 1 == destination_xpos and piece_ypos - 1 == destination_ypos ):
			print('Valid King move diagonally. Upper left')
			return True

		#Lower left
		elif ( piece_xpos - 1 == destination_xpos and piece_ypos - 1 == destination_ypos ):
			print('Valid King move diagonally. Upper left')
			return True

		 #Lower Right
		elif ( piece_xpos + 1 == destination_xpos and piece_ypos + 1 == destination_ypos ):
			print('Valid King move diagonally. Upper left')
			return True
		else:
			print('~~ Not a valid move for the king !!')
			return False



class Queen(ChessPiece):
	"""docstring for Queen"""
	def __init__(self , **kwargs):
		super(Queen, self).__init__(**kwargs)



class EmptySpace(pygame.sprite.Sprite):

	def __init__ (self, name = 'Empty', surface_pos = None , board_position = None):

		super().__init__()
		self.image = pygame.Surface( (100 , 100) , pygame.SRCALPHA, 32).convert_alpha()
		
		#Rect((left, top), (width, height)) -> Rect
		self.rect  = pygame.Rect(surface_pos[0] , surface_pos[1] , 21, 19)
		self.name = name
		self.board_position = board_position


	def draw_green_border(self, screen):
		GREEN = (0, 255, 0)
		pygame.draw.rect(screen, GREEN, self.rect, 2)


