
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
					
					#We check if we have clicked on a chess piece and its the right players turn and the save the information that the  player hasnt choosen a piece yet 
					if chess_piece.rect.collidepoint(pos) and isinstance(chess_piece , pygame.sprite.Sprite) and current_player.turn and current_player.piece_clicked is None:

						#If chess piece was clicked , get only first item
						clicked_chess_piece = [chess_piece for chess_piece in sprites if chess_piece.rect.collidepoint(pos)][0]	
						clicked_chess_piece.draw_red_border(screen)

						#Sprite Object that reprsents Chess Piece
						current_player.piece_clicked =  clicked_chess_piece 
						print('Clicked on piece: ' + str(clicked_chess_piece.name))	
						completed_turn = True		

					
				#We clicked on an empty square to move to and it should be in the bounds of the chess board
				if not completed_turn:	
					pos = list(pos)

					print('Trying to click where to move the piece')
					print('Clicked pos: ' + str(pos))


					for row in range(8):
						for col in range(8):

							#Clicked position where we want to move the piece.  
							if chess_board[row][col].board_position[0] == pos[0] and chess_board[row][col].board_position[1] == pos[1]:

								#Check if we want to move to an empty spot, or a spot where we want to capture a piece
								destination_spot = chess_board[row][col]

								if isinstance(destination_spot , EmptySpace ):
									print('Clicked on empty chess board space !! We want to move to empty space')

								elif isinstance(destination_spot , ChessPiece):
									print('** Clicked on another piece. A piece we want to capture !')
								else:
									print('I have no fucking idea what we clicked on')

					completed_turn = True



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