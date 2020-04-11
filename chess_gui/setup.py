
import pygame 
from .piece import ChessPiece
from .piece import EmptySpace
from pygame.sprite import Group as SpriteGroup
from pygame.time import Clock
import os

class ChessSetup(object):

	def __init__(self):
			
		self.screen_width = 500
		self.screen_height = 500

		self.all_sprites = SpriteGroup()

		self.image_extension = '.png'

		#self.board_images = ['../images/board_alt.png', '../images/numbers.png', '../images/text.png']

		self.pieces = ['rook', 'knight', 'bishop','king','queen','bishop','knight','rook']
		#Each player will have eight pawns
		self.pawns = ['pawn'] * 8	
		

		"""
		Two dimensional array, e.g.: [0][0] = Top left, rook 
		Each coordinate/spot , will represent if a piece class is present on it
		
		rows = columns (8 x 8)
		"""

	def fill_chess_board(self, board , white_pieces, black_pieces):

		for row in range(8):			
			for col in range(8):
				if row == 0:
					board[row][col] = black_pieces[col]
					black_pieces[col].board_position = [row , col] 
				elif row == 1:
					board[row][col] = black_pieces[8 + col]
					black_pieces[8 + col ].board_position = [row , col]
				elif row == 6:
					board[row][col] = white_pieces[col]
					white_pieces[col].board_position = [row , col]
				elif row == 7:
					board[row][col] = white_pieces[8 + col]
					white_pieces[8 + col].board_position = [row , col]
				else:
					board[row][col] = EmptySpace('Empty Space', [row, col])
		return board



	def setup_pieces(self):
		
		img_black_pieces = [ 'black_' + (piece) + self.image_extension  for piece in self.pieces  ]
		img_white_pieces = [ 'white_' + (piece) + self.image_extension  for piece in self.pieces  ]
		
		img_black_pawns = [ 'black_' + (piece) + self.image_extension  for piece in self.pawns   ]
		img_white_pawns = [ 'white_' + (piece) + self.image_extension  for piece in self.pawns   ]

		#Set intital x,y coordinates (top left for black, bototm left for white) when first displating pieces
		black_piece_xpos , black_piece_ypos = 100,160
		white_piece_xpos , white_piece_ypos = 100 , self.screen_height - 180

		black_pawn_xpos , black_pawn_ypos  =  100 , 185 
		white_pawn_xpos , white_pawn_ypos  =  100, self.screen_height - 205

		pawn_list_index = 0

		"""
		Save pieces and their SPECIFIC order, for when we added the objects to our chess_board
		BR, BK, BB, BKING, BQ, BB , BK , BR 
		"""
		black_piece_objects = []
		white_piece_objects = []

		#Each player has 16 pieces
		for index in range(16):

			if index < 8:

				black_piece = img_black_pieces[index]
				white_piece = img_white_pieces[index]

				black_piece_name = black_piece[ black_piece.index('black_') : black_piece.index(self.image_extension)  ]
				black_piece_image = img_black_pieces[index]
				black_piece_position = [ black_piece_xpos, black_piece_ypos ]
				black_piece_sprite = ChessPiece(name = black_piece_name , color = 'black', position = black_piece_position , is_taken = False, image = black_piece_image)
				black_piece_objects.append(black_piece_sprite)


				white_piece_name = white_piece[ white_piece.index('white_') : white_piece.index(self.image_extension) ]
				white_piece_image = img_white_pieces[index]
				white_piece_position = [ white_piece_xpos, white_piece_ypos]
				white_piece_sprite = ChessPiece(name = white_piece_name , color = 'white', position = white_piece_position , is_taken = False, image = white_piece_image)
				white_piece_objects.append(white_piece_sprite)


				#Add Chess Piece objetcs (black/white) to a list. In order to get all the pieces in one place with their attributes. Before adding to the GUI
				self.all_sprites.add(black_piece_sprite)
				self.all_sprites.add(white_piece_sprite)


				#Change horizontal(x) the same, keep vertical position (y) the same
				black_piece_xpos , black_piece_ypos = black_piece_xpos + 23, black_piece_ypos
				white_piece_xpos , white_piece_ypos = white_piece_xpos + 23, white_piece_ypos

			#Start to set up all the pawns (black and white). They need a new row (new y coordinate)
			else:

				white_pawn_image = img_white_pawns[pawn_list_index]
				white_pawn_position = [ white_pawn_xpos , white_pawn_ypos ]
				white_pawn_sprite = ChessPiece(name = 'pawn' , color = 'white', position = white_pawn_position , is_taken = False, image = white_pawn_image)
				white_piece_objects.append(white_pawn_sprite)


				black_pawn_image = img_black_pawns[pawn_list_index]
				black_pawn_position = [ black_pawn_xpos , black_pawn_ypos ]
				black_pawn_sprite = ChessPiece(name = 'pawn' , color = 'black', position = black_pawn_position , is_taken = False, image = black_pawn_image)				
				black_piece_objects.append(black_pawn_sprite)

				self.all_sprites.add(black_pawn_sprite)
				self.all_sprites.add(white_pawn_sprite)

				#Keep horizontal(x) the same, change vertical position (y)
				black_pawn_xpos , black_pawn_ypos = black_pawn_xpos + 23, black_pawn_ypos
				white_pawn_xpos , white_pawn_ypos = white_pawn_xpos + 23, white_pawn_ypos

				pawn_list_index += 1 

		return white_piece_objects , black_piece_objects


	
	def set_window(self):

		window = pygame.display.set_mode([500,500])
		window.fill((106, 168, 176))
		pygame.display.set_caption("Online Chess")	

		board_image_path = os.path.join(os.path.dirname(__file__), '../images/board.png')
		chess_board_image = pygame.image.load(board_image_path).convert_alpha()
		chess_board_image = pygame.transform.scale(chess_board_image , (180,180))

		#The topleft of the Surface will be placed at the position.
		window.blit(chess_board_image , (90,150) )
		return window
	
