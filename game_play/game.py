import sys
import pygame
import os
#sys.path.insert(0, "/home/edwin/Desktop/environment/Chess/src/gui_setup/piece.py")
from gui_setup.piece import ChessPiece, EmptySpace

class GamePlay(object):
	def __init__(self, chess_board = None , chess_sprites = None , player1 = None, player2 = None):
		self.chess_board = chess_board
		self.chess_sprites = chess_sprites
		# Player Objects
		self.player1 = player1
		self.player2 = player2
		self.current_player = player1

	def get_clicked_choosen_piece(self, screen , pos, chess_piece):
		
		if not chess_piece.rect.collidepoint(pos):
			return None

		has_intital_piece = self.current_player.piece_clicked is not None

		if isinstance(chess_piece , ChessPiece) and chess_piece.color.strip() == self.current_player.color.strip():
			chess_piece.draw_red_border(screen)
			print('Clicked on piece: ' + str(chess_piece.name))
			return chess_piece

		#Second click to tell the player which piece to capture.
		elif isinstance(chess_piece , ChessPiece) and chess_piece.color.strip() == self.current_player.color.strip():
			print('Clicked on 2nd piece to capture. ' + chess_piece.name)
			return chess_piece

		#Second click to tell the player where to move the chess piece. Where its an empty space in this situation
		elif isinstance(chess_piece , EmptySpace) and has_intital_piece:
			return True
		else:
			return None


	def validate_piece_move(self, chess_destination_piece):

		current_piece = self.current_player.piece_clicked

		#Wants to move to an empty spot. Check moves of moveable piece
		if chess_destination_piece.name == 'Empty':
			is_valid_move = current_piece.valid_moves(chess_board = self.chess_board , destination_piece = chess_destination_piece)
			return is_valid_move
		else:
			pass


	def move_piece(self, destination_space):
		moveable_piece = self.current_player.piece_clicked

		#Save information somewhere for our new empty space sprite
		original_rect = moveable_piece.rect
		original_board_position = moveable_piece.board_position
		original_x,original_y = moveable_piece.board_position[0] , moveable_piece.board_position[1]

		moveable_piece.rect = destination_space.rect
		moveable_piece.board_position = destination_space.board_position		
		
		new_empty_space = self.deep_copy_space_sprite(destination_space,surface_pos = original_rect,board_position = original_board_position)
	
		#Add empty space from location where piece was moved. x,y corrdinate
		self.chess_board[original_x][original_y] = new_empty_space
		self.chess_board[destination_space.board_position[0]][destination_space.board_position[1]] = moveable_piece
		return new_empty_space


	def deep_copy_space_sprite(self, destination_space ,  surface_pos , board_position):
		new_emptyspace = EmptySpace(destination_space.name , surface_pos = surface_pos , board_position = board_position)
		self.chess_sprites.remove(destination_space)
		self.chess_sprites.add(new_emptyspace)
		return new_emptyspace
