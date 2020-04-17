import sys
import pygame
import os 
sys.path.insert(0, "/home/edwin/Desktop/environment/Chess/src/gui_setup/piece.py")
from gui_setup.piece import ChessPiece, EmptySpace

class GamePlay(object):
	def __init__(self, chess_board = None , player1 = None, player2 = None):
		self.chess_board = chess_board
		# Player Objects
		self.player1 = player1
		self.player2 = player2
		self.current_player = player1 


	def get_clicked_choosen_piece(self, screen , pos, chess_piece):

		if not self.current_player.turn:
			return None	

		if not chess_piece.rect.collidepoint(pos):
			return None

		if isinstance(chess_piece , ChessPiece ) and self.current_player.piece_clicked is None:
			chess_piece.draw_red_border(screen)	
			self.current_player.piece_clicked =  chess_piece 
			print('Clicked on piece: ' + str(chess_piece.name))	
			return chess_piece

		#Second click to tell the player which piece to capture.
		elif isinstance(chess_piece , ChessPiece) and self.current_player.piece_clicked is not None:
			print('Clicked on 2nd piece to capture')
			return chess_piece
			
		#Second click to tell the player where to move the chess piece. Where its an empty space in this situation	
		elif isinstance(chess_piece , EmptySpace) and self.current_player.piece_clicked is not None:
			print('Clicked on empty space to move piece !!!!')
			return chess_piece
		else:
			return None


	def validate_piece_move(self, chess_destination_piece):
		
		destination_xpos , destination_ypos = chess_destination_piece.board_position[0] , chess_destination_piece.board_position[1]

		# Check if player wants to move to a spot where its either empty or another opposing piece is occupied

		#Wants to move to an empty spot. Check moves of moveable piece
		if chess_destination_piece.name == 'Empty':

			is_valid_move = self.current_player.piece_clicked.valid_moves( chess_board = self.chess_board , destination_piece = chess_destination_piece	)

			if is_valid_move:
				print('Great . Is a valid move for ' + self.current_player.piece_clicked.name)
				self.move_piece(chess_destination_piece)
			else:
				print('!! Not a valid move at all !')
		


	def move_piece(self, destination_space):
		pass




		
