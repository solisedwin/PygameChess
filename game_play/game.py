import sys
import pygame
from ..chess_gui.piece import ChessPiece, EmptySpace
sys.path.append("../gui_setup/piece")
import ChessPiece, EmptySpace

class GamePlay(object):
	"""docstring for GameMoves"""
	def __init__(self, chess_board = None , player1 = None, player2 = None):
		self.chess_board = chess_board
		self.player1 = player1
		self.player2 = player2
		self.current_player = player1 



	def get_clicked_choosen_piece(self, screen pos, chess_piece):

		#We check if we have clicked on a chess piece and its the right players turn and the save the information that the player hasnt choosen a piece yet 
		if chess_piece.rect.collidepoint(pos) and isinstance(chess_piece , ChessPiece ) and self.current_player.turn and current_player.piece_clicked is None:

			chess_piece.draw_red_border(screen)	

			current_player.piece_clicked =  chess_piece 
			print('Clicked on piece: ' + str(chess_piece.name))	
			return chess_piece

		#Second click to tell the player which piece to capture.
		elif chess_piece.rect.collidepoint(pos) and isinstance(chess_piece , ChessPiece) and current_player.turn and current_player.piece_clicked is not None:
			print('Clicked on 2nd piece to capture')
			return chess_piece
			

		#Second click to tell the player where to move the chess piece. Where its an empty space in this situation	
		elif chess_piece.rect.collidepoint(pos) and isinstance(chess_piece , EmptySpace) and current_player.turn and current_player.piece_clicked is not None:
			print('Clicked on empty space to move piece !!!!')
			return chess_piece

			clicked_board_piece = chess_piece
			destination_xpos , destination_ypos = clicked_board_piece.board_position[0] , clicked_board_piece.board_position[1]

			is_valid_move = current_player.piece_clicked.valid_moves(chess_board =  chess_board,  destination_piece =  clicked_board_piece)
		else:
			pass


	def move_piece(self):
		pass




		
