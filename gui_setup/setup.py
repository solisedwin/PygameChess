import os
import pygame 
from pygame.sprite import Group as SpriteGroup
from .piece import EmptySpace, Pawn, Rook, Bishop, Knight, King, Queen

class ChessSetup():
	def __init__(self):
		self.screen_width = 500
		self.screen_height = 500
		self.chess_board_height = 180
		self.chess_board_width = 180
		self.all_sprites = SpriteGroup()
		self.image_extension = '.png'

		self.pieces = ['rook','knight','bishop','king','queen','bishop','knight','rook']
		#Each player will have eight pawns
		self.pawns = ['pawn'] * 8

	def fill_chess_board(self, board , white_pieces, black_pieces):
		empty_space_inital_x = 96
		empty_space_x = 96  
		empty_space_y = 127

		for row in range(8):			
			empty_space_y += 23	
			#Go back to the start of a row
			empty_space_x = empty_space_inital_x

			for col in range(8):
				if row == 0:
					black_pieces[col].board_position = [row, col] 
					board[row][col] = black_pieces[col]
				elif row == 1:
					black_pieces[8 + col ].board_position = [row, col]
					board[row][col] = black_pieces[8 + col]
				elif row == 6:
					white_pieces[8 + col].board_position = [row, col]
					board[row][col] = white_pieces[8 + col]
				elif row == 7:
					white_pieces[col].board_position = [row, col]
					board[row][col] = white_pieces[col]
				else:
					board[row][col] = EmptySpace('Empty', surface_pos=[empty_space_x,empty_space_y], board_position = [row, col])
					self.all_sprites.add(board[row][col])
					#Move horizontal across board
					empty_space_x += 21
		return board


	def setup_pieces(self):
		img_black_pieces = ['black_' + (piece) + self.image_extension for piece in self.pieces]
		img_white_pieces = ['white_' + (piece) + self.image_extension for piece in self.pieces]
		
		img_black_pawns = ['black_' + (piece) + self.image_extension for piece in self.pawns]
		img_white_pawns = ['white_' + (piece) + self.image_extension for piece in self.pawns]

		#Set intital x,y coordinates (top left for black, bototm left for white) when first displating pieces
		black_piece_xpos, black_piece_ypos = 100,160
		white_piece_xpos, white_piece_ypos = 100, self.screen_height - 180

		black_pawn_xpos, black_pawn_ypos =  100, 185 
		white_pawn_xpos, white_pawn_ypos =  100, self.screen_height - 205
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

				black_piece_name = black_piece[ black_piece.index('black_') + 6 : black_piece.index(self.image_extension)]
				black_piece_image = img_black_pieces[index]
				black_piece_position = [black_piece_xpos, black_piece_ypos]
				
				black_piece_sprite = self.chess_piece_factory(name=black_piece_name, color='black', position=black_piece_position, is_taken=False, image=black_piece_image) 
				black_piece_objects.append(black_piece_sprite)

				white_piece_name = white_piece[ white_piece.index('white_') + 6: white_piece.index(self.image_extension)]
				white_piece_image = img_white_pieces[index]
				white_piece_position = [white_piece_xpos, white_piece_ypos]
				
				white_piece_sprite = self.chess_piece_factory(name=white_piece_name, color='white', position=white_piece_position, is_taken=False, image=white_piece_image) 
				white_piece_objects.append(white_piece_sprite)

				#Add Chess Piece objetcs (black/white) to a list. In order to get all the pieces in one place with their attributes. Before adding to the GUI
				self.all_sprites.add(black_piece_sprite)
				self.all_sprites.add(white_piece_sprite)

				#Change horizontal(x) the same, keep vertical position (y) the same
				black_piece_xpos = black_piece_xpos + 23
				white_piece_xpos = white_piece_xpos + 23

			#Start to set up all the pawns (black and white). They need a new row (new y coordinate)
			else:
				white_pawn_image = img_white_pawns[pawn_list_index]
				white_pawn_position = [white_pawn_xpos, white_pawn_ypos]
								
				white_pawn_sprite = self.chess_piece_factory(name='pawn', color='white', position=white_pawn_position, is_taken=False, image=white_pawn_image) 
				white_piece_objects.append(white_pawn_sprite)

				black_pawn_image = img_black_pawns[pawn_list_index]
				black_pawn_position = [black_pawn_xpos, black_pawn_ypos ]

				black_pawn_sprite = self.chess_piece_factory(name='pawn', color='black', position=black_pawn_position, is_taken=False, image=black_pawn_image)

				black_piece_objects.append(black_pawn_sprite)

				self.all_sprites.add(black_pawn_sprite)
				self.all_sprites.add(white_pawn_sprite)

				#Change horizontal(x) the same, keep vertical position (y)
				black_pawn_xpos = black_pawn_xpos + 23
				white_pawn_xpos = white_pawn_xpos + 23
				pawn_list_index += 1
		return white_piece_objects, black_piece_objects

	def chess_piece_factory(self, name, color, position, is_taken,image):
		if name == "pawn":
			return Pawn(name=name, color=color, position=position, is_taken=is_taken, image=image)
		if name == "rook":
			return Rook(name=name, color=color, position=position,is_taken = is_taken, image=image)
		if name == "bishop":
			return Bishop(name=name, color=color, position=position, is_taken=is_taken, image = image)
		if name == "king":
			return King(name=name, color = color, position=position, is_taken=is_taken, image=image)
		if name == "queen":
			return Queen(name=name, color=color, position=position, is_taken=is_taken, image=image)
		if name == "knight":
			return Knight(name=name, color=color, position=position, is_taken=is_taken, image=image)
		raise ValueError('UnKnown chess piece that cant be made')

	def set_window(self):
		window = pygame.display.set_mode([500, 500])
		window.fill((106, 168, 176))
		pygame.display.set_caption("Online Chess")	
		return window

	def get_main_board_image(self):
		board_image_path = os.path.join(os.path.dirname(__file__), '../images/board.png')
		chess_board_image = pygame.image.load(board_image_path).convert_alpha()
		chess_board_image = pygame.transform.scale(chess_board_image, (180,180))
		return chess_board_image