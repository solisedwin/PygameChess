import pygame
from gui_setup.setup import ChessSetup
from pygame.time import Clock
import sys
from game_play.player import Player
from game_play.game import GamePlay


WHITE = (255, 255, 255)
RED = (255, 0, 0)

class RunGame(object):

	def __init__(self):
		pygame.init()


	def handle_events(self, sprites, screen, game_play):
	
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				game_running = False	
				pygame.quit()	
				sys.exit(1)
			
			if event.type == pygame.MOUSEBUTTONUP:

				pos = pygame.mouse.get_pos()
				completed_turn = False

				for chess_piece_sprite in sprites:

					if game_play.get_clicked_choosen_piece(screen, pos, chess_piece_sprite) is not None:

						#First time clicking a piece
						if game_play.current_player.piece_clicked is None:
							game_play.current_player.piece_clicked = chess_piece_sprite
							break

						#Second time player clicked to tell the piece where to move 
						else:

							game_play.validate_piece_move(chess_piece_sprite)


	def main(self):
		
		chess_settings = ChessSetup()
		screen = chess_settings.set_window()
		
		empty_board = [[0 for x in range(8)] for _ in range(8)]

		#Set up Chess Piece Sprite Objects by name, color, position, image..etc
		white_pieces , black_pieces = chess_settings.setup_pieces()
		#Fill the chess board with pieces and empty spaces get a value of None
		chess_board = chess_settings.fill_chess_board(empty_board , white_pieces , black_pieces)
	
		all_sprites = chess_settings.all_sprites

		clock = Clock()

		white_player = Player('Edwin', 'White', True, None , [], False)
		black_player = Player('Kayne', 'Black', False, None , [], False)

		game_running = True
		current_player = white_player

		game_play_object = GamePlay(chess_board =  chess_board, player1 =  white_player , player2 = black_player)


		while game_running:
			clock.tick(30)
			self.handle_events(all_sprites, screen, game_play_object)
			chess_settings.all_sprites.draw(screen)

			# *after* drawing everything
			pygame.display.flip()

		pygame.display.quit() 
		


if __name__ == '__main__':	
	play_game = RunGame()
	play_game.main() 
