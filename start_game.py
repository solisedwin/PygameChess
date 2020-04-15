
import pygame
from chess_gui.setup import ChessSetup
from pygame.time import Clock
import sys
import time
from game_play.player import Player
from chess_gui.piece import ChessPiece, EmptySpace


WHITE = (255, 255, 255)
RED = (255, 0, 0)

class RunGame(object):

	def __init__(self):
		pygame.init()


	def handle_events(self, sprites, screen, current_player , chess_board):
		
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				game_running = False
				pygame.quit()	
				sys.exit(1)
			
			if event.type == pygame.MOUSEBUTTONUP:

				pos = pygame.mouse.get_pos()
				completed_turn = False

				for chess_piece in sprites:

					if hasattr(chess_piece, 'draw_green_border'):
						chess_piece.draw_green_border(screen)

					#We check if we have clicked on a chess piece and its the right players turn and the save the information that the player hasnt choosen a piece yet 
					if chess_piece.rect.collidepoint(pos) and isinstance(chess_piece , ChessPiece ) and current_player.turn and current_player.piece_clicked is None:

						#If chess piece was clicked , get only first item
						chess_piece.draw_red_border(screen)	

						#Sprite Object that reprsents Chess Piece
						current_player.piece_clicked =  chess_piece 
						print('Clicked on piece: ' + str(chess_piece.name))	

					#Second click to tell the player which piece to capture.
					elif chess_piece.rect.collidepoint(pos) and isinstance(chess_piece , ChessPiece) and current_player.turn and current_player.piece_clicked is not None:
						print('Clicked on 2nd piece to capture')
							
					#Second click to tell the player where to move the chess piece. Where its an empty space in this situation	
					elif chess_piece.rect.collidepoint(pos) and isinstance(chess_piece , EmptySpace) and current_player.turn and current_player.piece_clicked is not None:
						print('Clicked on empty space to move piece !!!!')
						
						clicked_board_destination = chess_piece
						current_player.piece_clicked.valid_moves(chess_board =  chess_board,  destination_space = clicked_board_destination)
					else:
						pass

					
	def main(self):
		
		chess = ChessSetup()
		screen = chess.set_window()
		
		empty_board = [[0 for x in range(8)] for _ in range(8)]

		#Set up Chess Piece Sprite Objects by name, color, position, image..etc
		white_pieces , black_pieces = chess.setup_pieces()
		#Fill the chess board with pieces and empty spaces get a value of None
		chess_board = chess.fill_chess_board(empty_board , white_pieces , black_pieces)
	
		clock = Clock()

		white_player = Player('Edwin', 'White', True, None , [], False)
		black_player = Player('Kayne', 'Black', False, None , [], False)

		game_running = True
		current_player = white_player

		while game_running:

			clock.tick(30)
			self.handle_events(chess.all_sprites, screen, current_player , chess_board)
			chess.all_sprites.draw(screen)

			# *after* drawing everything
			pygame.display.flip()

		pygame.display.quit() 
		


if __name__ == '__main__':	
	play_game = RunGame()
	play_game.main() 
